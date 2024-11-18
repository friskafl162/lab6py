## Program Pengelolaan Data Mahasiswa
Program input nilai mahasiswa ini merupakan program berbasis teks untuk mengelola data mahasiswa. program ini memungkinkan pengguna untuk :
1. *Melihat Data* :
    - menampilkan seluruh data mahasiswa dalam format tabel
2. *Menambah Data* :
    - Memasukkan data baru (NIM, nama, nilai tugas, UTS, UAS), menghitung nilai akhir, dan menyimpannya
3. *Mengubah Data* :
    - Mengedit data mahasiswa berdasarkan NIM yang sudah ada.
4. *Menghapus Data* :
    - Menghapus data mahasiswa berdasarkan NIM.
6. *Mencari Data8 :
    - menemukan data mahasiswa tertentu berdasarkan NIM.

## Deskripsi Program
## Deskripsi Program Input Nilai Mahasiswa

Program ini dirancang untuk mengelola data nilai mahasiswa secara sederhana. Program ini memungkinkan pengguna untuk:

* Menambahkan data mahasiswa baru: Pengguna dapat memasukkan NIM, nama, nilai tugas, UTS, dan UAS. Program akan menghitung nilai akhir secara otomatis berdasarkan bobot yang telah ditentukan.
* Melihat daftar nilai: Program akan menampilkan semua data mahasiswa yang sudah tersimpan dalam format tabel yang mudah dibaca.
* Mengubah data mahasiswa: Pengguna dapat mengubah data mahasiswa yang sudah ada berdasarkan NIM.
* Menghapus data mahasiswa: Pengguna dapat menghapus data mahasiswa yang sudah tidak diperlukan.
* Mencari data mahasiswa: Pengguna dapat mencari data mahasiswa berdasarkan NIM.

## flowchart Program
!/(Flowchart)[flowchartlab6.png] 

## Kode Program
``` python
# Program Input Nilai Mahasiswa
data_mahasiswa = {}

def tampilkan_menu():
    print("\nProgram Input Nilai")
    print("=" * 50)
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]")
    pilihan = input("Pilih menu: ").lower()
    return pilihan

def tampilkan_data():
    print("\nDaftar Nilai")
    print("=" * 65)
    print("| NO |   NIM   |      NAMA      | TUGAS | UTS | UAS | AKHIR |")
    print("=" * 65)
    if not data_mahasiswa:
        print("|                       TIDAK ADA DATA                         |")
    else:
        for i, (nim, data) in enumerate(data_mahasiswa.items(), start=1):
            print(f"| {i:<2} | {nim:<7} | {data['nama']:<14} | {data['tugas']:<5} | {data['uts']:<3} | {data['uas']:<3} | {data['akhir']:<5.2f} |")
    print("=" * 65)
def tambah_data():
    nim = input("NIM: ")
    if nim in data_mahasiswa:
        print("NIM sudah ada. Gunakan opsi ubah data untuk mengganti.")
        return
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": nilai_akhir}
    print("Data berhasil ditambahkan.")

def ubah_data():
    nim = input("Masukkan NIM yang ingin diubah: ")
    if nim not in data_mahasiswa:
        print("NIM tidak ditemukan.")
        return
    print(f"Data saat ini: {data_mahasiswa[nim]}")
    nama = input("Masukkan Nama baru: ")
    tugas = float(input("Masukkan Nilai Tugas baru: "))
    uts = float(input("Masukkan Nilai UTS baru: "))
    uas = float(input("Masukkan Nilai UAS baru: "))
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": nilai_akhir}
print("Data berhasil diubah.")
def hapus_data():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus.")
    else:
        print("NIM tidak ditemukan.")

def cari_data():
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in data_mahasiswa:
        data = data_mahasiswa[nim]
        print("\nData ditemukan:")
        print(f"NIM   : {nim}")
        print(f"Nama  : {data['nama']}")
        print(f"Tugas : {data['tugas']}")
        print(f"UTS   : {data['uts']}")
        print(f"UAS   : {data['uas']}")
        print(f"Akhir : {data['akhir']:.2f}")
    else:
        print("NIM tidak ditemukan.")
while True:
    pilihan = tampilkan_menu()
    if pilihan == "l":
        tampilkan_data()
    elif pilihan == "t":
        tambah_data()
    elif pilihan == "u":
        ubah_data()
    elif pilihan == "h":
        hapus_data()
    elif pilihan == "c":
        cari_data()
    elif pilihan == "k":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
```

## Output Program
```
PS C:\Users\user\Documents\Kuliah> & C:/Users/user/AppData/Local/Programs/Python/Python312/python.exe c:/Users/user/Documents/Kuliah/lab2py/pemrograman/lab6.py
Data berhasil diubah.

Program Input Nilai
==================================================
[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]
Pilih menu: L   

Daftar Nilai
=================================================================
| NO |   NIM   |      NAMA      | TUGAS | UTS | UAS | AKHIR |
=================================================================
|                       TIDAK ADA DATA                         |
=================================================================

Program Input Nilai
==================================================
[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]
Pilih menu: T
NIM: 312410160
Nama: Friska Pebriana Lestari
Nilai Tugas: 95
Nilai UTS: 96
Nilai UAS: 98
Data berhasil ditambahkan.

Program Input Nilai
==================================================
[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]
Pilih menu: L

Daftar Nilai
=================================================================
| NO |   NIM   |      NAMA      | TUGAS | UTS | UAS | AKHIR |
=================================================================
| 1  | 312410160 | Friska Pebriana Lestari | 95.0  | 96.0 | 98.0 | 96.40 |
=================================================================

Program Input Nilai
==================================================
[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]
Pilih menu: K
Keluar dari program.
PS C:\Users\user\Documents\Kuliah>
```

## Cara Kerja Program
1. *Menu Utama* : Program menyediakan menu utama degan pilihan berikut :
   - Lihat (L) : menampilkan semua data mahasiswa dalam format tabel
   - Tambah (T) : Menambahkan data mahasiswa baru (NIM, nama, nilai tugas, UTS, UAS).
   - Ubah (U) : Mengubah data mahasiswa yang sudah ada berdasarkan NIM.
   - Hapus (H) : Menghapus data mahasiswa berdasarkan NIM.
   - Cari (C) : Mencari Data mahasiswa tertentu berdasarkan NIM.
   - Keluar (K) : mengakhiri Program.
2. *Penyimpanan Data* : Data disimpan dalam dictionary data_mahasiswa, dengan format :
``` python
data_mahasiswa = {
    "NIM1": {"nama": "Nama Mahasiswa", "tugas": 80, "uts": 85, "uas": 90, "akhir": 85.5},
    ...
}
```
Dimana Akhir dihitung dengan rumus :
   ``` python
   nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
```
3. Proses Utama
   - *Menampilkan Data* (Lihat): Menampilkan semua data mahasiswa dalam format tabel. jika tidak ada data, tampilkan pean "Tidak ada data"
   - *Menambah data* \(Tambah) : Meminta input dari pengguna
       - NIM, nama, nilai tugaa=s, UTS, UAS.
       - Menghitung nilai akhir dan menyimpannya ke dalam dictionary.
   - *Mengubah Data* (Ubah) :
       - Mencari data mahasiswa berdasarkan NIM.
       - Jika ditemukan, meminta pengguna memasukkan data bary untuk mengganti data lama.
       - Menghitung ulang nilai akhir.
   - *Menghapus data* (Hapus) : Menghapus data mahasiswa tertentu berdasarkan NIM.
   - *Keluar program* : Program berhenti saat pengguna memilih menu Keluar (K)
