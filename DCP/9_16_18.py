# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

default_list = [10, 15, 3, 7, 16, 4, 25]
checking_value = 19


def sum_two_in_list(list_x, k):
    size = len(list_x)
    # go through starting point
    for x in range(0, size):
        # go through each point past starting point
        for y in range(0, size):
            if x != y and (k == list_x[x] + list_x[y]):
                print(list_x[x], ' + ', list_x[y], ' = ', k, " True ")
                return


sum_two_in_list(default_list, checking_value)
