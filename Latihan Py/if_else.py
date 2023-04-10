# nama = input('siapa nama anda : ')
# gender = int(input('jenis kelamin anda :\n 1.Cowok \n 2.Cewek \n pilih : '))
# print(nama)

# if gender == 1:
#     print('Kamu Ganteng ',nama)
# elif gender == 2:
#     print('Kamu Cantik', nama)
# else:
#     print('kayaknya kamu g punya kelamin, hmmm nama kamu ',nama)

print(17*'=')
print('KALKULATOR ONLINE')
print(17*'=')

angka1 = float(input('input angka pertama = ' ))
angka2 = float(input('input angka kedua   = ' ))
operator = input(''' Pilih Operator :
1.Tambah
2.Kurang
3.Kali
4.Bagi
''')
if operator == '1':
    hasil = angka1 + angka2
    print('Hasil Dari ',angka1, '+' ,angka2, 'adalah',hasil)
elif operator == '2':
    hasil = angka1 - angka2
    print('Hasil Dari ',angka1, '-' ,angka2, 'adalah',hasil)
elif operator == '3':
    hasil = angka1 * angka2
    print('Hasil Dari ',angka1, '*' ,angka2, 'adalah',hasil)
elif operator == '4':
    hasil = angka1 / angka2
    print('Hasil Dari ',angka1, '/' ,angka2, 'adalah',hasil)
