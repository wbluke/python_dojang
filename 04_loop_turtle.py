# for_range
for i in range(5):
    print('Hello, world!')


# if you want to reverse numbers in range
for i in reversed(range(5)):
    print('Hello, world!', i)


# list, tuple, string can also
fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in reversed('Python'):
    print(letter, end=' ') # n o h t y P


print()
print('============================')


# while
i = 1
while i <= 5:
    print('Hello, world!', i)
    i += 1


# random_while
import random
print(random.random()) # random float
i = 0
while i != 3:   # until appear 3
    i = random.randint(1, 6)    # random integer between 1 and 6
    print(i)


# continue_break
i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
    if i == 11:
        break
# 1 3 5 7 9 11


# turtle graphics
import turtle as t
t.shape('turtle')
t.fd(100)   # forward
t.rt(90)    # right
t.bk(100)   # backward
t.lt(90)    # left


t.reset()   # reset turtle and lines


# when you want to color on figure
t.color('red')          # pen color
t.begin_fill()          # begin to color
n = 6
for i in range(n):
    t.forward(100)
    t.right(360 / n)
t.end_fill()            # end to color


t.reset()   # reset turtle and lines


# when drawing several circles
n = 60
t.speed('fastest')      # maximize turtle's speed
for i in range(n):
    t.circle(120)       # radius = 120
    t.right(360 / n)


t.reset()   # reset turtle and lines


# when drawing complex lines
t.speed('fastest')
for i in range(300):
    t.forward(i)        # The line becomes longer
    t.right(91)


t.mainloop()    # to maintain turtle window