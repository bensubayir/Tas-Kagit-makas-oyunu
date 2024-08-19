import random

def tas_kagit_makas_ZAIDE_BENSU_BAYIR():
    
    print("Hoş geldiniz! Taş, Kağıt, Makas oyununa başlamak üzeresiniz.")
    print("Oyun kuralları: Taş makası yener, makas kağıdı yener, kağıt taşı yener.")
    print("Oyundan çıkmak için herhangi bir turdan sonra 'Hayır' diyebilirsiniz.\n")

    
    secenekler = ["taş", "kağıt", "makas"]

    while True:
        
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0
        oynanan_tur_sayisi = 0
        oyuncu_adi = input("Lütfen adınızı girin: ")

        while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            oynanan_tur_sayisi += 1
            print(f"\n{oynanan_tur_sayisi}. tur:")

            
            oyuncu_secimi = input("Taş, kağıt, makas seçin: ").lower()
            while oyuncu_secimi not in secenekler:
                oyuncu_secimi = input("Geçersiz seçim! Lütfen tekrar taş, kağıt veya makas seçin: ").lower()

            
            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayar {bilgisayar_secimi} seçti.")

            
            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print(f"Tebrikler {oyuncu_adi}, bu turu kazandınız!")
                oyuncu_galibiyetleri += 1
            else:
                print("Bilgisayar bu turu kazandı!")
                bilgisayar_galibiyetleri += 1

        
        if oyuncu_galibiyetleri == 2:
            print(f"\n{oyuncu_adi}, oyunu kazandınız!")
        else:
            print("\nBilgisayar oyunu kazandı!")

        
        devam_istegi = input("\nBaşka bir oyun oynamak ister misiniz? (Evet/Hayır): ").lower()
        if devam_istegi != "evet":
            print("Oyun bitti! Teşekkürler.")
            break

        
        bilgisayar_devam = random.choice(["evet", "hayır"])
        if bilgisayar_devam == "hayır":
            print("Bilgisayar artık oynamak istemiyor. Oyun sona erdi.")
            break

        print("Oyuna devam ediliyor...")


tas_kagit_makas_ZAIDE_BENSU_BAYIR()