# def sum_int_or_str(a, b):
#     return int(a) + int(b)

# assert (sum_int_or_str(1, '2')) == 3
# assert (sum_int_or_str(2, 2)) == 4



# def get_second_charachter(a):
#     "get second charachter, if only 1 charachter return 0"
#     if len(a) > 1:
#         return a[1]
#     else:
#         return 0

# assert(get_second_charachter("ab")) == "b"
# assert(get_second_charachter("a")) == 0



# car = {
#     'brand':'Toyota',
#     'year' : 2022
# }

# assert(car['brand']) == 'Toyota'

# cars = [
#     {
#     'brand' : 'Toyota'
#     },
#     {
#     'brand' : 'Honda',
#     'product':[
#     'civic'
#     ]
#     }
# ]

# assert(cars[1]['product'][0]) == 'civic'

# raw_cars = 'toyota,honda,indiacar'
# assert(raw_cars.split(',')) == ['toyota', 'honda', 'indiacar'] #turn raw-cars into a list

# assert(raw_cars.upper().split(',')) == ['TOYOTA', 'HONDA', 'INDIACAR']

# raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'
# #step 1 split
# #step 2 casting to set, return{''}
# #setp 3 casting back to list, ['']
# raw_cars = raw_cars.split(',')
# raw_cars = set(raw_cars)
# raw_cars = len(raw_cars)

# assert(raw_cars) == 3

#------------------#

# p = int(input("Masukan Panjang Persegi Panjang : "))
# l = int(input("Masukan Lebar Persegi Panjang : "))

# luas = p * l

# print( "luas persegi panjang adalah",luas)

#-------------------#
# a = "Chandra"
# b = "Ganteng"
# print("Si",a,"Sangat",b)
# print(len(a),len(b))

# x = range(9)
# print(x)

#---------------#

# x = 1
# y = 2.8
# z = 1j

# a = float(x)
# b = int(y)
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

#------------------#
# import random
# print(random.randrange(1, 3))

#-------------------#

# b = "Halo Dunia"
# print(b[-5:-2])

#-------------------#

# a = "chandraadipraja"
# print(a.replace("chandraadipraja", "kimak"))

#-------------------#

# a = "hello world  "
# print(a.strip())

#---------------#

# a = "hello, world, dunia "
# print(a.split(","))

#---------------#

# age = 36
# txt = "My Name is John, and i am {}"
# print(txt.format(age))

#----------------#
# quantity = 3
# itemno = 567
# price = 49.95

# myorder = "I Want {} pieces of item {} for {} dollars."

# print(myorder.format(quantity,itemno,price))
#---------------#

# a = "hai semuanya kembali lagi bersama kita di acara yang lumayan megah di kota ciamis ini, salam sehat,salam donn,disini kita akan memulai roadshow pembukaan acara gameseed di kota ciamis "
# print(a.endswith("ciamis "))

#--------------#
