def cek_sisi(sisi1, sisi2, sisi3):
    # Cek apakah ketiga sisi sama
    if sisi1 == sisi2 == sisi3:
        return "3 sisi sama"
    # Cek apakah ada dua sisi yang sama
    elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
        return "2 sisi sama"
    # Jika tidak ada sisi yang sama
    else:
        return "Tidak ada yang sama"

try:
    # Meminta input dari pengguna dan mengonversinya menjadi float
    sisi1 = float(input("Masukkan sisi 1: "))
    sisi2 = float(input("Masukkan sisi 2: "))
    sisi3 = float(input("Masukkan sisi 3: "))

    # Menampilkan hasil pengecekan
    print(cek_sisi(sisi1, sisi2, sisi3))

except ValueError:
    # Menangani kesalahan input yang tidak valid
    print("Input tidak valid. Silakan masukkan angka yang benar.")
