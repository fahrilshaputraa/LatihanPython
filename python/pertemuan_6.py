# #importing libraries
# import time
# import math

# #decorator to calculate duration 
# #taken by any function.

# def calculate_time(func):


#     def inner1(*args,**kwargs):
#         begin = time.time()

#         func(*args, **kwargs)

#         end = time.time()
#         print('Total time taken in : ',func.__name__,end - begin)

#     return inner1


# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))

# factorial(10)

import requests
from pprint import pprint

r = requests.get('https://jsonplaceholder.typicode.com/posts')
data = r.json()
pprint(data)

post = {
    'body':"LoremIpsum",
    'title':"Title",
    'userId': 5
}

req = requests.post('https://jsonplaceholder.typicode.com/posts',json=post)
print(req.json())

update_post = post
update_post['id'] = 5

req = requests.put(
    'https://jsonplaceholder.typicode.com/posts/10',json=update_post)
print(req.json())

'''
web method:
Get -> Ambil data
Post -> Buat Data di server
put/Patch -> Update data di server
Delete -> Hapus data di server
'''