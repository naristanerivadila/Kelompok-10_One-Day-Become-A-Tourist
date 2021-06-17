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
