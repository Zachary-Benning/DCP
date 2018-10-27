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
        for x in range(0, population_size):
            if score[x] == input_scorez and x != input_location:
                return input_scorez
        input_scorez += 1


def pick_top_two(population, population_size):
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


def selection(population, population_size, tournament_type):
    if tournament_type == 0:
        tournament_style_top_x(population, population_size, 5)


def tournament_style_top_x(population, population_size, x):
    print("0")
    random_x = rd.sample(range(0, population_size), x)
    print("1")
    #print(random_x)
    top_x = [0] * x
    for x in range(x):
        top_x[x] = population[random_x[x]]
    print("2")
    #print(top_x)
    score, top_one, top_two = pick_top_two(top_x, x)
    print('3')
    print(top_one, top_two)

current_population = create_population(population_size, representation_type)
selection(current_population, population_size, representation_type)
#it was working with just tournament style then when switched to selection function it broke
# or at least it worked partially  ... it breaks due to a seg fault "index" issue.

#score, alpha, beta = pick_top_two(current_population, population_size)
#print(current_population)
#print(alpha, beta)
