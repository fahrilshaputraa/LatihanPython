# angka1 = [1,2,3,4,5]

# for i in angka1:
#     print(f'i sekarang adalah {i}')

# angka2 = range(9)

# for i in angka2:
#     print(f'sayaa ganteng')

# angka3 = 1
# while angka3 < 8:
#     angka3 +=1
#     print(f'halo kak ei')
# print('eh ada luwak, dadah kak ei')


# data_user = int(input('Mau Hitung sampai berapa?'))

# angka = 0 

# while True:
#     angka += 1
#     print(f'angka sekarang -> {angka}')

#     if angka == data_user :
#         print('udah',data_user ,'aja masbro ')
#         break

# if angka > 10 :
#     print('cape banget anj sampe',angka,' segini,hadeh')


# print('thankyou')


# segitiga for
sisi = 10
count = 1
for i in range(sisi):
    print('*'* count)
    count += 1

print('akhir dari for')
#segitiga while

count = 1
while True:
    print('*'*count)
    count += 1

    if count > sisi:
        break

print('akhir dari while')

#ganjil aja
count = 1
spadsi = int(sisi/2)
while True:
    if (count%2):
        print(''*spadsi,'+'*count)
        spadsi -= 1
        count +=1
    else:
        count += 1
        continue
    if count > sisi:
        break
while True:
    if (count%2):
        spadsi += 1
        print(''*spadsi,'+'*count)
        count -= 1
    else:
        count -= 1
    if count == 0:
        break

for i in range(0,7):
    print(''*(7,-i), end='')
    for x in range(i):
        print('+', end='')
    print()

for i in range(7,0,-1):
    print(''*(7-i),end='')
    for x in range(i):
        print('+', end='')
    print()
    
