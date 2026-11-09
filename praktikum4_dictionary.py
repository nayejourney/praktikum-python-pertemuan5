# PRAKTIKUM 4 - DICTIONARY DAN TUPLE
# Nama barang menjadi key, sedangkan (harga, stok) menjadi value berbentuk tuple.

inventaris = {
    "Buku": (15000, 20),
    "Pulpen": (5000, 50),
    "Pensil": (3000, 40)
}


def tambah_barang(nama, harga, stok):
    """Menambahkan barang baru ke inventaris."""
    if nama in inventaris:
        print("Barang sudah ada. Gunakan fitur update stok jika ingin mengubah stok.")
    elif harga < 0 or stok < 0:
        print("Harga dan stok tidak boleh bernilai negatif.")
    else:
        inventaris[nama] = (harga, stok)
        print(f"Barang '{nama}' berhasil ditambahkan.")


def update_stok(nama, stok_baru):
    """Mengubah stok barang yang sudah terdaftar."""
    if nama not in inventaris:
        print("Barang tidak ditemukan.")
    elif stok_baru < 0:
        print("Stok tidak boleh bernilai negatif.")
    else:
        harga_lama, stok_lama = inventaris[nama]
        inventaris[nama] = (harga_lama, stok_baru)
        print(f"Stok '{nama}' berhasil diperbarui dari {stok_lama} menjadi {stok_baru}.")


def cari_barang_rentang_harga(harga_min, harga_maks):
    """Menampilkan barang dengan harga di dalam rentang yang ditentukan."""
    print(f"\nBarang dengan harga Rp{harga_min:,.0f} - Rp{harga_maks:,.0f}:")
    ditemukan = False

    for nama, (harga, stok) in inventaris.items():
        if harga_min <= harga <= harga_maks:
            print(f"- {nama}: harga Rp{harga:,.0f}, stok {stok}")
            ditemukan = True

    if not ditemukan:
        print("Tidak ada barang dalam rentang harga tersebut.")


def hitung_total_nilai_inventaris():
    """Menghitung total nilai seluruh stok barang (harga dikali stok)."""
    total = 0
    for harga, stok in inventaris.values():
        total += harga * stok
    return total


def tampilkan_inventaris():
    print("\n===== DAFTAR INVENTARIS =====")
    if not inventaris:
        print("Inventaris masih kosong.")
    else:
        for nama, (harga, stok) in inventaris.items():
            print(f"{nama}: harga Rp{harga:,.0f}, stok {stok}")


while True:
    print("\n===== MENU INVENTARIS TOKO =====")
    print("1. Tampilkan inventaris")
    print("2. Tambah barang baru")
    print("3. Update stok barang")
    print("4. Cari barang berdasarkan rentang harga")
    print("5. Hitung total nilai inventaris")
    print("0. Keluar")

    pilihan = input("Pilih menu: ").strip()

    if pilihan == "1":
        tampilkan_inventaris()

    elif pilihan == "2":
        nama = input("Nama barang: ").strip()
        try:
            harga = int(input("Harga barang: "))
            stok = int(input("Jumlah stok: "))
            tambah_barang(nama, harga, stok)
        except ValueError:
            print("Harga dan stok harus berupa bilangan bulat.")

    elif pilihan == "3":
        nama = input("Nama barang yang akan diupdate: ").strip()
        try:
            stok_baru = int(input("Masukkan stok terbaru: "))
            update_stok(nama, stok_baru)
        except ValueError:
            print("Stok harus berupa bilangan bulat.")

    elif pilihan == "4":
        try:
            harga_min = int(input("Harga minimum: "))
            harga_maks = int(input("Harga maksimum: "))
            if harga_min > harga_maks:
                print("Harga minimum tidak boleh lebih besar dari harga maksimum.")
            else:
                cari_barang_rentang_harga(harga_min, harga_maks)
        except ValueError:
            print("Rentang harga harus berupa bilangan bulat.")

    elif pilihan == "5":
        total = hitung_total_nilai_inventaris()
        print(f"Total nilai inventaris: Rp{total:,.0f}")

    elif pilihan == "0":
        print("Program inventaris selesai. Terima kasih.")
        break

    else:
        print("Pilihan tidak tersedia. Silakan pilih menu yang benar.")
