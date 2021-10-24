import os as os
import time


# ----------------------- PC Kapatma Uygulaması -----------------------


def seconds_shutdown(time):

    zaman_düzenlemesi = time * 60

    os.system(f"shutdown /s /t {zaman_düzenlemesi}")
    return f"{kapatma_işlemi} dakika içerisinde bilgisayarınız kapanacak."



def restart():

    print("Bilgisayarınız yeniden başlatılıyor...")
    time.sleep(0.5)
    os.system("shutdown /r")



def calloff_process():

    os.system("shutdown /a")

    return "Tüm Bilgisayar Kapatma İşlemleri İptal Edildi !"



def starting_app():

    print("\n")
    print("******************************************************")

    print("PC Kapatma Uygulaması")

    print("******************************************************")
    print("\n")

    print("""- Verilen Süre İçerisinde Kapanması İçin: 1
-- Bilgisayarı Yeniden Başlatmak İçin: 2
--- Bilgisayar Kapatma İşlemlerini Sonlandırmak İçin: 3
---- Belirlenen Saatte Kapanması İçin: 4""")

    print("\n")





starting_app()


while True:

    try:
        kapatma_işlemi = int(input("***** Lütfen Seçeneklerinden Birini Seçiniz:"))

    except:

        print("Lütfen Geçerli Bir Değer Giriniz !")
        continue

    break



while True:

    if kapatma_işlemi == 1:

        try:

            time = int(input("Bilgisayar Kaç Dakika İçerisinde Kapansın ?: "))
            seconds_shutdown(time)

        except:
            print("Lütfen Geçerli Bir Değer Giriniz !")

            continue

        break


    elif kapatma_işlemi == 2:

        restart()
        break


    elif kapatma_işlemi == 3:

        calloff_process()
        break

    else:

        print("Lütfen Geçerli Bir İşlem Giriniz !")
        continue
