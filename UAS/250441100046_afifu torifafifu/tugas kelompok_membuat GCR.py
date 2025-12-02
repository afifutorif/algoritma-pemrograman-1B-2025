database = {}
def tambah_siswa():

    while True:
        id_siswa = input("Masukkan ID siswa: ").strip()
        if id_siswa.lower() == "stop" or id_siswa == "0":
            print("Berhenti menambah siswa.")
            break

        if id_siswa in database:
            print("ID sudah ada! Gunakan ID lain.")
            continue

        nama = input("Masukkan nama siswa: ")

        nilai = []
        jumlah_mapel = int(input("Berapa mata pelajaran? "))

        for i in range(1, jumlah_mapel + 1):
            n = float(input(f"Nilai mapel {i}: "))
            nilai.append(n)

        database[id_siswa] = {
            "nama": nama,
            "nilai": nilai
        }

        print("Data siswa berhasil ditambahkan!\n")

def lihat_data():
    print("\n=== DATA SISWA ===")

    if not database:
        print("Belum ada data.")
        return

    for id_siswa, data in database.items():
        nama = data["nama"]
        nilai = data["nilai"]
        rata = sum(nilai) / len(nilai)

        print(f"\nID: {id_siswa}")
        print(f"Nama: {nama}")
        print(f"Nilai: {tuple(nilai)}")
        
        if rata >= 75:
            status = "Lulus"
        else:
            status = "Tidak Lulus"

        print(f"Rata-rata: {rata:.2f} ({status})")

def update_data():
    print("\n=== UPDATE DATA ===")
    id_siswa = input("Masukkan ID siswa: ")

    if id_siswa not in database:
        print("ID tidak ditemukan!")
        return

    print("1. Ubah Nama")
    print("2. Ubah Nilai")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        new_name = input("Nama baru: ")
        database[id_siswa]["nama"] = new_name
        print("Nama berhasil diperbarui!")

    elif pilihan == "2":
        nilai_baru = []
        jml = int(input("Jumlah mata pelajaran: "))
        for i in range(1, jml + 1):
            n = float(input(f"Nilai baru mapel {i}: "))
            nilai_baru.append(n)
        database[id_siswa]["nilai"] = nilai_baru
        print("Nilai berhasil diperbarui!")

    else:
        print("Pilihan tidak valid!")

def hapus_data():
    print("\n=== HAPUS DATA ===")
    id_siswa = input("Masukkan ID siswa: ")

    if id_siswa in database:
        del database[id_siswa]
        print("Data berhasil dihapus!")
    else:
        print("ID tidak ditemukan!")

while True:
    print("\n===== MENU SISTEM PENDIDIKAN GCR =====")
    print("1. Tambah Siswa")
    print("2. Lihat Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        tambah_siswa()
    elif menu == "2":
        lihat_data()
    elif menu == "3":
        update_data()
    elif menu == "4":
        hapus_data()
    elif menu == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")