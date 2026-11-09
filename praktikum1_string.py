# PRAKTIKUM 1 - STRING
# Menerima kalimat dan mengolah data teks.

kalimat = input("Masukkan sebuah kalimat: ")

# a. Menghitung jumlah kata
kata = kalimat.split()
jumlah_kata = len(kata)

# b. Menghitung jumlah karakter (termasuk spasi dan tanda baca)
jumlah_karakter = len(kalimat)

# c. Menampilkan kata terpanjang
if kata:
    kata_terpanjang = max(kata, key=len)
else:
    kata_terpanjang = "(tidak ada kata)"

# d. Menampilkan kalimat dalam bentuk title case
kalimat_title = kalimat.title()

print("\n===== HASIL PENGOLAHAN STRING =====")
print("Kalimat             :", kalimat)
print("Jumlah kata         :", jumlah_kata)
print("Jumlah karakter     :", jumlah_karakter)
print("Kata terpanjang     :", kata_terpanjang)
print("Title case          :", kalimat_title)
