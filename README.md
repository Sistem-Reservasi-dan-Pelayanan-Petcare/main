# Sistem Reservasi dan Pelayanan Petcare<br>
**Praktikum DDP**
**Kelas             : A**<br>
**Anggota & Peran   :**<br>

<ol>
                    <li> Daffa Rian Hadisaputra (Coding)</li><br>
                    <li> Daffa Naufal Abiyyi (Flowchart dan coding)</li><br>
                    <li> Octavia Putri Vierene (Readme dan Flowchart)</li><br>
                    <li> Sabichisma Sania Rachman (Laporan) </li><br>
</ol>

<h2>Deskripsi & Tujuan:</h2><br>
Sistem Reservasi dan Pelayanan Pet Care merupakan sistem yang dirancang untuk memudahkan pelanggan dalam melakukan reservasi layanan perawatan hewan. Sistem ini memungkinkan pengguna untuk memilih jenis layanan, menentukan jadwal, mengelola data hewan, melihat status pelayanan, serta melakukan pembayaran. Di sisi admin, sistem digunakan untuk mengelola data layanan, reservasi, jadwal antrean, status pelayanan, dan pembayaran secara lebih teratur.

<h2>Flowchart:</h2><br>

**Menu Utama**<br>
Pada bagian menu utama terdapat pilihan 'login' bagi pengguna dan admin, 'registrasi' untuk pengguna yang belum meiliki akun, dan 'keluar' untuk keluar dari menu utama. Pada bagian login sistem akan mendeteksi apakah yang login adalah admin atau user jika yang login adalah user akan di arahkan ke menu user dan jika admin maka akan di arahkan ke menu admin. 

<img width="696" height="672" alt="image" src="https://github.com/user-attachments/assets/eab17ec2-2f78-49f3-8ef1-3c8ad11d658c" />

**Menu Registrasi**<br>
<img width="403" height="667" alt="image" src="https://github.com/user-attachments/assets/33cab28b-facf-4bae-aa5b-35735774d24b" />

Pada bagian registrasi, user akan membuat akun di mana penguna akan membuat username terlebih dahulu, apabila username sudah dipakai maka user akan diminta untuk memasukkan ulang namanya. Kemudian user memasukkan password


**Menu User atau Pengguna**<br>

<img width="2312" height="1722" alt="Menu Pengguna drawio" src="https://github.com/user-attachments/assets/63e76ba3-1251-4e4c-b890-96c71be956a2" />

Pada menu ini user di berikan beberapa menu pilihan:<br>
1. `Layanan` jika pengguna memillih opsi ini maka akan di tampilkan layanan apa saja yang tersedia.<br>
2. `Reservasi` jika pengguna memilih opsi ini maka sistem akan menampilkan `penitipan` dan `perawatan` serta `keluar` <br>
3. `Saldo & Pembayaran` jika pengguna memilih menu ini maka sistem akan menampilkan dua opsi lagi yaitu `top up` opsi ini di gunakan untuk top up saldo pengguna agar bisa membayar reservasi dan `pembayaran` adalah opsi di mana pengguna dapat membayar reservasi. <br>
0. `Keluar` jika pengguna memilih opsi ini maka pengguna akan di kembalikan ke menu sebelumnya. <br>


**Menu Admin**<br>

<img width="3222" height="1702" alt="admin fikss drawio" src="https://github.com/user-attachments/assets/377e70f6-d17f-45c7-9af9-56661bd7f7f7" />


Pada role admin terdapat pilihan:
1. `Manajemen user` jika admin memilih opsi ini maka akan menampilkan beberapa pilihan lain seperti `lihat user` dan `nonaktifkan/aktifkan user` <br>
2. `Manajemen Reservasi` jika admin memilih opsi ini maka akan menampilkan `list reservasi` berguna untuk melihat list Reservasi dan `pembatalan reservasi` di gunakan untuk membatalkan reservasi <br>
3. `Keluar` di gunakan untuk keluar dari menu<br>



<h2>Daftar Fitur per Role:</h2><br>

