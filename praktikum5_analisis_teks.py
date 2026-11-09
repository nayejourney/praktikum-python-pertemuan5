# PRAKTIKUM 5 - KOMBINASI STRING, LIST, SET, DAN DICTIONARY
# Membaca teks dari file teks.txt dan menganalisis frekuensi kata.

import string

nama_file = "teks.txt"

try:
    with open(nama_file, "r", encoding="utf-8") as file:
        teks = file.read()

    # Membersihkan teks: huruf kecil dan tanda baca dihilangkan.
    teks_bersih = teks.lower()
    for tanda_baca in string.punctuation:
        teks_bersih = teks_bersih.replace(tanda_baca, " ")

    # Menggunakan list untuk menyimpan seluruh kata.
    daftar_kata = teks_bersih.split()

    if not daftar_kata:
        print("File tidak berisi kata yang dapat dianalisis.")
    else:
        # Menggunakan dictionary untuk menghitung frekuensi setiap kata.
        frekuensi_kata = {}
        for kata in daftar_kata:
            if kata in frekuensi_kata:
                frekuensi_kata[kata] += 1
            else:
                frekuensi_kata[kata] = 1

        # Menggunakan set untuk memperoleh kumpulan kata unik.
        kata_unik = set(daftar_kata)

        # a. Frekuensi setiap kata
        print("===== FREKUENSI SETIAP KATA =====")
        for kata, jumlah in sorted(frekuensi_kata.items()):
            print(f"{kata}: {jumlah}")

        # b. Menampilkan 10 kata paling sering muncul.
        print("\n===== 10 KATA PALING SERING MUNCUL =====")
        sepuluh_teratas = sorted(
            frekuensi_kata.items(),
            key=lambda item: item[1],
            reverse=True
        )[:10]

        for kata, jumlah in sepuluh_teratas:
            print(f"{kata}: {jumlah}")

        # c. Kata yang hanya muncul sekali (hapax legomena).
        hapax = [kata for kata, jumlah in frekuensi_kata.items() if jumlah == 1]
        print("\n===== KATA YANG HANYA MUNCUL SEKALI =====")
        print(sorted(hapax))

        # d. Type-token ratio = jumlah kata unik / jumlah seluruh kata.
        jumlah_token = len(daftar_kata)
        jumlah_type = len(kata_unik)
        ttr = jumlah_type / jumlah_token

        print("\n===== TYPE-TOKEN RATIO =====")
        print("Jumlah seluruh kata (token):", jumlah_token)
        print("Jumlah kata unik (type)    :", jumlah_type)
        print(f"Type-token ratio           : {ttr:.4f} ({ttr * 100:.2f}%)")

except FileNotFoundError:
    print(f"File '{nama_file}' tidak ditemukan.")
    print("Pastikan file teks.txt berada dalam folder yang sama dengan program.")
