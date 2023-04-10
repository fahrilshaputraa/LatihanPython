def persegi():
    a = int(input('Masukan Sisi : '))
    c = int(input('1.Cari Luas atau 2.Cari Keliling : '))
    l = a * a
    k = 4 * a
    if c == 1:
        print('Luas Persegi Panjang : ',l)
    elif c == 2:
        print('Keliling Persegi Panjang : ',k)
    else:
        'Masukan Pilihan Yang Sesuai'

def persegiPanjang():
    a = int(input('Masukan Panjang : '))
    b = int(input('Masukan Lebar : '))
    c = int(input('1.Cari Luas atau 2.Cari Keliling : '))
    l = a * b
    k = (2*a) + (2*b)
    if c == 1:
        print('Luas Persegi Panjang : ',l)
    elif c == 2:
        print('Keliling Persegi Panjang : ',k)
    else:
        'Masukan Pilihan Yang Sesuai'

def segitiga():
    print("Menghitung Luas Segitiga")
    a = float(input('Masukan Alas   : '))
    t = float(input('MAsukan Tinggi : '))
    l = (0.5 * a) * t
    print('Luas Segitiga Dari Alas ',a,'\nDan Tinggi',t,'\nAdalah',l)

def lingkaran():
    a = float(input('Masukan Jari-Jari : '))
    l = 3.14 * a * a
    print('Luas Lingkaran Adalah : ',l)

jawab = 'ya'
while(jawab == 'ya'):
    print(25*'=')
    print('Selamat Datang Di Aplikasi Bangun Datar')
    print(25*'=')
    print('Beberapa Bangun Datar Yang Tersedia : ')
    print('''
    1.Persegi
    2.Persegi Panjang
    3.Segitiga
    4.Lingkaran
''')
    try:
        pilihan = int(input('Pilih Bangun Datar : '))
        if pilihan == 1:
            persegi()
        elif pilihan == 2:
            persegiPanjang()
        elif pilihan == 3:
            segitiga()
        elif pilihan == 4:
            lingkaran()
        else:
            print('Angka Tidak Terdaftar')
    except ValueError:
        print('Masukan Dengan Menginputkan Angka Bukan Teks!')
    ulang = input('Ulangi Lagi?"Ya" atau "Tidak" : ')
    if ulang == 'tidak':
        print('Makasih Sudah Menggunakan Program Saya')
        break
