# import json

# # Python dictionary
# jsn = {
#     'name' : 'lasesa',
#     'number' : '234669890',
#     'country' : 'india',
#     'state ' : 'guj'
#     }

# # Serialize to JSON  Python objects into JSON format
# pyjsn = json.dumps(jsn)
# print(pyjsn)
# {"name": "lasesa", "number": "234669890", "country": "india", "state ": "guj"}

# # Deserialize from JSON   JSON back into Python objects
# jsnpy = json.loads(pyjsn)
# print(jsnpy)
# {'name': 'lasesa', 'number': '234669890', 'country': 'india', 'state ': 'guj'}


from functools import partial

# def multiply(x, y):
#         return x * y

# # create a new function that multiplies by 2
# dbl = partial(multiply, 5)
# print(dbl(4))


# def func(u, v, w, x):
#     return u*4 + v*3 + w*2 + x

# par = partial(func,5,6,7)
# print(par(8))

help(list)
