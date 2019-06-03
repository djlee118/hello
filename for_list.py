colors = ['red', 'yellow', 'blue', 'green', 'orange']

# for item in colors:
#     print(item)

wish_travel_city = {
    'bangkok': 'Thai',
    'LA': 'USA',
    'manila': 'Philippines'
}

# for key in wish_travel_city.keys():
#     print(wish_travel_city[key])

# for value in wish_travel_city.values():
#     print(value)

# for key, value in wish_travel_city.items():
#     print(key+': ' + value)

# addresses_new = {
#     '1': {'name': 'hong kildong', 'email': 'hong@mail.com', 'hp_num': '010-222-3333'},
#     '2': {'name': 'lee soonsin', 'email': 'lee@mail.com', 'hp_num': '010-222-3333'},
#     '3': {'name': 'jang youngsil', 'email': 'jan@mail.com', 'hp_num': '010-222-3333'},
#     '4': {'name': 'king sejong', 'email': 'king@mail.com', 'hp_num': '010-222-3333'}
# }
#
# for key in addresses_new:
#     my_dict = addresses_new[key]
#     print(my_dict)


#random module
import random

# for i in range(10):
#     print(random.randint(1, 6))

# num = {
#     '1': 0,
#     '2': 0,
#     '3': 0,
#     '4': 0,
#     '5': 0,
#     '6': 0
# }
# for i in range(10000):
#     rand_num = random.randint(1, 6)
#     num[str(rand_num)] = num[str(rand_num)] + 1
#
# print(num)
# sum = 0
# for value in num.values():
#     print('sum[' + str(sum) + '] value[' + str(value) + ']')
#     sum = sum + value
#
# print(sum)

num = {}

for i in range(10000):
    rand_num = random.randint(1,6)
    num[rand_num] = num.setdefault(rand_num,0) + 1

print(num)



