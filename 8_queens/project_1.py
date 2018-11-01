import numpy as np
import random as rd
from collections import Counter
from scipy.stats import mode as md

n_queens = 8
population_size = 1000
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


def fitness(individual): return diagonal_check(individual) + row_check(individual)


def find_second_value(input_value, input_location, score):
    input_scorez = input_value
    for y in range(0, 40):
        for x in range(0, 4):
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


def two_point_crossover(parent_one, parent_two):
    start, finish, length = create_two_point()
    child_one = [0] * 8
    child_two = [0] * 8
    for x in range(0, 8):
        if finish >= x >= start:
            child_one[x] = parent_one[x]
            child_two[x] = parent_two[x]
        else:
            child_one[x] = parent_two[x]
            child_two[x] = parent_one[x]
    for x in range(0, 8):
        for y in range(0, 8):
            if child_one[x] == child_one[y] and x != y:
                child_one[y] = parent_two[x]
            if child_two[x] == child_two[y] and x != y:
                child_two[y] = parent_one[x]
    return child_one, child_two


def create_two_point():
    end_point = rd.randint(1, 6)
    start_point = rd.randint(0, end_point - 1)
    length = end_point - start_point
    return start_point, end_point, length


def pick_bot_two(population, population_size):
    score = np.zeros(population_size, int)
    for x in range(0, population_size):
        score[x] = fitness(population[x])
    a = max(enumerate(score), key=(lambda x: x[1]))
    number_one = a[0]
    number_two = find_second_bot_value(a[1], a[0], score)
    double = 0
    for x in range(0, population_size):
        if score[x] == a[1]:
            double += 1
            if double < 1:
                print('found doubles')
    return score, number_one, number_two


def find_second_bot_value(input_value, input_location, score):
    count = 0
    for x in range(0, input_value):
        for y in range(0, population_size+2):
            if input_value - x == score[y]:
                count += 1
            if count == 2:
                return y


def pick_worst(population, population_size):
    score = np.zeros(population_size, int)
    for x in range(0, population_size):
        score[x] = fitness(population[x])
    a = max(enumerate(score), key=(lambda x: x[1]))
    return a[0]


def run_experiment():
    current_population = create_population(population_size, representation_type)
    for generation_checker in range(1000):
        if generation_checker % 100 == 0:
            print(generation_checker)
        individual_one, individual_two = selection(current_population, population_size, representation_type)
        baby_1, baby_2 = two_point_crossover(individual_one, individual_two)

        mutator(baby_1), mutator(baby_2)
        current_population.append(baby_1), current_population.append(baby_2)

        score, bot_one, bot_two = pick_bot_two(current_population, population_size+2)

        new_population = []
        for x in range(0, population_size+2):
            if x != bot_one and x != bot_two:
                new_population.append(current_population[x])

        score, best, top_two = pick_top_two(new_population, population_size)
        worst = pick_worst(new_population, population_size)
        mean = np.mean(score)
        median = np.median(score)
        mode = md(score)
        current_population = new_population
    print('best ', score[best], ' mean ', mean, ' median ', median, ' mode', mode[0][0], ' worst ', score[worst])
    count = 0
    perfect_solutions = []
    for xx in range(population_size):
        if score[xx] == 0:
            count += 1
            perfect_solutions.append(current_population[xx])
    print(count, " Perfect solutions")


run_experiment()
