import numpy as np
import random as rd
from collections import Counter

n_queens = 8
population_size = 100
generation_limit = 30
# representation 0 :: Simple Permutations
# representation 1 :: Simple Combinations
representation_type = 0


def create_population(size_of_population, representation_type):
    if representation_type == 1:
        a = [[rd.randint(0, n_queens - 1) for i in range(n_queens)] for y in range(size_of_population)]
        return a
    elif representation_type == 0:
        a = [rd.sample(range(0, 8), 8) for y in range(size_of_population)]
        return a


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


def fitness(individual): return row_check(individual) + diagonal_check(individual)


def find_second_value(input_value, input_location, score):
    input_scorez = input_value
    for y in range(0, 40):
        for x in range(0, 4):
            # end bound was population size ## 5 doesnt work not sure why ### addres this at a later time
            if score[x] == input_scorez and x != input_location:
                return input_scorez
        input_scorez += 1


def pick_top_two(population, population_size):
    score = np.zeros(population_size, int)
    for x in range(0, population_size):
        score[x] = fitness(population[x])
    a = min(enumerate(score), key=(lambda x: x[1]))
    number_one = a[0]
    solution = find_second_value(a[1], a[0], score)
    zztop = np.where(score == solution)
    if len(zztop[0]) > 1:
        number_two = zztop[0][1]
    else:
        number_two = zztop[0][0]
    return score, number_one, number_two


def selection(population, population_size, tournament_type):
    if tournament_type == 0:
        return tournament_style_top_x(population, population_size, 5)


def tournament_style_top_x(population, population_size, x):
    random_x = rd.sample(range(0, population_size), x)
    top_x = [0] * x
    for x in range(x):
        top_x[x] = population[random_x[x]]
    score, top_one, top_two = pick_top_two(top_x, x)
    return top_x[top_one], top_x[top_two]

def swap_function(genome_to_swap, location_a, location_b):
    swap_a = genome_to_swap[location_a]
    swap_b = genome_to_swap[location_b]
    genome_to_swap[location_a] = swap_b
    genome_to_swap[location_b] = swap_a
    return genome_to_swap


def weave(genome_to_weave):
    temp_genome = [0] * 8
    even_genome = genome_to_weave[::2]
    odd_genome = genome_to_weave[1::2]
    odd_counter = 0
    even_counter = 0
    for x in range(len(genome_to_weave)):
        if x % 2 == 1:
            temp_genome[x] = even_genome[even_counter]
            even_counter += 1
        if x % 2 == 0:
            temp_genome[x] = odd_genome[odd_counter]
            odd_counter += 1
    return temp_genome


def mutator(genome_to_mutate):
    extra_mutation_present = 1 if rd.uniform(0, 100) <= 12.5 else 0
    two_random_locations = rd.sample(range(0, 7), 2)
    if extra_mutation_present:
        return weave(swap_function(genome_to_mutate, two_random_locations[0], two_random_locations[1]))
    else:
        return swap_function(genome_to_mutate, two_random_locations[0], two_random_locations[1])


def cut_cross_fill(male, female):
    cross_point = np.random.randint(1, n_queens - 1)
    first_temp = [55] * cross_point
    second_temp = []
    off_spring = [55] * n_queens
    for x in range(n_queens):
        if x < cross_point:
            first_temp[x] = male[x]
    for x in range(n_queens):
        count = 0
        for y in range(cross_point):
            if female[(x + cross_point) % 8] == first_temp[y]:
                count += 1
            if count == 0 and y == cross_point - 1:
                second_temp.append(female[(x + cross_point) % 8])
    for x in range(n_queens):
        if x < cross_point:
            off_spring[x] = first_temp[x]
        if x >= cross_point:
            off_spring[x] = second_temp[x - cross_point]

    first_temp_two = [55] * cross_point
    second_temp_two = []
    off_spring_two = [55] * n_queens
    for x in range(n_queens):
        if x < cross_point:
            first_temp_two[x] = female[x]
    for x in range(n_queens):
        count = 0
        for y in range(cross_point):
            if male[(x + cross_point) % 8] == first_temp_two[y]:
                count += 1
            if count == 0 and y == cross_point - 1:
                second_temp_two.append(male[(x + cross_point) % 8])
    for x in range(n_queens):
        if x < cross_point:
            off_spring_two[x] = first_temp_two[x]
        if x >= cross_point:
            off_spring_two[x] = second_temp_two[x - cross_point]
    return off_spring, off_spring_two


# ######################################################################################################################
# ################################### TESTING ZONE ###### BEGIN ########################################################
# ######################################################################################################################


def two_point_crossover(male, female):
    return male, female



# ######################################################################################################################
# ######################################################################################################################
# ######################################################################################################################


# current_population = create_population(population_size, representation_type)
# individual_one, individual_two = selection(current_population, population_size, representation_type)
# print(individual_one, individual_two)
# print(cut_cross_fill(individual_one, individual_two))

# ######################################################################################################################
# ################################### TESTING ZONE ###### END ##########################################################
# ######################################################################################################################
