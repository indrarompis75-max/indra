# Program Game Tebak Angka
# Dibuat oleh AI Assistant

import random

def main():
    print("Selamat datang di Game Tebak Angka!")
    print("Saya telah memilih angka antara 1 dan 100. Coba tebak!")
    
    # Komputer pilih angka acak
    angka_rahasia = random.randint(1, 100)
    tebakan = 0
    jumlah_tebakan = 0
    
    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
            jumlah_tebakan += 1
            
            if tebakan < angka_rahasia:
                print("Terlalu rendah! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"Selamat! Anda menebak dengan benar dalam {jumlah_tebakan} tebakan.")
        except ValueError:
            print("Masukkan angka yang valid!")

if __name__ == "__main__":
    main()
    
