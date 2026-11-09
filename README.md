# Praktikum Python - Pertemuan 5

Paket ini berisi penyelesaian seluruh **Soal Praktik** pada Modul Bahan Ajar Pemrograman Python Pertemuan 5: String, List, Tuple, Set, dan Dictionary.

## Daftar file

1. `praktikum1_string.py` — menghitung kata dan karakter, mencari kata terpanjang, serta mengubah kalimat ke title case.
2. `praktikum2_list_dictionary.py` — menghitung rata-rata, nilai tertinggi/terendah, kategori nilai A-E, dan frekuensi kategori.
3. `praktikum3_set.py` — operasi irisan, selisih, dan gabungan data penerima beasiswa.
4. `praktikum4_dictionary.py` — inventaris toko menggunakan dictionary dengan tuple `(harga, stok)` serta fungsi pengelolaan.
5. `praktikum5_analisis_teks.py` — membaca `teks.txt`, menghitung frekuensi kata, 10 kata teratas, hapax legomena, dan type-token ratio.

## Cara menjalankan

Buka folder ini di VS Code. Jalankan setiap program melalui terminal:

```bash
python praktikum1_string.py
python praktikum2_list_dictionary.py
python praktikum3_set.py
python praktikum4_dictionary.py
python praktikum5_analisis_teks.py
```

Untuk Praktikum 5, biarkan `teks.txt` berada di folder yang sama dengan file Python. Isi `teks.txt` dapat diganti dengan teks lain untuk pengujian.

## Ketentuan kategori nilai

Mengikuti contoh pengelompokan nilai pada modul:
- A: nilai >= 85
- B: nilai >= 70
- C: nilai >= 55
- D: nilai >= 40
- E: nilai < 40

## Catatan pengujian

- Praktikum 1 menghitung karakter menggunakan `len(kalimat)`, sehingga spasi dan tanda baca ikut dihitung.
- Praktikum 4 menghitung total nilai inventaris dengan rumus `harga * stok` untuk setiap barang.
- Praktikum 5 mengubah huruf menjadi lowercase dan menghapus tanda baca sebelum menghitung kata. Type-token ratio dihitung sebagai jumlah kata unik dibagi jumlah seluruh kata.
