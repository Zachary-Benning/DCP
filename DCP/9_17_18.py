# Given an array of integers, return a new array such that each element at index i of the new
# array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?
import numpy as np

print("[  1,  2,  3,  4,  5] :: initial")
print("[120, 60, 40, 30, 24] :: expected")
list_integer = [1, 2, 3, 4, 5]
length = len(list_integer)
new_list = np.zeros(length, dtype=np.int)
print(list_integer)

for x in range(0, length):
    buffer = 1
    for y in range(0, length):
        if x != y:
            buffer *= list_integer[y]
    new_list[x] = buffer

print(new_list)
