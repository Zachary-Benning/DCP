#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and
# 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.


def largest_sum_of_nonadjacent(set_of_integers):
    count_even = 0
    count_odd = 0
    for x in range(0, len(set_of_integers)):
        if x % 2 == 0:
            count_even += set_of_integers[x]
        else:
            count_odd += set_of_integers[x]
    return count_even if count_even >= count_odd else count_odd


print(largest_sum_of_nonadjacent([-1,-2,3,-5,-4,17,23]))
