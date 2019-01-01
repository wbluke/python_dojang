# if you divide integer by integer, result is float.
num = 4 / 2
print(num) # 2.0


# convert float to int(int to float)
num = int(4/2)
print(num) # 2
num = float(1+3)
print(num) # 4.0


# delete variable
del num


# if you want to know class' type
print(type(3.3)) # <class 'float'>


# when save input data on variable
s = input() # string type
a = int(input()) # integer type


# several inputs
b, c = input().split() # two string types
b, c = map(int, input().split()) # two int types by using map()


# control print method
# sep : seperate character
print(1, 2, 3, sep=', ') # 1, 2, 3


# end : end character
print(1, end=' ')
print(2) # 1 2

