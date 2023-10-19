# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:08:08 2023

@author: Huawei
"""

nilai = {
    'A': 4.00,
    'A-': 3.75,
    'B+': 3.50,
    'B': 3.00,
    'B-': 2.75,
    'C+': 2.50,
    'C': 2.00,
    'C-': 1.75,
    'D': 1.50,
    'E': 1.25
}

total_nilai = 0
jumlah_kategori = 0

while True:
    kategori_huruf = input("Masukkan Nilai : ").upper()

    if kategori_huruf == '':
        break

    if kategori_huruf in nilai:
        nilai_kategori = nilai[kategori_huruf]
        total_nilai += nilai_kategori
        jumlah_kategori += 1
        print("nilai :", nilai_kategori)
    else:
        print(f"Kategori huruf '{kategori_huruf}' tidak valid dan akan diabaikan.")

if jumlah_kategori > 0:
    rata_rata = total_nilai / jumlah_kategori
    print(f"rata - ratanya adalah: {rata_rata:.2f}")
else:
    print("Tidak ada kategori huruf yang valid untuk dihitung rata-ratanya.")