**Daftar Fitur Admin**<br>
Pada menu admin ada beberapa fitur seperti:
1. Manajemen User<br>
2. Manajemen Reservas<br>
0. Logout<br>


**Daftar Fitur Pengguna**<br>
Pada menu pengguna ada beberapa fitur seperti:
1. Layanan<br>
2. Reservasi<br>
3. Saldo & Pembayaran<br>
0. Logout <br>


<h2>Screenshot Output & Penjelasan:</h2>

**Screenshot Menu Utama**<br>

<img width="734" height="391" alt="image" src="https://github.com/user-attachments/assets/08a980b1-a4ad-4baf-9875-8125a025e373" />

Pada gambar di atas pada menu "Login" berfungsi untuk login di sini kita akan memasukkan nama dan password kemudian sistem akan mendeteksi, apakah yang login ini adalah user atau admin. Sedangkan pada menu "Registrasi" berfungsi untuk registrasi atau membuat akun bagi pengguna yang tidak memiliki akun.


**Screenshot Menu User**<br>
Berikut hasil screenshot dari menu user.<br>
<img width="828" height="381" alt="image" src="https://github.com/user-attachments/assets/c6555a47-1697-4f38-9094-b2fc8c072278" />


Pada gambar di bawah menampilkan menu "Layanan" yang berfungsi untuk melihat atau menampilkan layanan apa saja yang ada di petcare. <br>
<img width="548" height="413" alt="image" src="https://github.com/user-attachments/assets/bbce4c63-fbd1-4552-a1e6-81d1300617fb" />


Pada gambar di bawah menampilkan "Reservasi" user bisa melakukan reservasi atau pemesanan untuk layanan yang di inginkan.<br>

Jika memilih 'Perawatan' maka sistem akan menampilkan: <br>
<img width="616" height="383" alt="image" src="https://github.com/user-attachments/assets/7f1abfd9-5ff6-4702-9177-d2a0a946e4eb" />

Jika memilih menu "Penitipan' maka sistem akan menampilkan: <br>
<img width="566" height="382" alt="image" src="https://github.com/user-attachments/assets/f6b3755a-300e-459c-98e3-380a26e230ca" />

Pada menu "Saldo & Pembayaran" berfungsi untuk melakukan top up saldo dan melakukan pembayaran.<br>
Jika memilih top up maka akan seperti di bawah ini:<br>

<img width="657" height="420" alt="image" src="https://github.com/user-attachments/assets/7a22144d-1d60-4e57-89cd-24636bc2ed82" />

Jika memilih pembayaran atau bayar reservasi<br>

<img width="344" height="422" alt="image" src="https://github.com/user-attachments/assets/f8318fc2-50d6-4e2e-b768-d0f3d3530931" />

Pada menu "Logout" berfungsi untuk keluar dari menu.<br>

**Screenshot Menu Admin**
<img width="901" height="379" alt="image" src="https://github.com/user-attachments/assets/cddbeb0d-b796-46d3-b294-d6cb9d7de126" />


Pada menu admin terdapa tiga pilihan.<br>
Pada menu pertama yaitu "Manajemen User" berfungsi untuk melihat user dan menonaktifkan akun user yang sudah lama tidak terpakai.<br>
<img width="499" height="350" alt="image" src="https://github.com/user-attachments/assets/628e5f93-4186-472a-9d32-ad419890d53b" />

<img width="502" height="365" alt="image" src="https://github.com/user-attachments/assets/f9661437-54cc-4817-9c76-06a90856230d" />


Pada menu kedua yaitu "Manajemen Reservasi" berfungsi untuk melihat list reservasi dan membatalkan reservasi jika pelanggan tidak datang pada waktu yang telah di tentukan<br>
<img width="1099" height="385" alt="image" src="https://github.com/user-attachments/assets/3ea3b1df-b052-4d88-a6de-99b15e1e6801" />

<img width="1011" height="400" alt="image" src="https://github.com/user-attachments/assets/818472e5-7bda-4dcd-90d8-94dc1cba6947" />

Pada menu terakhir yaitu "Logout" berfungsi untuk keluar dari menu admin.<br>



