import os


def reset_terminal(): # Fungsi reset Terminal
    if os.name == 'nt':
        os.system('cls')
    else :
        os.system('clear')

#Pengecekan sisi dengan memanggil fungsi def
def cek_sisi(sisi1, sisi2, sisi3):
    while True:
        # Cek apakah ketiga sisi sama
        if  sisi1 == 0 or sisi2 == 0 or sisi3 == 0:
            print("Terimakasih Telah melakukan pengecekan sisi")
            break
        # Cek apakah ada dua sisi yang sama
        elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3 :
            print ("2 sisi sama")
        # Jika tidak ada sisi yang sama
        elif sisi1 == sisi2 == sisi3 and sisi1 :
            print ("3 sisi sama") 
        else:
            print ("Tidak ada yang sama")

try:
        # Meminta input dari pengguna dan mengonversinya menjadi float
        print ("Selamat datang di pengecekan Sisi")
        print ("====Silahkan masukan Sisi====")
        print ("Tekan tulis angka '0' disetiap sisi untuk keluar program")
        sisi1 = float(input("Masukkan sisi 1: "))
        sisi2 = float(input("Masukkan sisi 2: "))
        sisi3 = float(input("Masukkan sisi 3: "))

        # Menampilkan hasil pengecekan
        print(cek_sisi(sisi1, sisi2, sisi3))

except ValueError:
    # Menangani kesalahan input yang tidak valid
    print("Input tidak valid. Silakan masukkan angka yang benar.")

