import os
import random

def reset_terminal():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')

def main_tebakan():
    while True:
        reset_terminal()
        print("      Selamat Datang di Game Tebakan Matematika")
        print("==================creadit by fukada=======================")
        nama = input('Masukan Username kamu: ')
        try : 
                print (f'Oke {nama} Sekarang Pilih Level : ')
                print('Pilih Level =')
                print('Level 1 (EZZ MODE)')
                print('Level 2 (MEDIUM MODE)')
                print('Level 3 (HARD MODE)')
                print('Level 4 (IMPOSIBLE MODE :(')
                print('Level 5 (GODDES MODE :)')
                level = input("Masukan Level 1/2/3/4/5 =...")
                if level == 1:
                    level1()
                elif level == 2:
                    level2()
                elif level == 3:
                    level3()
                elif level == 4:
                    level4()
                elif level == 5:
                    level5()
                else :
                    print('Pilih Level dari 1-5 aja ya')
                

        except ValueError:
            print ('Masukan Angka Bukan Huruf :]')
            continue

def level1():
    while True:
        angka1 = random.randint(1, 500)
        angka2 = random.randint(1, 500)
        simbol = ['+', '-', '/', '*']
        random_simbol = random.choice(simbol)
        hasil = eval(f'{angka1} {random_simbol} {angka2}')
        try :
            print("Selamat Datang di Game Tebakan Matematika")
            print('===============LV 1=======================')
            print(f'Oke, sekarang kita mulai tebak-tebakan matematika!')
            print(f'Berapakah hasil dari {angka1} {random_simbol} {angka2}?')
            
            jawaban = int(input("Masukan jawaban: "))

            if jawaban == hasil:
                print(f'Yeay! Kamu benar, jawabannya {hasil}. Lanjut? Y/N')
                pilihan = input().lower()
                if pilihan == 'n':
                    return  
                elif pilihan == 'y':
                    continue  
            else:
                print(f"Jawaban kamu salah, yang benar adalah {hasil}.")
                pilihan = input("Tekan Enter untuk mengulang, atau ketik 'NYERAH'...").lower()
                if pilihan == "nyerah":
                    return  
                else:
                    continue  
        except ValueError:
            print("Masukkan angka yang benar ya....")
            input("Tekan Enter untuk melanjutkan...")
def level2():
    while True:
        angka1 = random.randint(1, 500)
        angka2 = random.randint(1, 500)
        simbol = ['+', '-', '/', '*']
        random_simbol = random.choice(simbol)
        hasil = eval(f'{angka1} {random_simbol} {angka2}')
        try :
            print("Selamat Datang di Game Tebakan Matematika")
            print('===============LV 2=======================')
            print(f'Oke, sekarang kita mulai tebak-tebakan matematika!')
            print(f'Berapakah hasil dari {angka1} {random_simbol} {angka2}?')
            
            jawaban = int(input("Masukan jawaban: "))

            if jawaban == hasil:
                print(f'Yeay! Kamu benar, jawabannya {hasil}. Lanjut? Y/N')
                pilihan = input().lower()
                if pilihan == 'n':
                    return  
                elif pilihan == 'y':
                    continue  
            else:
                print(f"Jawaban kamu salah, yang benar adalah {hasil}.")
                pilihan = input("Tekan Enter untuk mengulang, atau ketik 'NYERAH'...").lower()
                if pilihan == "nyerah":
                    return  
                else:
                    continue  
        except ValueError:
            print("Masukkan angka yang benar ya....")
            input("Tekan Enter untuk melanjutkan...")
def level3():
    while True:
        angka1 = random.randint(1, 500)
        angka2 = random.randint(1, 500)
        simbol = ['+', '-', '/', '*']
        random_simbol = random.choice(simbol)
        hasil = eval(f'{angka1} {random_simbol} {angka2}')
        try :
            print("Selamat Datang di Game Tebakan Matematika")
            print('===============LV 5=======================')
            print(f'Oke, sekarang kita mulai tebak-tebakan matematika!')
            print(f'Berapakah hasil dari {angka1} {random_simbol} {angka2}?')
            
            jawaban = int(input("Masukan jawaban: "))

            if jawaban == hasil:
                print(f'Yeay! Kamu benar, jawabannya {hasil}. Lanjut? Y/N')
                pilihan = input().lower()
                if pilihan == 'n':
                    return  
                elif pilihan == 'y':
                    continue  
            else:
                print(f"Jawaban kamu salah, yang benar adalah {hasil}.")
                pilihan = input("Tekan Enter untuk mengulang, atau ketik 'NYERAH'...").lower()
                if pilihan == "nyerah":
                    return  
                else:
                    continue  
        except ValueError:
            print("Masukkan angka yang benar ya....")
            input("Tekan Enter untuk melanjutkan...")
