def ganjil(bawah, atas):
    if bawah < atas:
        deret = [i for i in range(bawah, atas+1) if i % 2 != 0]
    else:
        deret = [i for i in range(bawah, atas-1, -1) if i % 2 != 0]
    return deret

# Contoh penggunaan
bawah = int(input("Masukkan nilai bawah: "))
atas = int(input("Masukkan nilai atas: "))
hasil = ganjil(bawah, atas)
print(hasil)

bawah = int(input("Masukkan nilai bawah: "))
atas = int(input("Masukkan nilai atas: "))
hasil = ganjil(bawah, atas)
print(hasil)
