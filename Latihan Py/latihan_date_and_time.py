#date and time (latihan)

import datetime as dt
print ("\nMasukan tanggal, \nbulan dan tahun lahir anda! \n")

tanggal = int(input("Tanggal \t: "))
bulan   = int(input("Bulan \t\t: "))
tahun   = int(input("Tahun \t\t: "))

detail_lahir = dt.date(tahun, bulan, tanggal)
hari = (f"Dihari {detail_lahir:%A}")
print("Kamu Lahir Pada : ", detail_lahir,'\n',hari)

hari_ini = dt.date.today()
print("Hari ini tanngal : ",hari_ini)
umur_hari = hari_ini - detail_lahir
umur_tahun = umur_hari.days // 365
print(f'umur anda adalah : ',umur_tahun,'tahun')

