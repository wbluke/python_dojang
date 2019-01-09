# open : get file object
file = open('hello.txt', 'w')   # w : write
file.write('Hello, world!')
file.close()


# read
file = open('hello.txt', 'r')   # r : read
s = file.read()
print(s)
file.close()


# with as : if you want to close file automatically
with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)


# write several lines
with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

        # Hello, world! 0
        # Hello, world! 1
        # Hello, world! 2


# write several lines in list
lines = ['Hi\n', 'my name is\n', 'Luke\n']
with open('hello.txt', 'w') as file:
    file.writelines(lines)

    # Hi
    # my name is
    # Luke


# read file as list
with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)    # ['Hi\n', 'my name is\n', 'Luke\n']


# read file line by line using while
with open('hello.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

        # Hi
        # my name is
        # Luke


# read file line by line using for
with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))


#pickle : save object to file
import pickle

# dump : to pickling
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

with open('james.p', 'wb') as file:     # b : binary
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)


# load : to unpickling
with open('james.p', 'rb') as file:     # b : binary
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)


