# need to have a memory for the 92 solutions,
#there are only 92 solutions, took chess masters 2 years ... the entire community
#find 1 correct board configuration


import numpy as np
import random as rd
from collections import Counter
n_queens = 8
population_size = 100


def diagonal_check(z):
    internal_count = 0
    for x in range(0, 8):
        for y in range(0, 8):
            if abs(z[x] - z[y]) == abs(x - y) and x != y:
                internal_count += 1
    return internal_count


def row_check(z):
    internal_count = 0
    a = Counter(z)
    for x in range(0, 8):
        if a[x] > 1:
            internal_count += a[x] * (a[x] - 1)
    return internal_count


def create_population(size_of_population, is_permutation):
    if is_permutation == 1:
        #print(" Inputed 1 ")
        a = [[rd.randint(0, n_queens - 1) for i in range(n_queens)] for y in range(size_of_population)]
        return a
    elif is_permutation == 0:
        #print(" INPUTED 0")
        a = [rd.sample(range(0, 8), 8) for y in range(size_of_population)]
        return a


def fitness(individual): return row_check(individual) + diagonal_check(individual)


def print_population(size_of_population, population):
    for beta in range(0, size_of_population):
        print('{:>3}'.format(beta + 1), " individual: ", population[beta], ' - ',
              '{:>2}'.format(fitness(population[beta])))


def one_pt_cross_over(first_individual, second_individual):
    cross_point = np.random.randint(1, n_queens - 1)
    first_temp = [55] * cross_point
    second_temp = []
    off_spring = [55] * n_queens
    #print(cross_point)
    for x in range(n_queens):
        if x < cross_point:
            first_temp[x] = first_individual[x]

    for x in range(n_queens):
        count = 0
        for y in range(cross_point):
            if second_individual[(x+cross_point) % 8] == first_temp[y]:
                count += 1
            if count == 0 and y == cross_point-1:
                second_temp.append(second_individual[(x+cross_point) % 8])

    for x in range(n_queens):
        if x < cross_point:
            off_spring[x] = first_temp[x]
        if x >= cross_point:
            off_spring[x] = second_temp[x-cross_point]
    return off_spring


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


def find_second_value(input_value, input_location, score):
    input_scorez = input_value
    for y in range(0, 40):
        for x in range(0, population_size):
            if score[x] == input_scorez and x != input_location:
                return input_scorez
        input_scorez += 1


def selection(population_size, population):
    score = np.zeros(population_size, int)
    for x in range(0, population_size):
        score[x] = fitness(population[x])
    a = min(enumerate(score), key=(lambda x: x[1]))
    best_value_location = a[0]


    number_one = a[0]
    number_two = 0

    solution = find_second_value(a[1], a[0], score)
    zztop = np.where(score == solution)
    if len(zztop[0]) > 1:
        number_two = zztop[0][1]
    else:
        number_two = zztop[0][0]


    return score, number_one, number_two


def weakest_link(score):
    for x in range(len(score)):
        maxy = max(score)
        location_maxy = 0
        if score[x] == maxy:
            location_maxy = x
            break
    return location_maxy


def create_child(individual_one, individual_two):
    temp_child = one_pt_cross_over(individual_one, individual_two)
    mutator(temp_child)
    return temp_child


#score, number_one, number_two = selection(population_size, population)
#weak = weakest_link(score)
#print('number one -> ', number_one, number_two)
#print(score, ' scores ')
#print(population)
#print('weak locatoin: ', weak)
#print('best ', population[number_one], score[number_one])
#child = create_child(population[number_one], population[number_two])
#print('child', child)

# del population[weak]
# population.append(child)

def evolve(population):
    score, number_one, number_two = selection(population_size, population)
    weak = weakest_link(score)
    child = create_child(population[number_one], population[number_two])
    del population[weak]
    population.append(child)
    return population


def magic():
    population = create_population(population_size, 0)
    for x in range(10000):
        population = evolve(population)
        if x % 1000 == 0:
            print(x)
            scory, one, two = selection(population_size, population)
            if scory[one] == 0:
                print('perfect solution found @ ', x)
                print(population[one])
                break

for x in range(10):
    magic()

# scory, one, two = selection(population_size, population)
# print(scory[one], population[one])
