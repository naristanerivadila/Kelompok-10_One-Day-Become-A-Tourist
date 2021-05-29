#KELOMPOK 10
#TUGAS BESAR PROGRAMA KOMPUTER 2021

import sys

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

# Input data Pengguna
def datapengguna ():
    print('                 INFORMASI PENGGUNA')
    nama     = input('Masukkan nama lengkap Anda               : ')
    jk       = input('Masukkan jenis kelamin Anda (P/L)        : ')
    nohp     = input('Masukkan No HP pengguna                 : +62 ')
    ttinggal = input('Masukkan alamat anda                     : ')
    www      = input('  WIB/WITA/WIT        : ')
    print('Masukkan waktu Anda sekarang             ')
    wjam     = input('  Jam                 : ')
    wmenit   = input('  Menit               : ')
    wampm    = input('  AM/PM               : ')
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

# info merchandise
def merchandise ():
    # Menampilkan katalog merchandise dan promo
    print()
    print('======================================================')
    print("                 KATALOG MERCHANDISE")
    print('======================================================')
    print()

    file_merchandise = open("merchandise.txt", "r")
    print(file_merchandise.read())

    # Menampilkan informasi promo
    print("--- Diskon 10 % untuk pembelian merchandise lebih dari Rp 100.000 ---")
    print()

    # Menmpilkan informasi keputusan pembelian merchandise
    print("Apakah anda ingin melakukan pembelian merchandise?")

    # Inputkan jawaban pengunjung
    keterangan = input("YES/NO : ")
    if keterangan == "YES":
        print("Silahkan lihat merchandise yang tersedia di dalam Katalog Merchandise untuk melakukan pembelian")
        print()
    else:
        print("Terima kasih telah mengunjungi Katalog Merchandise kami")
        # Menampilkan informasi metode pembayaran
        print()

    # Menampilkan pilihan merchandise yang akan dibeli oleh pengunjung
    a = "T-Shirt Los Angeles Kings Catton Combed Black Rp 65.000"
    b = "T Shirt World Series Catton Combed Black Rp 65.000"
    c = "T Shirt Sushi Taste Catton Combed Black Rp 65.000"
    d = "Tumblr Rp 25.000"
    e = "Souvenir Gantungan Kunci Menara Eiffel Paris Rp 30.000"
    f = "Sweater Crewneck Basic Black and WHite Rp 75.000"
    g = "Sweater Crewneck colorful Rp 139.500"
    h = "Miniatur Big Ben England 30 cm Rp 124.000"
    i = "Miniatur Bus London Rp 227.000"
    j = "Magnet Kulkas Rp 10.000"

    # Menampilkan harga merchandise
    pilkaos_1 = 65.000
    pilkaos_2 = 65.000
    pilkaos_3 = 65.000
    tumblr = 35.000
    ganci = 30.000
    pilsweater_1 = 75.000
    pilsweater_2 = 139.500
    pilmin_1 = 124.000
    pilmin_2 = 227.000
    magnet = 10.000

    merch = input("Merchandise yang dipilih : ")
    if merch == a:
        print(pilkaos_1)
    elif merch == b:
        print(pilkaos_2)
    elif merch == c:
        print(pilkaos_3)
    elif merch == d:
        print(tumblr)
    elif merch == e:
        print(ganci)
    elif merch == f:
        print(pilsweater_1)
    elif merch == g:
        print(pilsweater_2)
    elif merch == h:
        print(pilmin_1)
    elif merch == i:
        print(pilmin_2)
    elif merch == j:
        print(magnet)

    # Menampilkan total pembayaran
    total1 = int(merch)
    promo = total1 * 10 / 100
    total2 = int(total1) - promo

    if total1 >= '100.000' :
        print("Total yang harus dibayar adalah : ", total2)
    else:
        print("Total yang harus dibayar adalah : ", total1)

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
            print("Total belanja anda 5.000")
            print()
    elif yakin1=='T' or yakin1=='t':
        infokotaawal()
    else:
        print('MAAF DATA TIDAK VALID')
        print()
        sys.exit()

# info kota awal 1
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