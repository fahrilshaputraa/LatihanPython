# range

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:3])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana"]
# thislist.append('mango')
# print(thislist)

# thislist = ["apple", "banana"]
# thislist.insert( 0,'mango')
# print(thislist)

# thislist = ["apple", "banana"]
# thislist2 = ["mango"]

# thislist.extend(thislist2)
# print(thislist)


#remove
# thislist = ["apple", "banana"]
# thislist.remove('apple')
# print(thislist)

# thislist = ["apple", "banana"]
# thislist.remove('apple') #step1
# thislist.pop(0) #step2
# print(thislist)

# thislist = ["apple", "banana"]
# thislist.clear()
# print(thislist)

#looplist
# thislist = ["apple", "banana"]
# for x in thislist:
#     print(x)

# thislist = ["apple", "banana", "mango"]
# a = thislist
# a.pop(1)

# assert(thislist) == ["apple", "mango"]

# b = thislist
# b.insert(2,"kiwi")
# assert(b) == ["apple", "mango", "kiwi"]

# new_list = ["apple", "apple", "apple" "apple", "mango", "kiwi", "apple", "apple" "apple" "apple"]

# assert() == ["mango", "kiwi"]

# new_list = ["apple", "apple", "apple", "apple", "mango", "kiwi", "apple", "apple", "mango", "kiwi", "apple", "apple"]

# assert([x for x in new_list if x != "apple"]) == ["mango", "kiwi", "mango", "kiwi"]


# list sort reverse reverse=true 
# list1 = ["mango"]
# list2 = ["banana"]

# list1.extend(list2)
# # list1 += list2
# print(list1)

# list1 = [1, 8, 3, 5, 6, 4, 7]
# list1.sort(reverse=True)  
# print(list1)



# list1 = [1, 4, 5, 6, 2, 4]

# assert([x for x in list1 if x != 4]) == [1, 5, 6, 2 ]
# # assert([x for x in list1 if x = 4]) == [4, 4]

# list1 = [1, 4, 5, 6 ,2, 4]
# list2 = list1.copy()
# list2.pop()

# print(list1, list2)

# list1 = [1, 4, 5, 7]

# list3 = list1.copy()
# list3.pop()

# assert(list3) == [1, 4, 5]
# assert(list1) == list1






#tuple
# fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')

# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# cars = {
#     'brand' : 'honda',
#     'product' : 'civic'
# }

# print(cars['brand'])

# print(cars.keys())

# for key in cars.keys():
#     print(cars[key])

# cars = {
#     'brand' : 'honda',
#     'product' : 'civic'
# }

# product = None

# assert(list(cars.keys())[1]) == 'product'

# print(cars.values())

# print(cars.get('year', None))
# print('tidak akan dijalankan')

# if 'year' in cars:
#     print(cars['year'])

# cars.update(
#     {
#         'year' : 2021
#     }
# )

# print(cars)

#FUNCTION
# def my_function(fname, lname):
#     print(fname +" "+ lname)

# my_function("Enil", "refsnes")
# my_function("Tobias", "refsnes")
# my_function("Linus", "refsnes")

# def my_function(*kids):
#     print(kids)
#     for kid in kids:
#         print(kid)

# my_function("Emil", "Tovias")

# def my_function(child1, child2):
#     print(child2)

# my_function(child2="Emil", child1="Tobias")

# def full_name(fname, lname):
#     print(fname + " " + lname)

# full_name(lname= "tobias", fname = "emil")

#**

# def full_name(**fullname):
#     print(fullname)

# full_name(nama_depan="emil", nama_belakang="tobias", umur=20, status="bekerja")

# full_name(nama_depan="chandra")

#default value
# def upper_case_country(country = "Norway"):
#     print(country.upper())

# upper_case_country("swiss")


def multiply_by_two(free):
    return (2 * free)

assert(multiply_by_two(3)) == 6

# def multiply_by_x(w, x = 2):
#     "if x not passed, then define the default value to 2"
#     return w + x

# assert(multiply_by_x(3)) == 6
# assert(multiply_by_x(3, 1)) == 3

# user_input = input("Isi User : ")
# print(multiply_by_two(int(user_input)))

how_many_input = input("Berapa kali input data? : ")
i = 0 

# while i < int(how_many_input):
#     user_input = input('input dikali dengan 2 : ')
#     print(multiply_by_two(int(user_input)))
#     i+= 1

while True:
    if i == 0 :
        break
        user_input = input('input dikali dengan 2 : ')
        print(multiply_by_two(int(user_input)))
        i+= 1