def level4():
    while True:
        angka1 = random.randint(1, 500)
        angka2 = random.randint(1, 500)
        simbol = ['+', '-', '/', '*']
        random_simbol = random.choice(simbol)
        hasil = eval(f'{angka1} {random_simbol} {angka2}')
        try :
            print("Selamat Datang di Game Tebakan Matematika")
            print('===============LV 5=======================')
            print(f'Oke, sekarang kita mulai tebak-tebakan matematika!')
            print(f'Berapakah hasil dari {angka1} {random_simbol} {angka2}?')
            
            jawaban = int(input("Masukan jawaban: "))

            if jawaban == hasil:
                print(f'Yeay! Kamu benar, jawabannya {hasil}. Lanjut? Y/N')
                pilihan = input().lower()
                if pilihan == 'n':
                    return  
                elif pilihan == 'y':
                    continue  
            else:
                print(f"Jawaban kamu salah, yang benar adalah {hasil}.")
                pilihan = input("Tekan Enter untuk mengulang, atau ketik 'NYERAH'...").lower()
                if pilihan == "nyerah":
                    return  
                else:
                    continue  
        except ValueError:
            print("Masukkan angka yang benar ya....")
            input("Tekan Enter untuk melanjutkan...")
def level5():
     while True:
        angka1 = random.randint(1, 500)
        angka2 = random.randint(1, 500)
        simbol = ['+', '-', '/', '*']
        random_simbol = random.choice(simbol)
        hasil = eval(f'{angka1} {random_simbol} {angka2}')
        try :
            print("Selamat Datang di Game Tebakan Matematika")
            print('===============LV 5=======================')
            print(f'Oke, sekarang kita mulai tebak-tebakan matematika!')
            print(f'Berapakah hasil dari {angka1} {random_simbol} {angka2}?')
            
            jawaban = int(input("Masukan jawaban: "))

            if jawaban == hasil:
                print(f'Yeay! Kamu benar, jawabannya {hasil}. Lanjut? Y/N')
                pilihan = input().lower()
                if pilihan == 'n':
                    return  
                elif pilihan == 'y':
                    continue  
            else:
                print(f"Jawaban kamu salah, yang benar adalah {hasil}.")
                pilihan = input("Tekan Enter untuk mengulang, atau ketik 'NYERAH'...").lower()
                if pilihan == "nyerah":
                    return  
                else:
                    continue  
        except ValueError:
            print("Masukkan angka yang benar ya....")
            input("Tekan Enter untuk melanjutkan...")
                
def game_jokesbapak():
    reset_terminal()
    print('Selamat datang di Game Jokes Bapak-Bapak')
    print("   ===== Seberapa Bapak-Bapak Kamu? =======")
    nama = input('Masukan namanya pak... : ')
    
    jokes_with_answers = [
        ("Antara besi 50 kg dengan kapas 50 kg, pas kalau dijatuhkan di kaki, nanti sakitan mana?", "sakitan kakinya"),
        ("Dia membuat karya, pas jadi hasil karya tersebut diinjak-injak tidak marah, siap coba?", "Pembuat sandal"),
        ("Hitam, putih, merah, apakah itu?", "Zebra abis dikerokin"),
        ("Telor apa yang sangar?", "Telor asin"),
        ("Telor asin takut ama siapa?", "telor puyuh"),
        ("Masak air biar apa?" ,"Biar Mateng"),
        ('Kecil putih, larinya cepet bgt', 'nasi nempel dikereta'),
    ]
    
    while True:
        # reset_terminal()  # Pastikan fungsi ini ada jika Anda menggunakannya
        joke, answers = random.choice(jokes_with_answers)
        # Ambil jawaban yang benar
        correct_answer = random.choice(answers)

        # Menyiapkan pilihan jawaban yang ditampilkan
        other_answers = random.sample(answers, 3)  # Mengambil 3 jawaban lain
        all_answers = [correct_answer] + other_answers
        random.shuffle(all_answers)  # Mengacak pilihan jawaban

        print(f"Pertanyaannya untuk {nama}:")
        print(joke)
        print(f"A. {all_answers[0]}")
        print(f"B. {all_answers[1]}")
        print(f"C. {all_answers[2]}")
        print(f"D. {all_answers[3]}")

        jawaban = input("Jawabanmu: ").strip()
        
        # Memeriksa apakah jawaban yang diberikan adalah jawaban yang benar
        if jawaban.lower() == correct_answer.lower():
            print("Jawaban kamu benar! Yeay!")
        else:
            print(f"Jawaban kamu salah! Jawaban yang benar adalah: {correct_answer}")

        pilihan = input("\nTekan Enter untuk lanjut atau ketik 'keluar' untuk mengakhiri... ").lower()
        if pilihan == 'keluar':
            print("Terima kasih sudah bermain!")
            break

def menu_utama():
    while True:
        try:
            reset_terminal()
            print('Kumpulan Game Tebak Tebakan Asah Otak')
            print('   =======Created By Fikri======')
            print('1. Game Asah Otak')
            print('2. Game Jokes Bapack2')
            print("3. Keluar")
            pilih = int(input('Masukan Angka ....: '))
            if pilih == 1:
                main_tebakan()
            elif pilih == 2:
                game_jokesbapak()
            elif pilih == 3:
                input("Terimakasih telah memaikai Program ini ... Tekan Enter untuk keluar")
                break
        except ValueError:
            print('Masukan angka bosku,,,,,')
            continue

menu_utama()


                


