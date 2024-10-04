#Nama : Fikri  Abdilah
#Jurusan : Sains Data
print ("Selamat datang di Pengecekan jumlah hari")
print ("Dengan Memasukkan Bulan nya ya")
def jumlah_hari(bulan):
    # Daftar jumlah hari dalam setiap bulan pada tahun 2020 (tahun kabisat)
    hari_per_bulan = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    } #Menggunakan dictionary
    
    # Cek apakah bulan valid
    if bulan in hari_per_bulan:
        return f"Jumlah hari: {hari_per_bulan[bulan]}"
    else:
        return "Bulan tidak valid. Silakan masukkan angka antara 1 dan 12."

try:
    # Meminta input dari pengguna
    bulan = int(input("Masukkan bulan (1-12): "))
    # Menampilkan jumlah hari
    print(jumlah_hari(bulan))
except ValueError:
    print("Input tidak valid. Silakan masukkan angka antara 1 dan 12.")
