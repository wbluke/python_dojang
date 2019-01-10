# function
def add(a, b):
    return a + b


# it can return several values
def add_sub(a, b):
    return a + b, a - b


# unpacking
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


x = [10, 20, 30]
print_numbers(*x)   # print_numbers(10, 20, 30)


# variable argument : not determined argument's number
def print_numbers(*args):
    for arg in args:
        print(arg)


# keyword argument
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')    # don't need order


# dictionary unpacking
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)  # *x : keys


# variable argument using keyword argument
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')


x = {'name': '홍길동'}
personal_info(**x)  # name: 홍길동


# initial value
def personal_info(name, age, address='비공개'):    # argument with initial value must be located at last position
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


personal_info('홍길동', 30)
# 이름:  홍길동
# 나이:  30
# 주소:  비공개


# ====================================================

# make function with lambda comprehension
plus_ten = lambda x: x + 10
plus_ten(1)


# lambda & map
list(map(lambda x: x + 10, [1, 2, 3]))  # [11, 12, 13]


# lambda & if : 'else' is necessary
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a)) # [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]


# map with several objects
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
list(map(lambda x, y: x * y, a, b)) # [2, 8, 18, 32, 50]


# filter
def f(x):
    return x > 5 and x < 10


a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(f, a))  # [8, 7, 9]
list(filter(lambda x: x > 5 and x < 10, a)) # [8, 7, 9]


# reduce
def f(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
from functools import reduce
reduce(f, a)    # 15
reduce(lambda x, y: x + y, a)   # 15


# ======================================================

# closure : maintaining local variables or code etc., we use it when we need the function.
def calc():
    a = 3
    b = 5

    def mul_add(x):
        return a * x + b
    return mul_add


c = calc()  # closure
print(c(1), c(2), c(3), c(4), c(5)) # 8 11 14 17 20


# nonlocal
def calc():
    a = 3
    b = 5
    total = 0

    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)

    return mul_add


c = calc()
c(1)    # 8
c(2)    # 19
c(3)    # 33

