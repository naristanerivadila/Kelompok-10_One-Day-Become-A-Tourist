#KELOMPOK 10
#TUGAS BESAR PROGRAMA KOMPUTER 2021

import sys
import datetime
import pytz
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

# Menu Tampilan Awal
def menu ():
    print()
    print('                       ONE DAY')
    print('                   become a TOURIST')
    print()
    print('====================W E L C O M E====================')
    print('Rasakan pengalaman melakukan perjalan online ke 5 kota')
    print('     yang paling terkenal di dunia secara online.')
    print('======================================================')
    print()
menu ()

#info kota
def menuinfolondon ():
    print()
    print('>>MENU INFORMASI<<')
    print('1. Sejarah Kota')
    print('2. Rekomendasi Wisata')
    print('3. Bahasa')
    print('4. Kuliner')
    print('5. Perbedaan Waktu')
    print('6. Jalan-Jalan Virtual')
    print('7. Exit')
    menu = input('Masukkan No. menu yang akan anda pilih : ')
    print()
    if menu == '1':
        london_sk = open("london_sk.txt", "r")
        print(london_sk.read())
        menuinfolondon()
    elif menu == '2':
        london_rw = open("london_rw.txt", "r")
        print(london_rw.read())
        menuinfolondon()
    elif menu == '3':
        london_b = open("london_b.txt", "r")
        print(london_b.read())
        menuinfolondon()
    elif menu == '4':
        london_k = open("london_k.txt", "r")
        print(london_k.read())
        menuinfolondon()
    elif menu == '5':
        print('waktu anda sekarang jika berada di kota London ialah : ')
        print()
        # gaperlu input lagi waktunya langsung convert aja nanti di output jamnya
        waktu_saya = datetime.datetime.now()

        # masukin variabel timezonenya yg lama sama baru
        timezone_lama = pytz.timezone("Asia/Jakarta")
        timezone_baru = pytz.timezone("Europe/London")

        # two-step process
        localized_timestamp = timezone_lama.localize(waktu_saya)
        new_timezone_timestamp = localized_timestamp.astimezone(timezone_baru)
        print(f"waktu WIB - London adalah {new_timezone_timestamp}")
        menuinfolondon()
    elif menu == '6':
        print('Untuk menikmati jalan-jalan virtual, ')
        print('silahkan copy-paste link ini ke web anda')
        print('https://driveandlisten.herokuapp.com/')
        print()
        menuinfolondon()
    elif menu == '7':
        print('Terimakasih telah mengunjungi program kami')
        sys.exit()
    else:
        print('MAAF DATA TIDAK VALID')
        print()
        infokota()

