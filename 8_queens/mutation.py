#mutation done to use mutation.mutator(genomone) ... built exclusively for n-queens problem
import numpy as np
n_queens = 8


def reverse(genome):
    final = genome[::-1]
    for x in range(n_queens):
        genome[x] = final[x]


def weave(genome):
    temp_genome = [0] * 8
    even_genome = genome[::2]
    odd_genome = genome[1::2]
    odd_counter = 0
    even_counter = 0
    for x in range(len(genome)):
        if x % 2 == 1:
            temp_genome[x] = even_genome[even_counter]
            even_counter += 1
        if x % 2 == 0:
            temp_genome[x] = odd_genome[odd_counter]
            odd_counter += 1
    final = [0] * n_queens
    for x in range(n_queens):
        final[x] = genome[temp_genome[x]]
    for x in range(n_queens):
        genome[x] = final[x]


def section_move(genome):
    # There are three cases for each ... in each of the three cases there are three subcases
    insertion_bool = False
    stop_bool = False
    insertion_point = 0
    start = 0
    stop = 0
    while not insertion_bool or not stop_bool:
        insertion_point = np.random.randint(0, 8)
        if insertion_point != start:
            insertion_bool = True
        start = np.random.randint(0, 8)
        stop = np.random.randint(0, 8)
        if start != 0 and stop != 7:
            stop_bool = True

    temp_insertion = []
    temp_remainder = []
    temp_genome = [66] * 8

    #selection of one point
    if start == stop:
        #print('onepoint')
        temp_insertion.append(start)
        for y in range(0, start):
            temp_remainder.append(y)
        for x in range(start + 1, 8):
            temp_remainder.append(x)
     ################################
        for a in range(0, 8):
            if insertion_point <= a <= insertion_point + len(temp_insertion)-1:
                #print(a, insertion_point, a-insertion_point)
                temp_genome[a] = temp_insertion[a-insertion_point]
            elif a > insertion_point + len(temp_insertion)-1:
                #print(a, len(temp_insertion)-1, a + len(temp_insertion), insertion_point)
                temp_genome[a] = temp_remainder[a-len(temp_insertion)]
            elif a < insertion_point:
                #print(a, insertion_point)
                temp_genome[a] = temp_remainder[a]

    #standard 0-7 pull out 2-4
    elif start - stop < 0:
        #print('standard_case')
        for x in range(start, stop+1):
            temp_insertion.append(x)
        for y in range(0, start):
            temp_remainder.append(y)
        for z in range(stop + 1, 8):
            temp_remainder.append(z)
            #print(len(temp_remainder), " : length of remaidner ")
        if len(temp_remainder) != 0:
            insertion_point = np.random.randint(0, len(temp_remainder))
        if len(temp_remainder) == 0:
            insertion_point = 0
    ################################
        #print(temp_remainder, temp_insertion)
        for a in range(0, 8):
            if insertion_point <= a <= insertion_point + len(temp_insertion)-1:
                #print(a, insertion_point, a-insertion_point)
                temp_genome[a] = temp_insertion[a-insertion_point]
            elif a > insertion_point + len(temp_insertion)-1:
                  ####4,  2,                         7,                 ,1
                #print(a, len(temp_insertion)-1, a + len(temp_insertion), insertion_point)
                temp_genome[a] = temp_remainder[a-len(temp_insertion)]
            elif a < insertion_point:
                if a - 2 == len(temp_remainder):
                    temp_genome = temp_genome + temp_insertion
                    break
                #print(a, insertion_point)
                #print(temp_remainder)
                temp_genome[a] = temp_remainder[a]

    #wrap around 0-7 pull out 6-2
    elif start - stop > 0:
        #print('wrap around ')
        for x in range(start, 8):
            temp_insertion.append(x)
        for y in range(0, stop+1):
            temp_insertion.append(y)
        for z in range(stop+1, start):
            temp_remainder.append(z)
        if len(temp_remainder) != 0:
            insertion_point = np.random.randint(0, len(temp_remainder))
        if len(temp_remainder) == 0:
            insertion_point = 0

        for a in range(0, 8):
            if insertion_point <= a <= insertion_point + len(temp_insertion)-1:
                #print(a, insertion_point, a-insertion_point)
                temp_genome[a] = temp_insertion[a-insertion_point]
            elif a > insertion_point + len(temp_insertion)-1:
                #print(a, len(temp_insertion)-1, a + len(temp_insertion), insertion_point)
                temp_genome[a] = temp_remainder[a-len(temp_insertion)]
            elif a < insertion_point:
                #print(a, insertion_point)
                temp_genome[a] = temp_remainder[a]
    final = [0] * n_queens
    for x in range(n_queens):
        final[x] = genome[temp_genome[x]]
    for x in range(n_queens):
        genome[x] = final[x]


def swap_multiple(genome):
    number_of_swaps = int(np.ceil(abs(np.random.normal(0.0, scale=n_queens, size=None))))
    for x in range(number_of_swaps):
        temp_swap_locations = (np.random.choice(8, 2, replace=False))
        swap_function(genome, temp_swap_locations[0], temp_swap_locations[1])


def swap_function(genome, location_a, location_b):
    swap_a = genome[location_a]
    swap_b = genome[location_b]
    genome[location_a] = swap_b
    genome[location_b] = swap_a


def mutator(genome):
    pick = np.random.randint(0, 4)
    if pick == 0:
        reverse(genome)
    if pick == 1:
        weave(genome)
    if pick == 2:
        section_move(genome)
    if pick == 3:
        swap_multiple(genome)

