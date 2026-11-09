# PRAKTIKUM 2 - LIST DAN DICTIONARY
# Mengolah nilai mahasiswa, menentukan kategori, dan menghitung frekuensinya.

input_nilai = input(
    "Masukkan nilai mahasiswa, pisahkan dengan koma (contoh: 90,80,75,60): "
)

try:
    nilai_mahasiswa = [float(nilai.strip()) for nilai in input_nilai.split(",") if nilai.strip()]

    if not nilai_mahasiswa:
        print("Belum ada nilai yang dimasukkan.")
    else:
        # a. Menghitung rata-rata
        rata_rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa)

        # b. Menentukan nilai tertinggi dan terendah
        nilai_tertinggi = max(nilai_mahasiswa)
        nilai_terendah = min(nilai_mahasiswa)

        # c dan d. Mengelompokkan nilai serta menghitung frekuensi kategori
        frekuensi = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
        hasil_kategori = []

        for nilai in nilai_mahasiswa:
            if nilai >= 85:
                kategori = "A"
            elif nilai >= 70:
                kategori = "B"
            elif nilai >= 55:
                kategori = "C"
            elif nilai >= 40:
                kategori = "D"
            else:
                kategori = "E"

            hasil_kategori.append(kategori)
            frekuensi[kategori] += 1

        print("\n===== HASIL PENGOLAHAN NILAI =====")
        print("Daftar nilai       :", nilai_mahasiswa)
        print(f"Rata-rata          : {rata_rata:.2f}")
        print("Nilai tertinggi    :", nilai_tertinggi)
        print("Nilai terendah     :", nilai_terendah)
        print("Kategori tiap nilai:", hasil_kategori)

        print("\nFrekuensi kategori:")
        for kategori, jumlah in frekuensi.items():
            print(f"Kategori {kategori}: {jumlah} mahasiswa")

except ValueError:
    print("Input tidak valid. Masukkan angka dan pisahkan setiap nilai dengan koma.")
