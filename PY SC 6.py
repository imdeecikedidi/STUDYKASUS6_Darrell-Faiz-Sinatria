import json
from pathlib import Path

file_nilai = Path(__file__).parent / "JSON SC 6.json"

try:
    with open(file_nilai, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

while True:
    print("\n1. Lihat nilai\n2. Tambah nilai\n3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        if not data:
            print("Belum ada data.")
        for m in data:
            print(f"{m['nim']} | {m['nama']} | "
                f"{m['mata_kuliah']} | {m['nilai']}")

    elif pilihan == "2":
        nim = input("NIM: ").strip()
        nama = input("Nama: ").strip()
        matkul = input("Mata kuliah: ").strip()

        if not nim or not nama or not matkul:
            print("Semua identitas wajib diisi.")
            continue

        try:
            nilai = float(input("Nilai (0–100): "))
            if not 0 <= nilai <= 100:
                print("Nilai harus 0–100.")
                continue
        except ValueError:
            print("Nilai harus angka.")
            continue

        data.append({
            "nim": nim,
            "nama": nama,
            "mata_kuliah": matkul,
            "nilai": nilai
        })

        with open(file_nilai, "w") as file:
            json.dump(data, file, indent=4)
        print("Data berhasil disimpan.")

    elif pilihan == "3":
        break

    else:
        print("Pilihan tidak valid.")