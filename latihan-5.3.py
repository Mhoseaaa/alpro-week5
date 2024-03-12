def hitung_ips(jumlah_matkul):
    total_sks = jumlah_matkul * 3
    total_bobot = 0

    for i in range(1, jumlah_matkul + 1):
        nilai = input(f"Masukkan nilai untuk mata kuliah ke-{i} (A/B/C/D): ").upper()

        # Menghitung bobot berdasarkan nilai
        if nilai == 'A':
            bobot = 4
        elif nilai == 'B':
            bobot = 3
        elif nilai == 'C':
            bobot = 2
        elif nilai == 'D':
            bobot = 1
        else:
            print("Nilai tidak valid. Silakan masukkan nilai A, B, C, atau D.")
            return None

        # Menambah total bobot nilai
        total_bobot += bobot * 3  # setiap mata kuliah memiliki 3 SKS

    # Menghitung IPS
    ips = total_bobot / total_sks
    return ips

def main():
    # Input jumlah mata kuliah
    while True:
        try:
            jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
            if jumlah_matkul > 0:
                break
            else:
                print("Jumlah mata kuliah harus lebih dari 0.")
        except ValueError:
            print("Masukkan angka yang valid untuk jumlah mata kuliah.")

    # Hitung IPS
    ips = hitung_ips(jumlah_matkul)
    if ips is not None:
        print(f"Indeks Prestasi Semester (IPS) Anda adalah: {ips:.2f}")

if __name__ == "__main__":
    main()
