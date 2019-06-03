# try:
#     file = open('abc.txt', 'r')
#     print(file)
# except FileNotFoundError:
#     print('error occurred!')
#
#

# try:
#     number = float('hello')
#     print(number)
# except ValueError as e:
#     print('Not a number ' + str(e))


class BizException(Exception):
    pass

try:
    number = float('hello')
    print(number)
except ValueError as e:
    raise BizException(e)

