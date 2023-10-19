# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:00:57 2023

@author: Huawei
"""

print("=====SELAMAT DATANG DI KEBUN BINATANG TRISAKTI=====")

harga_gratis = 0
harga_anak = 14
harga_lansia = 18
harga_normal = 23

total_pembayaran = 0
harga = harga_gratis, harga_anak, harga_lansia, harga_normal
while True:
    umur = input("masukkan umur : ")
    if umur == '':
        break

    try:
        umur = int(umur)
    except ValueError:
        print("Masukkan umur dalam bentuk angka.")
        continue

    if umur <= 2:
        total_pembayaran += harga_gratis
        print("Gratis")
        print(f"Running total : ${total_pembayaran:.2f}")
    elif 3 <= umur <= 12:
        total_pembayaran += harga_anak
        print("Harga $", harga_anak)
        print(f"Running total : ${total_pembayaran:.2f}")
    elif umur >= 65:
        total_pembayaran += harga_lansia
        print("Harga $", harga_lansia)
        print(f"Running total : ${total_pembayaran:.2f}")
    else:
        total_pembayaran += harga_normal
        print("Harga $", harga_normal)
        print(f"Running total : ${total_pembayaran:.2f}")


while True:
    pembayaran = input("masukkan jumlah uang : ")
    try:
        pembayaran = float(pembayaran)
        if pembayaran >= total_pembayaran:
            kembalian = pembayaran - total_pembayaran
            print(f"Running Kembalian: ${kembalian:.2f}")
            print("=====TERIMAKASIH=====")
            break
        else:
            print("Jumlah uang yang dibayarkan kurang dari total pembayaran.")
    except ValueError:
        print("Masukkan jumlah uang dalam bentuk angka.")
