# if you want to use several line strings
a = """Hello, world!
안녕하세요
It's Python! """


# list
b = [0, 1, 2]
b = list(range(3))
print(b) # [0, 1, 2]


# range
c = range(0, 10, 3)
print(list(c)) # [0, 3, 6, 9]


# tuple : cannot change values(read only)
d = (0, 1, 2)


# "value" (not) in sequence
print(0 in d) # True
print(1 not in d) # False


# sequence can be repeated by multiplying integer
print(d * 3) # (0, 1, 2, 0, 1, 2, 0, 1, 2)


# sequence can be accessed by negative integer
print(d[-1]) # 2
print(d[-2:3]) # (1, 2)


# slice
e = [0, 1, 2, 3, 4]
print(e[:2]) # [0, 1]
print(e[2:]) # [2, 3, 4]
print(e[::2]) # [0, 2, 4]


# dictionary
f = {'num1':3, 'num2':4, 'num3':5}
print(f['num2']) # 4
print('num2' not in f) # False


# make dictionary
g = dict(key1='value1', key2='value2')
print(g) # {'key1': 'value1', 'key2': 'value2'}


# dictionary can be made by two lists(tuples)
h = ['one', 'two', 'three']
i = [1, 2, 3]
j = dict(zip(h, i))
print(j) # {'one': 1, 'two': 2, 'three': 3}


# dictionary can be made by tuples formed (key, value)
k = dict([('key1', 100), ('key2', 200)])
print(k) # {'key1': 100, 'key2': 200}
