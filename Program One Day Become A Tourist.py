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
