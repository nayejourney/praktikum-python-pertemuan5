# PRAKTIKUM 3 - SET
# Membandingkan penerima Beasiswa A dan Beasiswa B menggunakan operasi himpunan.

input_a = input("Masukkan ID penerima Beasiswa A (pisahkan dengan koma): ")
input_b = input("Masukkan ID penerima Beasiswa B (pisahkan dengan koma): ")

# Mengubah input menjadi set agar setiap ID bersifat unik.
beasiswa_a = {id_mhs.strip() for id_mhs in input_a.split(",") if id_mhs.strip()}
beasiswa_b = {id_mhs.strip() for id_mhs in input_b.split(",") if id_mhs.strip()}

# a. Mahasiswa yang menerima kedua beasiswa (irisan / intersection)
kedua_beasiswa = beasiswa_a & beasiswa_b

# b. Mahasiswa yang hanya menerima Beasiswa A (difference)
hanya_a = beasiswa_a - beasiswa_b

# c. Mahasiswa yang menerima Beasiswa B tetapi tidak A
hanya_b = beasiswa_b - beasiswa_a

# d. Semua mahasiswa unik penerima beasiswa (gabungan / union)
semua_penerima = beasiswa_a | beasiswa_b

print("\n===== HASIL OPERASI SET =====")
print("Penerima Beasiswa A              :", sorted(beasiswa_a))
print("Penerima Beasiswa B              :", sorted(beasiswa_b))
print("Menerima kedua beasiswa          :", sorted(kedua_beasiswa))
print("Hanya menerima Beasiswa A        :", sorted(hanya_a))
print("Beasiswa B tetapi tidak A        :", sorted(hanya_b))
print("Semua penerima unik              :", sorted(semua_penerima))
