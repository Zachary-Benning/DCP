# Python tricks
# I will test them here first
# Then I will make flash cards to memorize
#  The hope is to commit them to memory then utilize them in my daily code base
#########################################################
## Swapping Values
a, b = 5, 10
# print(a, b)
a, b = b, a
# print(a, b)
#########################################################
#########################################################
## Create a single string from all the elements in a list
a_1 = ["Python", "is", "awsome"]
# print(a_1)
# print(" ".join(a_1))
#########################################################
#########################################################
a_2 = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
#print(a_2)
#print(max(set(a_2), key=a_2.count))
####Using collections
from collections import Counter
cnt = Counter(a_2)
#print(cnt.most_common(3))
#########################################################
#########################################################
from collections import Counter
str1 = 'hello'
str2 = 'olleh'
# if Counter(str1) == Counter(str2):
#     print("got it")

str3 = 'lhole'
str4 = 'ohlel'
# if Counter(str3) == Counter(str4):
#     print("got it")

original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*original)
#print(list(transposed))


def product(a, b):
    return a * b

def add(a, b):
    return a + b

b = True
#print((product if b else add)(5, 7))

#copying lists
# fast way to make a shallow copy
a = [1, 2, 3, 4, 5]
b = a
# both b and a will change
b[0] = 10
#print(a, b)

#only b will change
a = [1, 2, 3, 4, 5]
b = a[:]
b[0] = 10
#print(a, b)

ddd = [1, 2]
bbb = ddd.copy()
#print(bbb)
bbb[0] = 100
#print(bbb, ddd)

from copy import deepcopy
l = [[1, 2], [3, 4]]
l2 = deepcopy(l)
#print(l, l2)
l2[0][0] = 55555
#print(l, l2)

d = {'a': 1, 'b': 2}
x = d.get(1)
#print(x)

