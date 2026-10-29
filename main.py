import json
import os
import pwinput
from prettytable import PrettyTable
import time
from datetime import datetime

users = []
allowedanimals = ["kucing", "anjing"]

def clearpause():
    input("\nKlik Enter untuk kembali ke menu...")
    os.system("cls" if os.name == "nt" else "clear")
def clears():
    os.system("cls" if os.name == "nt" else "clear")

def input_angka(pesan, maks=None):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai <= 0:
                print("Harus lebih dari 0.")
            elif maks is not None and nilai > maks:
                print(f"Maksimal {maks}kg.")
            else:
                return nilai
        except ValueError:
            print("Masukkan angka yang valid.")
            
def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks:
            return teks
        print("Input tidak boleh kosong.")

def input_tanggal(pesan):
    while True:
        teks = input(pesan).strip()
        try:
            tgl = datetime.strptime(f"{teks}/{datetime.now().year}", "%d/%m/%Y")
            return tgl.strftime("%d/%m")
        except ValueError:
            print("Tanggal tidak valid. Contoh: 05/03")

def input_jam(pesan):
    while True:
        teks = input(pesan).strip()
        try:
            jam = datetime.strptime(teks, "%H:%M")
            return jam.strftime("%H:%M")
        except ValueError:
            print("Jam tidak valid. Contoh: 09:30")

def input_hewan(pesan):
    while True:
        teks = input(pesan).strip().lower()
        if teks in allowedanimals:
            return teks
        print(f"Hewan tidak diterima. Hanya boleh: {', '.join(allowedanimals)}")

def tabeluser(userdata):
    data = userdata
    tabel = PrettyTable()
    tabel.title = "LIST USER"
    tabel.field_names = ["ID", "Username", "Saldo", "Status"]
    for u in data:
        if u["role"] == "user":
            tabel.add_row([u["id"], u["username"], f"Rp.{u['saldo']}", u.get("status", "aktif")])
    print(tabel)

def tabelreserv(datareserv):
    data = datareserv
    tabel = PrettyTable()
    tabel.title = "LIST RESERVASI"
    tabel.field_names = ["ID", "User ID", "Layanan", "Nama", "Jenis",
                            "Berat/Malam", "Tanggal", "Jam", "Harga", "Status"]
    for r in data:
        detail = f"{r['berat']} kg" if r["layanan"] == "Perawatan" else f"{r['malam']} malam"
        tabel.add_row([r["res_id"], r["user_id"], r["layanan"], r["nama"],
                        r["jenis"], detail, r["tanggal"], r["jam"],
                        f"Rp.{r['harga']}", r["status"]])
    print(tabel)

