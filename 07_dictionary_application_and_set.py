# setdefault : append key to dictionary with default value
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')       # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None}
x.setdefault('f', 100)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None, 'f': 100}


# update
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90)          # {'a': 90, 'b': 20, 'c': 30, 'd': 40}
x.update(e=50)          # {'a': 90, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
x.update(a=900, f=60)   # {'a': 900, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

# if key is number
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})    # {1: 'ONE', 2: 'two', 3: 'THREE'}

# use list or tuple
y.update([[2, 'TWO'], [4, 'FOUR']])     # {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR'}

# use object can be iterated
y.update(zip([1, 2], ['one', 'two']))   # {1: 'one', 2: 'two', 3: 'THREE', 4: 'FOUR'}



# delete key
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')  # 10
x           # {'b': 20, 'c': 30, 'd': 40}

# if there is not specific key
x.pop('z', 0)   # 0 : pop('key', 'default') set default value

# del
del x['b']


# popitem : del last key-value and return it by tuple
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()     # ('d', 40)


# clear() : del all key-values
x.clear()   # {}


# get() : take key
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.get('a')      # 10
x.get('z', 0)   # 0


# items() : take all key-values
# keys() : take all keys
# values() : take all values


# make dictionary from list or tuple
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)         # {'a': None, 'b': None, 'c': None, 'd': None}
y = dict.fromkeys(keys, 100)    # {'a': 100, 'b': 100, 'c': 100, 'd': 100}


# print all key-values
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)
# a 10
# b 20
# c 30
# d 40

# can use keys() and values() also


# make dictionary with dictionary comprehension
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
# {'a': None, 'b': None, 'c': None, 'd': None}

# just keys :
# {key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}

# take values and use them to keys :
# {value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()}

# change keys and values :
# {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}


# if delete specific value : not next method
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
#
# for key, value in x.items():
#     if value == 20:
#         del x[key]

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
# {'a': 10, 'c': 30, 'd': 40}



# =============================================================

# set : unordered
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}


# check value
'orange' in fruits      # True
'orange' not in fruits  # False


# make set
a = set('apple')    # {'e', 'l', 'a', 'p'}
b = set(range(5))   # {0, 1, 2, 3, 4}
c = set()           # empty set
                    # {} : This is not a set! it's dictionary


# set operation
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# set.union(a, b)
a | b       # {1, 2, 3, 4, 5, 6}

# set.intersection(a, b)
a & b       # {3, 4}

# set.difference(a, b)
a - b       # {1, 2}

# set.symmetric_difference(a, b)
a ^ b       # {1, 2, 5, 6}


# operate and update
# a.update(b)
a != {5}

# a.intersection_update(b)
a &= b

# a.difference_update(b)
a -= b

# a.symmetric_difference_update(b)
a ^= b


# subset
# a.issubset(b)
a <= {1, 2}

# < : proper subset

# a.superset(b)
a >= {1, 2}

# > : proper superset


# disjoint
# a.disjoint(b)


# handling set
a = {1, 2, 3, 4}
a.add(5)        # {1, 2, 3, 4, 5}

a.remove(3)     # {1, 2, 4, 5}, if there is not value, error.
a.discard(3)    # discard is same and do not occur error

a.pop()         # remove random value

a.clear()       # clear all values

len(a)          # count values (length)


# copy
a = {1, 2, 3, 4}
b = a.copy()


# set comprehension
a = {i for i in 'pineapple' if i not in 'apl'}  # {'e', 'i', 'n'}




