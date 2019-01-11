# class
class Person:
    def greeting(self):
        print('Hello')

james = Person()
james.greeting()    # Hello


# class attribute
class Person:
    def __init__(self):
        self.hello = '안녕하세요.'

    def greeting(self):
        print(self.hello)


james = Person()
james.greeting()    # Hello


# class init attribute
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))


maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()  # 안녕하세요. 저는 마리아입니다.

print('이름:', maria.name)  # 마리아
print('나이:', maria.age)  # 20
print('주소:', maria.address)  # 서울시 서초구 반포동


# private attribute
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # private : __attribute

    def pay(self, amount):
        self.__wallet -= amount  # private attribute can be accessed with inner method
        print('이제 {0}원 남았네요.'.format(self.__wallet))


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# maria.__wallet -= 10000  ---> error
maria.pay(3000)     # 이제 7000원 남았네요.


# =========================================================

# instance attribute (__init__) - independent by instance
# class attribute - common thing
class Person:
    bag = []       # class attribute

    def put_bag(self, stuff):
        Person.bag.append(stuff)    # it's clear using class' name than using 'self'


james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)    # ['책', '열쇠']
print(maria.bag)    # ['책', '열쇠']


# static method : for pure function
class Calc:
    @staticmethod   # decorator
    def add(a, b):  # not setting 'self'
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)


Calc.add(10, 20)  # call the method directly from class
Calc.mul(10, 20)


# class method
class Person:
    count = 0  # class attribute

    def __init__(self):
        Person.count += 1  # when instance is created

    @classmethod    # decorator
    def print_count(cls):   # set cls
        print('{0}명 생성되었습니다.'.format(cls.count))  # access to class using cls


james = Person()
maria = Person()

Person.print_count()  # 2명 생성되었습니다.


# =======================================================

# class inheritance
class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):  # subclass(superclass)
    def study(self):
        print('공부하기')


james = Student()
james.greeting()    # 안녕하세요.
james.study()       # 공부하기


# To use attribute in superclass
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()  # super(). : call __init__ method in superclass
        self.school = '파이썬 코딩 도장'


james = Student()
print(james.school)
print(james.hello)

# Student __init__
# Person __init__
# 파이썬 코딩 도장
# 안녕하세요.


# overriding
class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def greeting(self):
        super().greeting()  # to reduce repetition
        print('저는 파이썬 코딩 도장 학생입니다.')


james = Student()
james.greeting()


# multiple inheritance
class Person:
    def greeting(self):
        print('안녕하세요.')


class University:
    def manage_credit(self):
        print('학점 관리')


class Undergraduate(Person, University):    # multiple inheritance
    def study(self):
        print('공부하기')


james = Undergraduate()
james.greeting()        # 안녕하세요.
james.manage_credit()   # 학점 관리
james.study()           # 공부하기


# abstract class
from abc import *   # abc : abstract base class


class StudentBase(metaclass=ABCMeta):   # metaclass=ABCMeta
    @abstractmethod     # decorator
    def study(self):
        pass            # must empty

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')


james = Student()
james.study()
james.go_to_school()

