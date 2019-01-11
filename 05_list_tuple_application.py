a = [10, 20]


# append an element in list (tuple X)
a.append(30)    # [10, 20, 30]


# you can append a list in the list
a.append([[400, 500]])  # [10, 20, 30, [400, 500]]
                        # len(a) = 4 (not 5)


# if elements to append are many, use extend. (tuple X)
a.extend([600, 700])    # [10, 20, 30, [400, 500], 600, 700]
                        # the appended element is not a list


# if you want to append an element on specific index (tuple X)
a.insert(2, 100)        # [10, 20, 100, 30, [400, 500], 600, 700]


# usually
# 1. insert(0, element)             # append to first index
# 2. insert(len('list'), element)   # append to last index
# 3. a[1:1] = [500, 600]            # extend several elements to specific index


# ===========================================

# pop : delete (last) element (tuple X)
a.pop()     # 700
a.pop(4)    # [400, 500]
a           # [10, 20, 100, 30, 600]


# delete specific data (tuple X)
a.remove(100)   # [10, 20, 30, 600]


# ===========================================

b = [10, 20, 10, 30]


# take index (tuple O)
b.index(20)      # 1


# count data (tuple O)
b.count(10)     # 2


# reverse elements
b.reverse()     # [30, 10, 20, 10]


# sort
b.sort()        # [10, 10, 20, 30]
                # sorted(b) : generate new sorted list


# clear all elements
a.clear()       # a == []


# ===========================================

a = [10, 20, 30]
b = a           # This is not a copy
a is b          # True

b = a.copy()    # This is a correct copy
a is b          # False
a == b          # True


# ===========================================

# enumerate : print elements in list with index
a = [10, 20, 30, 40, 50]
for index, value in enumerate(a):   # index : 0 ~ 4
    print(index, value)


for index, value in enumerate(a, start=1):   # index : 1 ~ 5
    print(index, value)


# ===========================================

# list comprehension
a = [i for i in range(5)]      # [0, 1, 2, 3, 4]
b = [i * 2 for i in range(5)]      # [0, 2, 4, 6, 8]

c = [i for i in range(5) if i % 2 == 0]      # [0, 2, 4]


# tuple
a = tuple(i for i in range(5) if i % 2 == 0)    # (0, 2, 4, 6, 8)
# not this : (i for i in range(5) if i % 2 == 0)
            # => generator comprehension

# ===========================================

# map & list
# => list(map('function', 'list'))
a = [1.1, 2.2, 3.3, 4.4]
a = list(map(int, a))           # [1, 2, 3, 4]

b = list(map(str, range(5)))    # ['0', '1', '2', '3', '4']


# ===========================================

# make jagged list
a = [3, 1, 3, 2, 5]  # width size
b = []  # make empty list

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)

print(b)    # [[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]]

# it can be constructed by list comprehension : a = [[0] * i for i in [3, 1, 3, 2, 5]]


# ===========================================

# deepcopy : to copy multiArray
a = [[10, 20], [30, 40]]
import copy
b = copy.deepcopy(a)


