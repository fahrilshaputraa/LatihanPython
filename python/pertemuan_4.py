# import datetime as dt

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_my_name(self):
#         print('Hello my name is ' + self.name)

# person_1 = Person("John", 35)
# print(person_1.name)
# print(person_1.age)
# print(person_1.say_my_name())


# class Mathematic:

#     def __init__(self) :
#         self.value = 0
        
#     def increment(self) :
#         self.value =+ 2

#     def decrement(self) :
#         self.value -= 2

#     def add(self, a, b):
#         return a + b
    
#     def substraction(self, a, b):
#         return a - b
    
#     def multiply(self, a, b):
#         return a * b
    
# math = Mathematic()

# print(math.add(1,2))
# print(math.substraction(5, 1))
# print(math.multiply(5, 2))
# print(dt.datetime.now())

class car:
    def __init__(self, brand, year,):
        self.b = brand
        self.y = year

        self.pintu = "tutup"
        self.mobil = "mati"

    def openDoor(self):
        if self.pintu == 'tutup':
            print('Door Opened')
            self.pintu = 'Buka'
        else:
            print('Door Closed')
    def closeDoor(self):
        if self.pintu == 'Buka':
            print('Door Closed')
            self.pintu = 'tutup'
        else:
            print('Door Opened')
    def turnOn(self):
        if self.mobil == 'mati':
            print('Mobil Menyala')
            self.mobil = 'nyala'
        else:
            print('Mobil Mati')
    def turnOff(self):
        if self.mobil == 'nyala':
            print('Mobil mati')
            self.mobil = 'mati'
        else:
            print('Mobil Menyala')
car1 = car('Civic', 1998)
car1.openDoor()
car1.closeDoor()
car1.turnOn()
car1.turnOff()
        