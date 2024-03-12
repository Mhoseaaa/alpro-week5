def perkalian(a, b):
    hasil = 0
    for _ in range(b):
        hasil += a
    return hasil

def main():
    while True:
        try:
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))
            hasil_perkalian = perkalian(angka1, angka2)
            print(f"{angka1}x{angka2} =", end="")
            for _ in range(angka2):
                if _ != angka2 - 1:
                    print(f"{angka1}+", end="")
                else:
                    print(f"{angka1}=", end="")
            print(hasil_perkalian)
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan bilangan bulat.")

if __name__ == "__main__":
    main()
