# replace
a = 'Hello, world!'
a = a.replace('world', 'Python')    # Hello, Python!


# translate : alter char
# maketrans : make the change table
table = str.maketrans('aeiou', '12345')
'apple'.translate(table)    # 1ppl2


# split
b = 'apple pear grape orange'.split()
print(b)    # ['apple', 'pear', 'grape', 'orange']


# join : connect list elements to string
'-'.join(['apple', 'pear', 'grape', 'orange'])   # apple-pear-grape-orange


# upper, lower
'python'.upper()    # PYTHON
'PYTHON'.lower()    # python


# delete left or right, or both spaces
'   Python   '.lstrip()     # 'Python   '
'   Python   '.rstrip()     # '   Python'
'   Python   '.strip()      # 'Python'

# it can delete specified char
', Python.'.strip(',.')         # ' Python'

# string.punctiation have all punctuation mark.
import string
',^_ Python.%~!'.strip(string.punctuation)  # ' Python'


# line up with length
'python'.ljust(10)  # 'python    '
'python'.rjust(10)  # '    python'
'python'.center(10)  # '  python  '


# method chaining
'python'.rjust(10).upper()  # '    PYTHON'


# fill zero
'35'.zfill(4)   # '0035'
'3.5'.zfill(6)   # '0003.5'
'hello'.zfill(10)   # '00000hello'


# find
'apple pineapple'.find('pl')    # 2
'apple pineapple'.find('xy')    # -1

'apple pineapple'.rfind('pl')    # 12

'apple pineapple'.index('pl')    # 2

'apple pineapple'.rindex('pl')    # 12


# count
'apple pineapple'.count('pl')    # 2



# =======================================================
# string formatting


# format specifier
'I am %s.' % 'james'                # I am james.
'Today is %d %s.' % (3, 'April')    # Today is 3 April.

# %d : decimal integer
# %f : fixed point
# %10s  : secure 10 space and line up right side
# %-10s : secure 10 space and line up left side


# format method
'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)    # 'Hello, Python 3.6 Script'

'Hello, {language} {version}'.format(language='Python', version=3.6)    # 'Hello, Python 3.6'

# simple
language = 'Python'
version = 3.6
'Hello, {language} {version}'   # 'Hello, Python 3.6'


# align with format()
'{0:<10}'.format('python')  # 'python    '

# ':<'  : left
# ':>'  : right


# align with zero
'{0:03d}'.format(35)    # '035'




















