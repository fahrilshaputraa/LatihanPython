# import datetime as dt
# import math

# x = dt.datetime.now()
# print(type(x))

# print(x.year)
# print(x.strftime("%A"))

# x = dt.datetime(2020, 5, 17)
# print(x)

# print(x.strftime("%d-%m-%Y"))

# arr_1 = [5, 78, 2, 0]
# #cari nilai array besar
# assert(min(arr_1)) == 0 
# assert(max(arr_1)) == 78

# #function 5 pangkat 5
# x = pow( 5,5)
# assert(x) == 3125
# assert(math.pow(5, 5)) == 3125

#try except
# try:
#     print(y)
# except:
#     print('An Exception occured')

# try:
#     f = open("demofile.txt")
#     try:
#         f.write('Lorem Ipsum')
#     except:
#         print('Something Wrong When Writing To The File')
#     finally:
#         f.close()
# except:
#     print('Something wen Wrong When opening this file')

# try:
#     print(x)
# except:
#     print('something went wrong')
# finally:
#     print("The 'try except' is finished")

##---JSON

import json
import os

# #some JSON
# x = '{"name":"John", "Age":30, "City":"New York"}'

# #parse x:
# y = json.loads(x)

# #result is a python dictionary
# print(y["Age"])

# #python object (dict)
# x = {
#     "name":"John",
#     "Age":30,
#     "City":"New York"
# }

# #convert into JSON
# y = json.dumps(x)

# #the result is a json string
# print(y)

# f = open("demofile.txt", "w")
# f.write("\nNow Is The Monday")
# f.close()

# #open and read the file after appending
# f = open("demofile.txt")
# print(f.read())

# os.remove("demofile.txt")

# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("The File Does Not Exist")

# f = open("demofiles.txt", "x")
