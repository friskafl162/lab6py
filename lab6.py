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