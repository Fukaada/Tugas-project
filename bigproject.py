import os

# Fungsi untuk membersihkan terminal
def clear_terminal():
    if os.name == 'nt':  # Jika Windows
        os.system('cls')
    else:  # Jika Linux/Mac
        os.system('clear')

# Fungsi untuk menampilkan menu utama
def tampilkan_menu():
    print("========= Menu Utama =========")
    for nomor, menu in daftar_menu.items():
        print(f"{nomor}. {menu['nama']}")
    print("0. Keluar")

# FUngsi untuk melihat stock barang digudang
def lihat_stok_barang():
    print("=== Stok Barang Tersedia ===")
    if stok_barang:
        for barang, stok in stok_barang.items():
            print(f"{barang}: {stok} tersisa")
    else:
        print("Stok barang kosong.")
    input("\nTekan Enter untuk kembali ke menu utama...")

def edit_stok_barang():
    while True:
        print("\n=== Edit Stok Barang ===")
        print("1. Tambah barang baru")
        print("2. Update stok barang")
        print("3. Kembali ke menu utama")
        
        try:
            pilihan = int(input("Pilih opsi (1/2/3): "))
            if pilihan == 1:
                # Tambah barang baru
                nama_barang_baru = input("Masukkan nama barang baru: ").capitalize()
                if nama_barang_baru in stok_barang:
                    print(f"{nama_barang_baru} sudah ada dalam stok. Gunakan opsi update stok.")
                else:
                    try:
                        jumlah_stok_baru = int(input(f"Masukkan jumlah stok untuk {nama_barang_baru}: "))
                        stok_barang[nama_barang_baru] = jumlah_stok_baru
                        print(f"{nama_barang_baru} berhasil ditambahkan dengan stok {jumlah_stok_baru}.")
                    except ValueError:
                        print("Jumlah stok harus berupa angka.")
                
            elif pilihan == 2:
                # Update stok barang yang sudah ada
                nama_barang = input("Masukkan nama barang yang ingin diupdate: ").capitalize()
                if nama_barang in stok_barang:
                    try:
                        jumlah_stok = int(input(f"Masukkan jumlah stok baru untuk {nama_barang} (stok saat ini: {stok_barang[nama_barang]}): "))
                        stok_barang[nama_barang] = jumlah_stok
                        print(f"Stok {nama_barang} berhasil diperbarui menjadi {jumlah_stok}.")
                    except ValueError:
                        print("Jumlah stok harus berupa angka.")
                else:
                    print(f"{nama_barang} tidak ditemukan di dalam stok.")
            
            elif pilihan == 3:
                # Kembali ke menu utama
                break
            else:
                print("Opsi tidak valid. Silakan pilih 1, 2, atau 3.")
        
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
        input("Tekan Enter untuk melanjutkan...")


# Fungsi untuk menghitung total belanja
def hitung_belanja():
    total = 0
    while True:
        try:
            harga = float(input("Masukkan harga barang (ketik 0 untuk selesai): "))
            if harga == 0:
                break
            total += harga
        except ValueError:
            print("Input tidak valid, masukkan angka.")
    print(f"Total belanja: Rp {total:.2f}")

# Fungsi untuk top-up saldo
def topup_saldo():
    try:
        jumlah = float(input("Masukkan jumlah saldo yang ingin di-top-up: "))
        print(f"Saldo sebesar Rp {jumlah:.2f} telah berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid, masukkan angka.")

# Fungsi untuk membayar BPJS
def bayar_bpjs():
    try:
        jumlah_tagihan = float(input("Masukkan jumlah tagihan BPJS: "))
        print(f"Pembayaran BPJS sebesar Rp {jumlah_tagihan:.2f} berhasil.")
    except ValueError:
        print("Input tidak valid, masukkan angka.")
# Dictionary yang menyimpan stock barang 
stok_barang = {
    'Beras': 50,
    'Gula': 30,
    'Minyak Goreng': 20,
    'Telur': 100,
    'Sabun': 40
}


# Dictionary yang menyimpan daftar menu dan fungsinya
daftar_menu = {
    1: {'nama': 'Top-up Saldo', 'fungsi': topup_saldo},
    2: {'nama': 'Hitung Belanja', 'fungsi': hitung_belanja},
    3: {'nama': 'Bayar BPJS', 'fungsi': bayar_bpjs},
    4: {'nama': 'Lihat Stok Barang', 'fungsi': lihat_stok_barang} 
}
daftar_menu[5] = {'nama': 'Edit Stok Barang', 'fungsi': edit_stok_barang}


# Program utama
while True:
    clear_terminal()
    tampilkan_menu()
    
    try:
        pilihan = int(input("Pilih menu (masukkan angka): "))
        if pilihan == 0:
            print("Terima kasih telah menggunakan program kasir.")
            break
        elif pilihan in daftar_menu:
            daftar_menu[pilihan]['fungsi']()

        else:
            print("Menu tidak valid. Silakan pilih kembali.")
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")
    
    input("Tekan Enter untuk kembali ke menu utama...")
