# def times(a, b):
#     print(a*b)
#
# times(5,6)

def cube(number):
    return number**3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

def main():
    result = by_three(3)
    print(result)

main()