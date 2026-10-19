import json
import os
import pwinput
from prettytable import PrettyTable
import time

users = []

def clears():
    input("\nKlik Enter untuk kembali ke menu...")
    os.system("cls" if os.name == "nt" else "clear")
    
def readjson(jsfile):
    with open (jsfile, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def writejson(jsfile, data):
    with open(jsfile, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def tambah_reservasi(data_baru):
    data = readjson("reservations.json")
    data.append(data_baru)
    writejson("reservations.json", data)

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
        try:
            print("Reservasi Layanan")
            print("1: Perawatan")
            print("2: Penitipan")
            print("3: Lihat Reservasi")
            print("0: Keluar")
            opsi = input("Pilih layanan: ")

            if opsi == "1":
                nama = input("Masukkan nama hewan: ")
                jenis = input("Masukkan jenis hewan: ")
                berat = int(input("Masukkan berat badan hewan (kg bulat): "))
                jam = input("Masukkan jam datang: ")
                tanggal = input("Masukkan tanggal datang (HH/BB): ")

                if berat <= 0:
                    print("Berat tidak boleh 0")
                    continue
                elif berat <= 10:
                    harga = 75000
                else:
                    harga = 100000

                data = {
                    "user_id": user["id"],
                    "layanan": "Perawatan",
                    "nama": nama,
                    "jenis": jenis,
                    "berat": berat,
                    "jam": jam,
                    "tanggal": tanggal,
                    "harga": harga,
                    "status": "Belum lunas"
                }

                tambah_reservasi(data)
                print("Reservasi berhasil")
                break

            elif opsi == "2":
                nama = input("Masukkan nama hewan: ")
                jenis = input("Masukkan jenis hewan: ")
                malam = int(input("Masukkan jumlah malam penitipan: "))
                tanggal = input("Masukkan tanggal datang (HH/BB): ")
                jam = input("Masukkan jam datang (JJ:MM): ")

                if malam <= 0: 
                    print("Jumlah malam harus lebih dari 0")
                    continue

                harga = 150000 * malam

                data= {
                    "user_id": user["id"],
                    "layanan": "Penitipan",
                    "nama": nama,
                    "jenis": jenis,
                    "malam": malam,
                    "tanggal": tanggal,
                    "jam": jam,
                    "harga": harga,
                    "status": "Belum lunas"
                }

                tambah_reservasi(data)
                print("Reservasi berhasil")
                break

            elif opsi == "3":
                lihat_reservasi(user)
            elif opsi == "0":
                break
            else:
                print("Opsi tidak valid")
        except ValueError:
            print("Masukkan angka yang sesuai")

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
            clears()
        elif opsi == "2":
            reservasi(user)
            clears()
        elif opsi == "3":
            print("Andaikan ini menu saldo dan pembayaran")
        elif opsi == "0":
            break
        else:
            print("Opsi tidak valid")

def menu_admin(user):
    while True:
        print("Ini adalah menu admin")
        time.sleep(3)
        break

def login():
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")

    users = readjson("users.json")
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login berhasil")
            identitas = ["id"]
            if user["role"] == "admin":
                menu_admin(user)
            else:
                menu_user(user)
            return
    
def main():
    while True:
        print("Selamat datang di aplikasi PetCare")
        print("1: Login")
        print("2: Register")
        print("0: Keluar")
        opsi = input("Pilih menu: ")

        if opsi == "1":
            os.system("cls" if os.name == "nt" else "clear")
            login()
        elif opsi == "2":
            print("Andaikan ini menu registrasi")
        elif opsi == "0":
            print("Terimakasih")
            break
        else:
            print("Opsi tidak valid")

main()