def menuinfoparis():
    print()
    print('>>MENU INFORMASI<<')
    print('1. Sejarah Kota')
    print('2. Rekomendasi Wisata')
    print('3. Bahasa')
    print('4. Kuliner')
    print('5. Perbedaan Waktu')
    print('6. Jalan-Jalan Virtual')
    print('7. Exit')
    menu = input('Masukkan No. menu yang akan anda pilih : ')
    print()
    if menu == '1':
        paris_sk = open("paris_sk.txt", "r")
        print(paris_sk.read())
        img = mpimg.imread('paris_sk.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfoparis()
    elif menu == '2':
        paris_rw = open("paris_rw.txt", "r")
        print(paris_rw.read())
        img = mpimg.imread('paris_rw.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfoparis()
    elif menu == '3':
        paris_b = open("paris_b.txt", "r")
        print(paris_b.read())
        menuinfoparis()
    elif menu == '4':
        paris_k = open("paris_k.txt", "r")
        print(paris_k.read())
        img = mpimg.imread('paris_k.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfoparis()
    elif menu == '5':
        print('waktu anda sekarang jika berada di kota paris ialah : ')
        print()
        # gaperlu input lagi waktunya langsung convert aja nanti di output jamnya
        waktu_saya = datetime.datetime.now()

        # masukin variabel timezonenya yg lama sama baru
        timezone_lama = pytz.timezone("Asia/Jakarta")
        timezone_baru = pytz.timezone("Europe/Paris")

        # two-step process
        localized_timestamp = timezone_lama.localize(waktu_saya)
        new_timezone_timestamp = localized_timestamp.astimezone(timezone_baru)
        print(f"waktu WIB - Paris adalah {new_timezone_timestamp}")
        menuinfoparis()
    elif menu == '6':
        print('Untuk menikmati jalan-jalan virtual, ')
        print('silahkan copy-paste link ini ke web anda')
        print('https://driveandlisten.herokuapp.com/')
        print()
        menuinfoparis()
    elif menu == '7':
        print('Terimakasih telah mengunjungi program kami')
        sys.exit()
    else:
        print('MAAF DATA TIDAK VALID')
        print()
        infokota()

def menuinfotokyo ():
    print()
    print('>>MENU INFORMASI<<')
    print('1. Sejarah Kota')
    print('2. Rekomendasi Wisata')
    print('3. Bahasa')
    print('4. Kuliner')
    print('5. Perbedaan Waktu')
    print('6. Jalan-Jalan Virtual')
    print('7. Exit')
    menu = input('Masukkan No. menu yang akan anda pilih : ')
    print()
    if menu == '1':
        tokyo_sk = open("tokyo_sk.txt", "r")
        print(tokyo_sk.read())
        img = mpimg.imread('tokyo_sk.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfotokyo()
    elif menu == '2':
        tokyo_rw = open("tokyo_rw.txt", "r")
        print(tokyo_rw.read())
        img = mpimg.imread('tokyo_rw.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfotokyo()
    elif menu == '3':
        tokyo_b = open("tokyo_b.txt", "r")
        print(tokyo_b.read())
        menuinfotokyo()
    elif menu == '4':
        tokyo_k = open("tokyo_k.txt", "r")
        print(tokyo_k.read())
        img = mpimg.imread('tokyo_k.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfotokyo()
    elif menu == '5':
        print('waktu anda sekarang jika berada di kota tokyo ialah : ')
        print()
        # gaperlu input lagi waktunya langsung convert aja nanti di output jamnya
        waktu_saya = datetime.datetime.now()

        # masukin variabel timezonenya yg lama sama baru
        timezone_lama = pytz.timezone("Asia/Jakarta")
        timezone_baru = pytz.timezone("Asia/Tokyo")

        # two-step process
        localized_timestamp = timezone_lama.localize(waktu_saya)
        new_timezone_timestamp = localized_timestamp.astimezone(timezone_baru)
        print(f"waktu WIB - Tokyo adalah {new_timezone_timestamp}")
        menuinfotokyo()
    elif menu == '6':
        print('Untuk menikmati jalan-jalan virtual, ')
        print('silahkan copy-paste link ini ke web anda')
        print('https://driveandlisten.herokuapp.com/')
        print()
        menuinfotokyo()
    elif menu == '7':
        print('Terimakasih telah mengunjungi program kami')
        sys.exit()
    else:
        print('MAAF DATA TIDAK VALID')
        print()
        infokota()

def menuinfomoscow():
    print()
    print('>>MENU INFORMASI<<')
    print('1. Sejarah Kota')
    print('2. Rekomendasi Wisata')
    print('3. Bahasa')
    print('4. Kuliner')
    print('5. Perbedaan Waktu')
    print('6. Jalan-Jalan Virtual')
    print('7. Exit')
    menu = input('Masukkan No. menu yang akan anda pilih : ')
    print()
    if menu == '1':
        moscow_sk = open("moscow_sk.txt", "r")
        print(moscow_sk.read())
        img = mpimg.imread('moskow_sk.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfomoscow()
    elif menu == '2':
        moscow_rw = open("moscow_rw.txt", "r")
        print(moscow_rw.read())
        img = mpimg.imread('moskow_rw.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfomoscow()
    elif menu == '3':
        moscow_b = open("moscow_b.txt", "r")
        print(moscow_b.read())
        menuinfomoscow()
    elif menu == '4':
        moscow_k = open("moscow_k.txt", "r")
        print(moscow_k.read())
        img = mpimg.imread('moskow_k.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfomoscow()
    elif menu == '5':
        print('waktu anda sekarang jika berada di kota moscow ialah : ')
        print()
        # gaperlu input lagi waktunya langsung convert aja nanti di output jamnya
        waktu_saya = datetime.datetime.now()

        # masukin variabel timezonenya yg lama sama baru
        timezone_lama = pytz.timezone("Asia/Jakarta")
        timezone_baru = pytz.timezone("Europe/Moscow")

        # two-step process
        localized_timestamp = timezone_lama.localize(waktu_saya)
        new_timezone_timestamp = localized_timestamp.astimezone(timezone_baru)
        print(f"waktu WIB - Moscow adalah {new_timezone_timestamp}")
        menuinfomoscow()
    elif menu == '6':
        print('Untuk menikmati jalan-jalan virtual, ')
        print('silahkan copy-paste link ini ke web anda')
        print('https://driveandlisten.herokuapp.com/')
        print()
        menuinfomoscow()
    elif menu == '7':
        print('Terimakasih telah mengunjungi program kami')
        sys.exit()
    else:
        print('MAAF DATA TIDAK VALID')
        print()
        infokota()

def menuinfony():
    print()
    print('>>MENU INFORMASI<<')
    print('1. Sejarah Kota')
    print('2. Rekomendasi Wisata')
    print('3. Bahasa')
    print('4. Kuliner')
    print('5. Perbedaan Waktu')
    print('6. Jalan-Jalan Virtual')
    print('7. Exit')
    menu = input('Masukkan No. menu yang akan anda pilih : ')
    print()
    if menu == '1':
        ny_sk = open("ny_sk.txt", "r")
        print(ny_sk.read())
        img = mpimg.imread('ny_sk.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfony()
    elif menu == '2':
        ny_rw = open("ny_rw.txt", "r")
        print(ny_rw.read())
        img = mpimg.imread('ny_rw.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfony()
    elif menu == '3':
        ny_b = open("ny_b.txt", "r")
        print(ny_b.read())
        menuinfony()
    elif menu == '4':
        ny_k = open("ny_k.txt", "r")
        print(ny_k.read())
        img = mpimg.imread('ny_k.jpg')
        imgplot = plt.imshow(img)
        plt.show()
        menuinfony()
    elif menu == '5':
        print('waktu anda sekarang jika berada di Kota New York ialah : ')
        print()
        # gaperlu input lagi waktunya langsung convert aja nanti di output jamnya
        waktu_saya = datetime.datetime.now()

        # masukin variabel timezonenya yg lama sama baru
        timezone_lama = pytz.timezone("Asia/Jakarta")
        timezone_baru = pytz.timezone("America/New_York")

        # two-step process
        localized_timestamp = timezone_lama.localize(waktu_saya)
        new_timezone_timestamp = localized_timestamp.astimezone(timezone_baru)
        print(f"waktu WIB - New York adalah {new_timezone_timestamp}")
        menuinfony()
    elif menu == '6':
        print('Untuk menikmati jalan-jalan virtual, ')
        print('silahkan copy-paste link ini ke web anda')
        print('https://driveandlisten.herokuapp.com/')
        print()
        menuinfony()
    elif menu == '7':
        print('Terimakasih telah mengunjungi program kami')
        sys.exit()
    else:
        print('MAAF DATA TIDAK VALID')
        print()
        infokota()

def infokota():
    print()
    print("-----SELAMAT ANDA TELAH DAPAT MENGAKSES PROGRAM ONE DAY BECOME A TOURIST-----")
    print('Kota apa yang akan anda kunjungi?')
    print('1. London')
    print('2. Paris')
    print('3. Tokyo')
    print('4. Moscow')
    print('5. New York')
    kotaawal = input('Masukkan No. kota yang akan dikunjungi : ')
    print()
    if kotaawal == '1':
        print('>>MENU INFORMASI<<')
        print('1. Sejarah Kota')
        print('2. Rekomendasi Wisata')
        print('3. Bahasa')
        print('4. Kuliner')
        print('5. Perbedaan Waktu')
        print('6. Jalan-Jalan Virtual')
        print('7. Exit')
        menu = input('Masukkan No. menu yang akan anda pilih : ')
        print()
        if menu == '1':
            london_sk = open("london_sk.txt", "r")
            print(london_sk.read())
            img = mpimg.imread('london_sk.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfolondon()
        elif menu == '2':
            london_rw = open("london_rw.txt", "r")
            print(london_rw.read())
            img = mpimg.imread('london_rw.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfolondon()
        elif menu == '3':
            london_b = open("london_b.txt", "r")
            print(london_b.read())
            menuinfolondon()
        elif menu == '4':
            london_k = open("london_k.txt", "r")
            print(london_k.read())
            img = mpimg.imread('london_k.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfolondon()
        elif menu == '5':
            print('waktu anda sekarang jika berada di kota London ialah : ')
            print()
            # gaperlu input lagi waktunya langsung convert aja nanti di output jamnya
            waktu_saya = datetime.datetime.now()

            # masukin variabel timezonenya yg lama sama baru
            timezone_lama = pytz.timezone("Asia/Jakarta")
            timezone_baru = pytz.timezone("Europe/London")

            # two-step process
            localized_timestamp = timezone_lama.localize(waktu_saya)
            new_timezone_timestamp = localized_timestamp.astimezone(timezone_baru)
            print(f"waktu WIB - London adalah {new_timezone_timestamp}")
            menuinfolondon()
        elif menu == '6':
            print('Untuk menikmati jalan-jalan virtual, ')
            print('silahkan copy-paste link ini ke web anda')
            print('https://driveandlisten.herokuapp.com/')
            print()
            menuinfolondon()
        elif menu == '7':
            print('Terimakasih telah mengunjungi program kami')
            sys.exit()
        else:
            print('MAAF DATA TIDAK VALID')
            print()
            infokota()
    elif kotaawal == '2':
        print('>>MENU INFORMASI<<')
        print('1. Sejarah Kota')
        print('2. Rekomendasi Wisata')
        print('3. Bahasa')
        print('4. Kuliner')
        print('5. Perbedaan Waktu')
        print('6. Jalan-Jalan Virtual')
        print('7. Exit')
        menu = input('Masukkan No. menu yang akan anda pilih : ')
        print()
        if menu == '1':
            paris_sk = open("paris_sk.txt", "r")
            print(paris_sk.read())
            img = mpimg.imread('paris_sk.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfoparis()
        elif menu == '2':
            paris_rw = open("paris_rw.txt", "r")
            print(paris_rw.read())
            img = mpimg.imread('paris_rw.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfoparis()
        elif menu == '3':
            paris_b = open("paris_b.txt", "r")
            print(paris_b.read())
            menuinfoparis()
        elif menu == '4':
            paris_k = open("paris_k.txt", "r")
            print(paris_k.read())
            img = mpimg.imread('paris_k.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfoparis()
        elif menu == '5':
            print('waktu anda sekarang jika berada di kota paris ialah : ')
            print()
            # gaperlu input lagi waktunya langsung convert aja nanti di output jamnya
            waktu_saya = datetime.datetime.now()

            # masukin variabel timezonenya yg lama sama baru
            timezone_lama = pytz.timezone("Asia/Jakarta")
            timezone_baru = pytz.timezone("Europe/Paris")

            # two-step process
            localized_timestamp = timezone_lama.localize(waktu_saya)
            new_timezone_timestamp = localized_timestamp.astimezone(timezone_baru)
            print(f"waktu WIB - Paris adalah {new_timezone_timestamp}")
            menuinfoparis()
        elif menu == '6':
            print('Untuk menikmati jalan-jalan virtual, ')
            print('silahkan copy-paste link ini ke web anda')
            print('https://driveandlisten.herokuapp.com/')
            print()
            menuinfoparis()
        elif menu == '7':
            print('Terimakasih telah mengunjungi program kami')
            sys.exit()
        else:
            print('MAAF DATA TIDAK VALID')
            print()
            infokota()
    elif kotaawal == '3':
        print('>>MENU INFORMASI<<')
        print('1. Sejarah Kota')
        print('2. Rekomendasi Wisata')
        print('3. Bahasa')
        print('4. Kuliner')
        print('5. Perbedaan Waktu')
        print('6. Jalan-Jalan Virtual')
        print('7. Exit')
        menu = input('Masukkan No. menu yang akan anda pilih : ')
        print()
        if menu == '1':
            tokyo_sk = open("tokyo_sk.txt", "r")
            print(tokyo_sk.read())
            img = mpimg.imread('tokyo_sk.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfotokyo()
        elif menu == '2':
            tokyo_rw = open("tokyo_rw.txt", "r")
            print(tokyo_rw.read())
            img = mpimg.imread('tokyo_rw.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfotokyo()
        elif menu == '3':
            tokyo_b = open("tokyo_b.txt", "r")
            print(tokyo_b.read())
            menuinfotokyo()
        elif menu == '4':
            tokyo_k = open("tokyo_k.txt", "r")
            print(tokyo_k.read())
            img = mpimg.imread('tokyo_k.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfotokyo()
        elif menu == '5':
            print('waktu anda sekarang jika berada di kota tokyo ialah : ')
            print()
            # gaperlu input lagi waktunya langsung convert aja nanti di output jamnya
            waktu_saya = datetime.datetime.now()

            # masukin variabel timezonenya yg lama sama baru
            timezone_lama = pytz.timezone("Asia/Jakarta")
            timezone_baru = pytz.timezone("Asia/Tokyo")

            # two-step process
            localized_timestamp = timezone_lama.localize(waktu_saya)
            new_timezone_timestamp = localized_timestamp.astimezone(timezone_baru)
            print(f"waktu WIB - Tokyo adalah {new_timezone_timestamp}")
            menuinfotokyo()
        elif menu == '6':
            print('Untuk menikmati jalan-jalan virtual, ')
            print('silahkan copy-paste link ini ke web anda')
            print('https://driveandlisten.herokuapp.com/')
            print()
            menuinfotokyo()
        elif menu == '7':
            print('Terimakasih telah mengunjungi program kami')
            sys.exit()
        else:
            print('MAAF DATA TIDAK VALID')
            print()
            infokota()
    elif kotaawal == '4':
        print()
        print('>>MENU INFORMASI<<')
        print('1. Sejarah Kota')
        print('2. Rekomendasi Wisata')
        print('3. Bahasa')
        print('4. Kuliner')
        print('5. Perbedaan Waktu')
        print('6. Jalan-Jalan Virtual')
        print('7. Exit')
        menu = input('Masukkan No. menu yang akan anda pilih : ')
        print()
        if menu == '1':
            moscow_sk = open("moscow_sk.txt", "r")
            print(moscow_sk.read())
            img = mpimg.imread('moskow_sk.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfomoscow()
        elif menu == '2':
            moscow_rw = open("moscow_rw.txt", "r")
            print(moscow_rw.read())
            img = mpimg.imread('moskow_rw.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfomoscow()
        elif menu == '3':
            moscow_b = open("moscow_b.txt", "r")
            print(moscow_b.read())
            menuinfomoscow()
        elif menu == '4':
            moscow_k = open("moscow_k.txt", "r")
            print(moscow_k.read())
            img = mpimg.imread('moskow_k.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfomoscow()
        elif menu == '5':
            print('waktu anda sekarang jika berada di kota moscow ialah : ')
            print()
            # gaperlu input lagi waktunya langsung convert aja nanti di output jamnya
            waktu_saya = datetime.datetime.now()

            # masukin variabel timezonenya yg lama sama baru
            timezone_lama = pytz.timezone("Asia/Jakarta")
            timezone_baru = pytz.timezone("Europe/Moscow")

            # two-step process
            localized_timestamp = timezone_lama.localize(waktu_saya)
            new_timezone_timestamp = localized_timestamp.astimezone(timezone_baru)
            print(f"waktu WIB - Moscow adalah {new_timezone_timestamp}")
            menuinfomoscow()
        elif menu == '6':
            print('Untuk menikmati jalan-jalan virtual, ')
            print('silahkan copy-paste link ini ke web anda')
            print('https://driveandlisten.herokuapp.com/')
            print()
            menuinfomoscow()
        elif menu == '7':
            print('Terimakasih telah mengunjungi program kami')
            sys.exit()
        else:
            print('MAAF DATA TIDAK VALID')
            print()
            infokota()
    elif kotaawal == '5':
        print()
        print('>>MENU INFORMASI<<')
        print('1. Sejarah Kota')
        print('2. Rekomendasi Wisata')
        print('3. Bahasa')
        print('4. Kuliner')
        print('5. Perbedaan Waktu')
        print('6. Jalan-Jalan Virtual')
        print('7. Exit')
        menu = input('Masukkan No. menu yang akan anda pilih : ')
        print()
        if menu == '1':
            ny_sk = open("ny_sk.txt", "r")
            print(ny_sk.read())
            img = mpimg.imread('ny_sk.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfony()
        elif menu == '2':
            ny_rw = open("ny_rw.txt", "r")
            print(ny_rw.read())
            img = mpimg.imread('ny_rw.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfony()
        elif menu == '3':
            ny_b = open("ny_b.txt", "r")
            print(ny_b.read())
            menuinfony()
        elif menu == '4':
            ny_k = open("ny_k.txt", "r")
            print(ny_k.read())
            img = mpimg.imread('ny_k.jpg')
            imgplot = plt.imshow(img)
            plt.show()
            menuinfony()
        elif menu == '5':
            print('waktu anda sekarang jika berada di Kota New York ialah : ')
            print()
            # gaperlu input lagi waktunya langsung convert aja nanti di output jamnya
            waktu_saya = datetime.datetime.now()

            # masukin variabel timezonenya yg lama sama baru
            timezone_lama = pytz.timezone("Asia/Jakarta")
            timezone_baru = pytz.timezone("America/New_York")

            # two-step process
            localized_timestamp = timezone_lama.localize(waktu_saya)
            new_timezone_timestamp = localized_timestamp.astimezone(timezone_baru)
            print(f"waktu WIB - New York adalah {new_timezone_timestamp}")
            menuinfony()
        elif menu == '6':
            print('Untuk menikmati jalan-jalan virtual, ')
            print('silahkan copy-paste link ini ke web anda')
            print('https://driveandlisten.herokuapp.com/')
            print()
            menuinfony()
        elif menu == '7':
            print('Terimakasih telah mengunjungi program kami')
            sys.exit()
        else:
            print('MAAF DATA TIDAK VALID')
            print()
            infokota()
    else :
        print('MAAF DATA TIDAK VALID')
        print()
        infokota()

# Input data Pengguna
def datapengguna ():
    print('                 INFORMASI PENGGUNA')
    nama     = input('Masukkan nama lengkap Anda               : ')
    for name in nama:
        if name.isdigit():
            print("Tolong Masukan Dengan Huruf")
            datapengguna()
    jk       = input('Masukkan jenis kelamin Anda (P/L)        : ')
    nohp     = input('Masukkan No HP pengguna                 : +62 ')
    ttinggal = input('Masukkan alamat anda                     : ')
    print()
    print('======================================================')
    print()
    if jk == 'L' or jk == 'l':
        print("Selamat Datang, Tuan", nama, "!")
        info1 = open("info1.txt", "r")
        print(info1.read())
    else:
        print("Selamat Datang, Nyonya", nama, "!")
        info1 = open("info1.txt", "r")
        print(info1.read())
datapengguna ()

# info kota awal 2
def infokotaawal2 ():
    print('Kota apa yang akan anda kunjungi?')
    print('1. London')
    print('2. Paris')
    print('3. Tokyo')
    print('4. Moscow')
    print('5. New York')
    kotaawal = input('Masukkan No. kota yang akan dikunjungi : ')
    if kotaawal == '1':
        print('>>London')
        S_london = open("S_london.txt", "r")
        print(S_london.read())
        yakin1()
    elif kotaawal == '2':
        print('>>Paris')
        S_paris = open("S_paris.txt", "r")
        print(S_paris.read())
        yakin1()
    elif kotaawal == '3':
        print('>>Tokyo')
        S_tokyo = open("S_tokyo.txt", "r")
        print(S_tokyo.read())
        yakin1()
    elif kotaawal == '4':
        print('>>Moscow')
        S_moscow = open("S_moscow.txt", "r")
        print(S_moscow.read())
        yakin1()
    elif kotaawal == '5':
        print('>>New York')
        S_ny = open("S_ny.txt", "r")
        print(S_ny.read())
        yakin1()
    else :
        print('MAAF DATA TIDAK VALID')
        print()
        infokotaawal2 ()

def struk():
    #kode pelunasan
    lunas = random.randrange(55555, 77777, 10)
    print("Kode Pembayaran anda adalah", lunas)
    print("Silahkan membayar ke No. Akun tersebut")
    print()
    while True:
        bayarr = int(input("Masukan Kode Pelunasan: "))
        if bayarr == lunas:
            print("Pembayaran Dengan No Akun", bayarr, "Berhasil. \n Hubungi Admin Jika Ada Kendala")
            break
        else:
            print("Maaf, Kode Pelunasan Salah!")

    # Menampilkan struk
    nama = input('Masukkan nama lengkap Anda               : ')
    jk = input('Masukkan jenis kelamin Anda (P/L)        : ')
    nohp = input('Masukkan No HP pengguna                  : +62 ')
    ttinggal = input('Masukkan alamat anda                     : ')

    print()
    print('======================================================')
    print("                 STRUK PEMBELIAN")
    print('======================================================')
    print()
    print(" Nama                :", nama)
    print(" Jenis Kelamin       :", jk)
    print(" Nomor HP            :", nohp)
    print(" Alamat              :", ttinggal)
    print(" Kode Pembayaran     :", bayarr)
    print(" Nominal Bayar       : Rp. 5.000")
    print("==============================================================")
    print("                        TERIMA KASIH                          ")
    print("==============================================================")
    infokota()

#merchandise
def strukbeli():
    #kode pelunasan
    print()
    lunas = random.randrange(55555, 77777, 10)
    print("Kode Pembayaran anda adalah", lunas)
    print("Silahkan membayar ke No. Akun tersebut")
    while True:
        print()
        bayarr = int(input("Masukan Kode Pelunasan: "))
        if bayarr == lunas:
            print("Pembayaran Dengan No Akun", bayarr, "Berhasil. \n Hubungi Admin Jika Ada Kendala")
            break
        else:
            print("Maaf, Kode Pelunasan Salah!")

    # Menampilkan struk
    print()
    print('----------MENGISI DATA PEMBELI----------')
    nama = input('Masukkan nama lengkap Anda               : ')
    jk = input('Masukkan jenis kelamin Anda (P/L)        : ')
    nohp = input('Masukkan No HP pengguna                  : +62 ')
    ttinggal = input('Masukkan alamat anda                     : ')

    print()
    print('======================================================')
    print("                 STRUK PEMBELIAN")
    print('======================================================')
    print()
    print(" Nama                : ", nama)
    print(" Jenis Kelamin       : ", jk)
    print(" Nomor HP            : +62", nohp)
    print(" Alamat              : ", ttinggal)
    print(" Metode Pembayaran   : ", bayarr)
    print(" Nominal Bayar       : Rp.", tbayar)
    print("==============================================================")
    print("                        TERIMA KASIH                          ")
    print("==============================================================")
    print()
    print("Terimakasih pesanan akan dikirim\n"
          "Apabila belum terkirim dapat hubungi admin.")
    infokota()

def metodebayar2():
    global tbayar

    print("Pilih Metode Pembayaran\n"
              "[1] Gopay\n"
              "[2] Bank Mandiri\n"
              "[3] OVO\n")
    bayar = int(input('>>'))
    if bayar == 1:
        tbayar = int(input('Masukkan total nominal pembelajaan ke rekening yg telah disediakan : '))
        strukbeli()
    elif bayar == 2:
        tbayar = int(input('Masukkan total nominal pembelajaan ke rekening yg telah disediakan : '))
        strukbeli()
    else:
        tbayar = int(input('Masukkan total nominal pembelajaan ke rekening yg telah disediakan : '))
        strukbeli()

def merchandise ():
    # Menampilkan katalog merchandise dan promo
    print()
    print('======================================================')
    print("                 KATALOG MERCHANDISE")
    print('======================================================')
    print()
    merch = open("merch.txt", "r")
    print(merch.read())

    # Menampilkan informasi promo
    print("--- Diskon 10 % untuk pembelian merchandise lebih dari Rp 100.000 ---")
    print()
    pilihan()

def pilihan():
    # Menampilkan pilihan merchandise yang akan dibeli oleh pengunjung
    a = "T-Shirt Los Angeles Kings Catton Combed Black Rp 65.000"
    b = "T Shirt World Series Catton Combed Black Rp 65.000"
    c = "T Shirt Sushi Taste Catton Combed Black Rp 65.000"
    d = "Sweater Crewneck Basic Black and white Rp 75.000"
    e = "Sweater Crewneck Colorful Rp 139.500"
    f = "Tumblr Rp 25.000"
    g = "Magnet Kulkas Rp 10.000"
    h = "Souvenir Gantungan Kunci Menara Eiffel Paris Rp 30.000"
    i = "Miniatur Big Ben England 30 cm Rp 124.000"
    j = "Miniatur Bus London Rp 227.000"

    # Menampilkan harga merchandise
    pilkaos_1 = 65000
    pilkaos_2 = 65000
    pilkaos_3 = 65000
    pilsweater_1 = 75000
    pilsweater_2 = 139500
    tumblr = 25000
    magnet = 10000
    ganci = 30000
    mini_1 = 124000
    mini_2 = 227000

    #alamat ongkir
    ongkir_l = 5000
    ongkir_s = 7000
    ongkir_b = 9000
    ongkir_pk = 11000
    ongkir_j = 13000


#pemilihan merhendise
    global bayar
    global pilih
    global harga

    merch = input("Merchandise yang dipilih : ")
    if merch == "a":
        pilih = pilkaos_1
        print(pilkaos_1)
        #alamat ongkir
        print()
        print('barang anda akan diantarkan hanya jika berada di kota solo')
        rumah = input("Masukan alamat rumah anda : ")
        alamat = input("Kecamatan (Laweyan/Jebres/Pasar Kliwon/Banjarsari/Serengan) : ")
        if alamat == "Laweyan":
            bayar = ongkir_l + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Jebres":
            bayar = ongkir_j + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Pasar Kliwon":
            bayar = ongkir_pk + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Banjarsari":
            bayar = ongkir_b + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Serengan":
            bayar = ongkir_s + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        else:
            print('Alamat yang anda cantumkan tidak dapat dideteksi')
            sys.exit()
    elif merch == "b":
        pilih = pilkaos_2
        print(pilkaos_2)
        # alamat ongkir
        print()
        print('barang anda akan diantarkan hanya jika berada di kota solo')
        rumah = input("Masukan alamat rumah anda : ")
        alamat = input("Kecamatan (Laweyan/Jebres/Pasar Kliwon/Banjarsari/Serengan) : ")
        if alamat == "Laweyan":
            bayar = ongkir_l + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Jebres":
            bayar = ongkir_j + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Pasar Kliwon":
            bayar = ongkir_pk + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Banjarsari":
            bayar = ongkir_b + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Serengan":
            bayar = ongkir_s + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        else:
            print('Alamat yang anda cantumkan tidak dapat dideteksi')
            sys.exit()
    elif merch == "c":
        pilih = pilkaos_3
        print(pilkaos_3)
        # alamat ongkir
        print()
        print('barang anda akan diantarkan hanya jika berada di kota solo')
        rumah = input("Masukan alamat rumah anda : ")
        alamat = input("Kecamatan (Laweyan/Jebres/Pasar Kliwon/Banjarsari/Serengan) : ")
        if alamat == "Laweyan":
            bayar = ongkir_l + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Jebres":
            bayar = ongkir_j + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Pasar Kliwon":
            bayar = ongkir_pk + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Banjarsari":
            bayar = ongkir_b + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Serengan":
            bayar = ongkir_s + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        else:
            print('Alamat yang anda cantumkan tidak dapat dideteksi')
            sys.exit()
    elif merch == "d":
        pilih = pilsweater_1
        print(pilsweater_1)
        # alamat ongkir
        print()
        print('barang anda akan diantarkan hanya jika berada di kota solo')
        rumah = input("Masukan alamat rumah anda : ")
        alamat = input("Kecamatan (Laweyan/Jebres/Pasar Kliwon/Banjarsari/Serengan) : ")
        if alamat == "Laweyan":
            bayar = ongkir_l + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Jebres":
            bayar = ongkir_j + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Pasar Kliwon":
            bayar = ongkir_pk + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Banjarsari":
            bayar = ongkir_b + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Serengan":
            bayar = ongkir_s + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        else:
            print('Alamat yang anda cantumkan tidak dapat dideteksi')
            sys.exit()
    elif merch == "e":
        total1 = pilsweater_2
        print(pilsweater_2)
        print('-----------------Selamat anda mendapatkan promo 10%-----------------')
        promo = int(total1) * 10 / 100
        pilih = round(int(total1) - promo)
        print('Total belanja anda adalah', pilih)
        # alamat ongkir
        print()
        print('barang anda akan diantarkan hanya jika berada di kota solo')
        rumah = input("Masukan alamat rumah anda : ")
        alamat = input("Kecamatan (Laweyan/Jebres/Pasar Kliwon/Banjarsari/Serengan) : ")
        if alamat == "Laweyan":
            bayar = ongkir_l + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Jebres":
            bayar = ongkir_j + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Pasar Kliwon":
            bayar = ongkir_pk + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Banjarsari":
            bayar = ongkir_b + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Serengan":
            bayar = ongkir_s + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        else:
            print('Alamat yang anda cantumkan tidak dapat dideteksi')
            sys.exit()
    elif merch == "f":
        pilih = tumblr
        print(tumblr)
        # alamat ongkir
        print()
        print('barang anda akan diantarkan hanya jika berada di kota solo')
        rumah = input("Masukan alamat rumah anda : ")
        alamat = input("Kecamatan (Laweyan/Jebres/Pasar Kliwon/Banjarsari/Serengan) : ")
        if alamat == "Laweyan":
            bayar = ongkir_l + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Jebres":
            bayar = ongkir_j + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Pasar Kliwon":
            bayar = ongkir_pk + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Banjarsari":
            bayar = ongkir_b + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Serengan":
            bayar = ongkir_s + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        else:
            print('Alamat yang anda cantumkan tidak dapat dideteksi')
            sys.exit()
    elif merch == "g":
        pilih = magnet
        print(magnet)
        # alamat ongkir
        print()
        print('barang anda akan diantarkan hanya jika berada di kota solo')
        rumah = input("Masukan alamat rumah anda : ")
        alamat = input("Kecamatan (Laweyan/Jebres/Pasar Kliwon/Banjarsari/Serengan) : ")
        if alamat == "Laweyan":
            bayar = ongkir_l + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Jebres":
            bayar = ongkir_j + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Pasar Kliwon":
            bayar = ongkir_pk + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Banjarsari":
            bayar = ongkir_b + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Serengan":
            bayar = ongkir_s + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        else:
            print('Alamat yang anda cantumkan tidak dapat dideteksi')
            sys.exit()
    elif merch == "h":
        pilih = ganci
        print(ganci)
        # alamat ongkir
        print()
        print('barang anda akan diantarkan hanya jika berada di kota solo')
        rumah = input("Masukan alamat rumah anda : ")
        alamat = input("Kecamatan (Laweyan/Jebres/Pasar Kliwon/Banjarsari/Serengan) : ")
        if alamat == "Laweyan":
            bayar = ongkir_l + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Jebres":
            bayar = ongkir_j + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Pasar Kliwon":
            bayar = ongkir_pk + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Banjarsari":
            bayar = ongkir_b + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Serengan":
            bayar = ongkir_s + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        else:
            print('Alamat yang anda cantumkan tidak dapat dideteksi')
            sys.exit()
    elif merch == "i":
        total1 = mini_1
        print(mini_1)
        print('-----------------Selamat anda mendapatkan promo 10%-----------------')
        promo = int(total1) * 10 / 100
        pilih = round(int(total1) - promo)
        print('Total belanja anda adalah', pilih)
        # alamat ongkir
        print()
        print('barang anda akan diantarkan hanya jika berada di kota solo')
        rumah = input("Masukan alamat rumah anda : ")
        alamat = input("Kecamatan (Laweyan/Jebres/Pasar Kliwon/Banjarsari/Serengan) : ")
        if alamat == "Laweyan":
            bayar = ongkir_l + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Jebres":
            bayar = ongkir_j + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Pasar Kliwon":
            bayar = ongkir_pk + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Banjarsari":
            bayar = ongkir_b + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Serengan":
            bayar = ongkir_s + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        else:
            print('Alamat yang anda cantumkan tidak dapat dideteksi')
            sys.exit()
    elif merch == "j":
        total1 = mini_2
        print(mini_2)
        print('-----------------Selamat anda mendapatkan promo 10%-----------------')
        promo = int(total1) * 10 / 100
        pilih = round(int(total1) - promo)
        print('Total belanja anda adalah', pilih)
        # alamat ongkir
        print()
        print('barang anda akan diantarkan hanya jika berada di kota solo')
        rumah = input("Masukan alamat rumah anda : ")
        alamat = input("Kecamatan (Laweyan/Jebres/Pasar Kliwon/Banjarsari/Serengan) : ")
        if alamat == "Laweyan":
            bayar = ongkir_l + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Jebres":
            bayar = ongkir_j + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Pasar Kliwon":
            bayar = ongkir_pk + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Banjarsari":
            bayar = ongkir_b + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        elif alamat == "Serengan":
            bayar = ongkir_s + pilih + 5000
            print("Total yang harus dibayarkan : ", bayar)
            metodebayar2()
        else:
            print('Alamat yang anda cantumkan tidak dapat dideteksi')
            sys.exit()
    else:
        sys.exit()

def yakin1 ():
    print('Apakah anda yakin untuk mengunjungi kota tersebut? (Y/T)')
    yakin1 = input('= ')
    print()
    if yakin1=='Y' or yakin1=='y':
        print('Apakah anda ingin membeli merchandise? (Y/T)')
        bmerch = input('= ')
        if bmerch == "Y" or bmerch == "y":
            merchandise()
        else:
            metodebayar1()
            struk()
            infokota()
    elif yakin1=='T' or yakin1=='t':
        infokotaawal()
    else:
        print('MAAF DATA TIDAK VALID')
        print()
        sys.exit()

def metodebayar1():
    global bayar
    print("Pilih Metode Pembayaran Website (Rp. 5000)\n"
              "[1] Gopay\n"
              "[2] Bank Mandiri\n"
              "[3] OVO\n")
    bayar = int(input('>>'))
    if bayar == 1:
        struk()
    elif bayar == 2:
        struk()
    else:
        struk()

def infokotaawal ():
    print('Kota apa yang akan anda kunjungi?')
    print('1. London')
    print('2. Paris')
    print('3. Tokyo')
    print('4. Moscow')
    print('5. New York')
    kotaawal = input('Masukkan No. kota yang akan dikunjungi : ')
    if kotaawal == '1':
        print('>>London')
        S_london = open("S_london.txt", "r")
        print(S_london.read())
        yakin1()
    elif kotaawal == '2':
        print('>>Paris')
        S_paris = open("S_paris.txt", "r")
        print(S_paris.read())
        yakin1()
    elif kotaawal == '3':
        print('>>Tokyo')
        S_tokyo = open("S_tokyo.txt", "r")
        print(S_tokyo.read())
        yakin1()
    elif kotaawal == '4':
        print('>>Moscow')
        S_moscow = open("S_moscow.txt", "r")
        print(S_moscow.read())
        yakin1()
    elif kotaawal == '5':
        print('>>New York')
        S_ny = open("S_ny.txt", "r")
        print(S_ny.read())
        yakin1()
    else :
        print('MAAF DATA TIDAK VALID')
        print()
        infokotaawal ()
infokotaawal()