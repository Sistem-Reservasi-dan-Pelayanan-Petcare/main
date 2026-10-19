import json
import os
import pwinput
from prettytable import PrettyTable
import time

users = []

def clearpause():
    input("\nKlik Enter untuk kembali ke menu...")
    os.system("cls" if os.name == "nt" else "clear")
def clears():
    os.system("cls" if os.name == "nt" else "clear")

def input_angka(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai > 0:
                return nilai
            print("Harus lebih dari 0.")
        except ValueError:
            print("Masukkan angka yang valid.")

def readjson(jsfile):
    with open (jsfile, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

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
        print("2: Topup Saldo User")
        print("3: Hapus User")
        print("0: Kembali")
        opsi = input("Pilih opsi: ")

        if opsi == "1":
            tabel = PrettyTable()
            tabel.title = "LIST USER"
            tabel.field_names = ["ID", "Username", "Saldo"]
            for u in data:
                if u["role"] == "user":
                    tabel.add_row([u["id"], u["username"], f"Rp.{u['saldo']}"])
            print(tabel)
            clearpause()

        elif opsi == "2":
            try:
                uid = int(input("Masukkan ID User: "))
                jumlah = int(input("Masukkan jumlah topup: "))
            except ValueError:
                print("Input harus berupa angka")
                clearpause()
                continue

            if jumlah <=0:
                print("Jumlah harus lebih dari 0")
                clearpause()
                continue

            for u in data:
                if u["id"] == uid and u["role"] == "user":
                    u["saldo"] += jumlah
                    writejson("users.json", data)
                    print(f"Topup berhasil, Saldo {u['username']}: {u['saldo']}")
                    break
            else:
                print("User tidak ditemukan")
            clearpause()

        elif opsi == "3":
            try:
                uid = int(input("Masukkan ID user yang ingin dihapus: "))
            except ValueError:
                print("ID harus berupa angka")
                continue

            userdel = next((u for u in data if u["id"] == uid and u["role"] == "user"), None)
            if userdel is None:
                print("User tidak ditemukan")
            else:
                confirm = input(f"Hapus user {userdel['username']}? (y/n): ")
                if confirm == "y":
                    data.remove(userdel)
                    writejson("users.json", data)
                    reservations = readjson("reservations.json")
                    reservations = [r for r in reservations if r.get("user_id") != uid]
                    writejson("reservations.json", reservations)
                    print("User berhasil dihapus")
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
                clearpause()
                
            elif opsi == "2":
                resid = int(input("Masukkan ID Reservasi yang ingin dibatalkan: "))
                target = next((r for r in data if r["res_id"] == resid), None)
                if target is None:
                    print("Reservasi tidak ditemukan")
                else:
                    confirm = input(f"Batalkan reservasi {resid} ({target['layanan']}, hewan '{target['nama']}')? (y/n): ").strip().lower()
                if confirm == "y":
                    data.remove(target)
                    writejson("reservations.json", data)
                    print("Reservasi dibatalkan")
                else:
                    print("Dibatalkan")
                clearpause()

            elif opsi == "0":
                clears()
                break

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
        "saldo": 0
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
                nama = input("Masukkan nama hewan: ")
                jenis = input("Masukkan jenis hewan: ")
                berat = input_angka("Masukkan berat badan hewan (kg bulat): ")
                jam = input("Masukkan jam datang: ")
                tanggal = input("Masukkan tanggal datang (DD/MM): ")

                if berat <= 0:
                    print("Berat tidak boleh 0")
                    continue
                elif berat <= 10:
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
                print("Reservasi berhasil")
                clearpause()
                break

            elif opsi == "2":
                nama = input("Masukkan nama hewan: ")
                jenis = input("Masukkan jenis hewan: ")
                malam = input_angka("Masukkan jumlah malam penitipan: ")
                tanggal = input("Masukkan tanggal datang (DD/MM): ")
                jam = input("Masukkan jam datang (JJ:MM): ")

                if malam <= 0: 
                    print("Jumlah malam harus lebih dari 0")
                    continue

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
                print("Reservasi berhasil")
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
            reservasi(user)
            clears()
        elif opsi == "3":
            print("Andaikan ini menu saldo dan pembayaran")
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
            manageusers()
            clears()
        elif opsi == "2":
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