def readjson(jsfile):
    try:
        with open(jsfile, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def writejson(jsfile, data):
    with open(jsfile, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def tambah_data(data_baru, jsfile):
    data = readjson(jsfile)
    data.append(data_baru)
    writejson(jsfile, data)

def res_id_new():
    data = readjson("reservations.json")
    return max((r["res_id"] for r in data), default=2000) + 1

def manageusers():
    while True:
        data = readjson("users.json")
        print("Manajemen User")
        print("1: Lihat User")
        print("2: Nonaktifkan/Aktifkan User")
        print("0: Kembali")
        opsi = input("Pilih opsi: ")

        if opsi == "1":
            tabeluser(data)
            clearpause()

        elif opsi == "2":
            tabeluser(data)
            try:
                uid = int(input("Masukkan ID user yang ingin dinonaktifkan: "))
            except ValueError:
                print("ID harus berupa angka")
                clearpause()
                continue

            target = next((u for u in data if u["id"] == uid and u["role"] == "user"), None)
            if target is None:
                print("User tidak ditemukan")
            else:
                current = target.get("status", "aktif")
                new = "nonaktif" if current == "aktif" else "aktif"
                confirm = input(f"Ubah status {target['username']} dari {current} ke {new}? (y/n): ")
                if confirm.strip().lower() == "y":
                    target["status"] = new
                    writejson("users.json", data)
                    print(f"Status {target['username']} sekarang {new}")
                else:
                    print("Dibatalkan")
            clearpause()
        elif opsi == "0":
            break
        else:
            clears()
            print("Opsi tidak valid")

def managereserv():
    while True:
        try:
            data = readjson("reservations.json")
            print("Manajemen Reservasi")
            print("1: List Reservasi")
            print("2: Membatalkan Reservasi")
            print("0: Keluar")
            opsi = input("Pilih opsi: ")

            if opsi == "1":
                if not data:
                    print("Belum ada reservasi.")
                else:
                    tabelreserv(data)
                clearpause()
                
            elif opsi == "2":
                tabelreserv(data)
                resid = int(input("Masukkan ID Reservasi yang ingin dibatalkan: "))
                resselect = next((r for r in data if r["res_id"] == resid), None)
                if resselect is None:
                    print("Reservasi tidak ditemukan")
                    clearpause()
                else:
                    confirm = input(f"Batalkan reservasi {resid} ({resselect['layanan']}, hewan '{resselect['nama']}')? (y/n): ")
                    if confirm == "y":
                        if resselect["status"] == "Lunas":
                            users = readjson("users.json")
                            for u in users:
                                if u["id"] == resselect["user_id"]:
                                    u["saldo"] += resselect["harga"]
                            writejson("users.json", users)
                        data.remove(resselect)
                        writejson("reservations.json", data)
                        print("Reservasi dibatalkan")
                        clearpause()
                    else:
                        print("Reservasi tidak dibatalkan")
                        clearpause()

            elif opsi == "0":
                break
            else:
                print("Opsi tidak valid")
                clearpause()

        except ValueError:
            print("ID harus berupa angka")
            clearpause()
            continue

def registrasi():
    users = readjson("users.json")
    usn = input("Masukkan username: ")
    if not usn:
        print("Username tidak boleh kosong!")
        clearpause()
        return
    elif any(u["username"] == usn for u in users):
        print("Username sudah dipakai!")
        clearpause()
        return
    else:
        psw = pwinput.pwinput("Masukkan password: ")
        if len (psw) < 8:
            print("Password harus minimal 8 karakter")
            clearpause()
            return

    data = {
        "id": max((user["id"] for user in users), default=1000) + 1,
        "username": usn,
        "password": psw,
        "role": "user",
        "saldo": 0,
        "status": "aktif"
    }

    tambah_data(data, "users.json")

    print("Registrasi berhasil")
    clearpause()

def layanan():
    pelayanan = PrettyTable()
    pelayanan.title = "LAYANAN YANG TERSEDIA"
    pelayanan.field_names = ["Layanan", "Harga"]
    pelayanan.add_row(["Perawatan (Grooming)", "Rp.75k - Rp.100k"])
    pelayanan.add_row(["Penitipan (Daycare)", "Rp.150k/malam"])
    print(pelayanan)

def lihat_reservasi(user):
    data = readjson("reservations.json")
    milik_user = [reservasi for reservasi in data if reservasi.get("user_id") == user["id"]]
    if not milik_user:
        print("Tidak ada reservasi")
        return

    tabel = PrettyTable()
    tabel.title = "RESERVASI"
    tabel.field_names = ["Layanan", "Nama", "Jenis", "Berat/Malam", "Tanggal", "Jam", "Harga", "Status"]

    for data in milik_user:
        if data["layanan"] == "Perawatan":
            tabel.add_row([data["layanan"], data["nama"], data["jenis"], f"{data['berat']} kg", data["tanggal"], data["jam"], f"Rp.{data['harga']}", data["status"]])
        elif data["layanan"] == "Penitipan":
            tabel.add_row([data["layanan"], data["nama"], data["jenis"], f"{data['malam']} malam", data["tanggal"], data["jam"], f"Rp.{data['harga']}", data["status"]])
    print(tabel)

def reservasi(user):
    while True:
            print("Reservasi Layanan")
            print("1: Perawatan")
            print("2: Penitipan")
            print("3: Lihat Reservasi")
            print("0: Keluar")
            opsi = input("Pilih layanan: ")

            if opsi == "1":
                nama = input_teks("Masukkan nama hewan: ")
                jenis = input_hewan("Masukkan jenis hewan (kucing/anjing): ")
                berat = input_angka("Masukkan berat badan hewan (kg bulat, maks: 120): ", maks=120)
                jam = input_jam("Masukkan jam datang: ")
                tanggal = input_tanggal("Masukkan tanggal datang (DD/MM): ")

                if berat <= 10:
                    harga = 75000
                else:
                    harga = 100000

                data = {
                    "user_id": user["id"],
                    "res_id": res_id_new(),
                    "layanan": "Perawatan",
                    "nama": nama,
                    "jenis": jenis,
                    "berat": berat,
                    "jam": jam,
                    "tanggal": tanggal,
                    "harga": harga,
                    "status": "Belum lunas"
                }

                tambah_data(data, "reservations.json")
                print(f"Reservasi berhasil dengan ID: {data['res_id']}")
                clearpause()
                break

            elif opsi == "2":
                nama = input_teks("Masukkan nama hewan: ")
                jenis = input_hewan("Masukkan jenis hewan (kucing/anjing): ")
                malam = input_angka("Masukkan jumlah malam penitipan: ")
                tanggal = input_tanggal("Masukkan tanggal datang (DD/MM): ")
                jam = input_jam("Masukkan jam datang (JJ:MM): ")

                harga = 150000 * malam

                data= {
                    "user_id": user["id"],
                    "res_id": res_id_new(),
                    "layanan": "Penitipan",
                    "nama": nama,
                    "jenis": jenis,
                    "malam": malam,
                    "tanggal": tanggal,
                    "jam": jam,
                    "harga": harga,
                    "status": "Belum lunas"
                }

                tambah_data(data, "reservations.json")
                print(f"Reservasi berhasil dengan ID: {data['res_id']}")
                clearpause()
                break

            elif opsi == "3":
                lihat_reservasi(user)
                clearpause()
            elif opsi == "0":
                break
            else:
                clears()
                print("Opsi tidak valid")

def topup(user):
    print("======== LIST NOMINAL TOPUP ========")
    print("1: Rp.200.000")
    print("2: Rp.100.000")
    print("3: Rp.50.000")
    print("4: Rp.20.000")
    opsi = input("Pilih jumlah topup: ")

    if opsi == "1":
        jumlah = 200000
    elif opsi == "2":
        jumlah = 100000
    elif opsi == "3":
        jumlah = 50000
    elif opsi == "3":
        jumlah = 20000
    else:
        print("Opsi Invalid")
        clearpause()
        return

    while True:
        password_input = pwinput.pwinput("Masukkan password: ")

        if password_input != user["password"]:
            print("Password salah")
        else:
            break

    user["saldo"] += jumlah
    users = readjson("users.json")
    for u in users:
        if u["id"] == user["id"]:
            u["saldo"] = user["saldo"]
    writejson("users.json", users)
    print("Top Up berhasil!")
    print("Saldo:", f"Rp.{user['saldo']}")
    clearpause()

def emoney(user):
    while True:
        print("\n=== E-MONEY ===")
        print("Saldo:", f"Rp.{user['saldo']}")
        print("1. Top Up")
        print("2. Bayar Reservasi")
        print("0. Kembali")

        pilih = input("Opsi: ")

        if pilih == "1":
            topup(user)

        elif pilih == "2":
            data = readjson("reservations.json")

            milik_user = [
                r for r in data
                if r["user_id"] == user["id"]
                and r["status"] == "Belum lunas"
            ]

            if not milik_user:
                print("Tidak ada reservasi yang belum dibayar.")
                clearpause()
                continue

            print("\n=== RESERVASI BELUM LUNAS ===")
            for r in milik_user:
                print(
                    f"ID: {r['res_id']} | "
                    f"{r['layanan']} | "
                    f"{r['nama']} | "
                    f"Rp.{r['harga']}"
                )

            resid = input_angka("Masukkan ID Reservasi: ")

            res = next(
                (r for r in milik_user if r["res_id"] == resid),
                None
            )
            if res is None:
                print("Reservasi tidak ditemukan")
                clearpause()
                continue
            harga = res["harga"]
            if user["saldo"] >= harga:
                user["saldo"] -= harga
                res["status"] = "Lunas"
                users = readjson("users.json")
                for u in users:
                    if u["id"] == user["id"]:
                        u["saldo"] = user["saldo"]
                writejson("users.json", users)
                writejson("reservations.json", data)
                invoices = readjson("invoices.json")

                invoice = {
                    "invoice_id": max((i["invoice_id"] for i in invoices), default=3000) + 1,
                    "res_id": res["res_id"],
                    "user_id": user["id"],
                    "nama": res["nama"],
                    "layanan": res["layanan"],
                    "harga": harga,
                    "status": "Lunas"
                }
                invoices.append(invoice)
                writejson("invoices.json", invoices)
                print("\n" + "=" * 35)
                print("          INVOICE PETCARE")
                print("=" * 35)
                print("ID Invoice :", invoice["invoice_id"])
                print("ID Reservasi:", invoice["res_id"])
                print("Nama Hewan :", invoice["nama"])
                print("Layanan    :", invoice["layanan"])
                print("Total Bayar:", f"Rp.{invoice['harga']}")
                print("Status     : LUNAS")
                print("Terimakasih, selamat datang kembali")
                print("=" * 35)
                clearpause()
                break

            else:
                print("Saldo tidak cukup!")
                confirm = input("Apakah kamu ingin topup saldo? (y/n)")
                if confirm == "y":
                    topup(user)
                else:
                    clears()
                    continue

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid!")

def menu_user(user):
    while True:
        print("======== MENU USER ========")
        print("1: Layanan")
        print("2: Reservasi")
        print("3: Saldo & Pembayaran")
        print("0: Logout")
        opsi = input("Pilih menu: ")

        if opsi == "1":
            layanan()
            clearpause()
        elif opsi == "2":
            clears()
            reservasi(user)
            clears()
        elif opsi == "3":
            clears()
            emoney(user)
            clears()
        elif opsi == "0":
            clears()
            break
        else:
            clears()
            print("Opsi tidak valid")

def menu_admin(user):
    while True:
        print("======== MENU ADMIN ========")
        print("1: Manajmen User")
        print("2: Manajemen Reservasi")
        print("0: Logout")
        opsi = input("Pilih menu: ")
        
        if opsi == "1":
            clears()
            manageusers()
            clears()
        elif opsi == "2":
            clears()
            managereserv()
            clears()
        elif opsi == "0":
            clears()
            break
        else:
            clears()
            print("Opsi tidak valid")

def login():
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")

    users = readjson("users.json")
    for user in users:
        if user["username"] == username and user["password"] == password:
            if user.get("status", "aktif") != "aktif":
                print("Akun kamu dinonaktifkan. Silakan hubungi admin.")
                time.sleep(2)
                clears()
                return
            print("Login berhasil")
            time.sleep(2)
            clears()
            if user["role"] == "admin":
                menu_admin(user)
            else:
                menu_user(user)
            return
        
    print("Username atau password salah.")
    time.sleep(2)
    clears()
    
def main():
    while True:
        print("Selamat datang di aplikasi PetCare")
        print("1: Login")
        print("2: Register")
        print("0: Keluar")
        opsi = input("Pilih menu: ")

        if opsi == "1":
            clears()
            login()
        elif opsi == "2":
            registrasi()
        elif opsi == "0":
            print("Terimakasih")
            break
        else:
            print("Opsi tidak valid")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")
