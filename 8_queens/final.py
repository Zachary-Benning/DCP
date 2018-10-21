# need to have a memory for the 92 solutions,
#there are only 92 solutions, took chess masters 2 years ... the entire community
#find 1 correct board configuration


import numpy as np
import random as rd
from collections import Counter


n_queens = 8


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


#crux of the manner
def fitness(individual): return row_check(individual) + diagonal_check(individual)
#need to ad ver* check
#variance analysis __ probability class

#collect data 30 times for two should have 90,000 data points 30 * 1000 * 3(worst,best,averge fitness pts)


def print_population(size_of_population, population):
    for beta in range(0, size_of_population):
        print('{:>3}'.format(beta + 1), " individual: ", population[beta], ' - ',
              '{:>2}'.format(fitness(population[beta])))


def one_pt_cross_over(first_individual, second_individual):
    cross_point = np.random.randint(1, n_queens - 1)
    first_temp = [55] * cross_point
    second_temp = []
    off_spring = [55] * n_queens
    print(cross_point)
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


#create two point cross over
#link files together in python _init_.py files
#create selection from population
def selection(): return 0


population_size = 6
population = create_population(population_size, 0)
print(population[0],population[1])
#print(one_pt_cross_over(population[0], population[1]))



#print(population[0], population[1])
#cross_over(population[0], population[1])
#print(population[0], population[1])
# score = np.zeros(population_size, int)
# for x in range(0, population_size):
#     score[x] = fitness(population[x])


#a = min(enumerate(score), key=(lambda x: x[1]))
#best_value_location = a[0]

#print("Best fitnesss")
#print(population)
#print(population[0])
#test_mutate = population[0]
#print(mutation(test_mutate))
#print(score)

# def find_second_value(input_value, input_location):
#     input_scorez = input_value
#     for y in range(0, 40):
#         for x in range(0, population_size):
#             if score[x] == input_scorez and x != input_location:
#                 return input_scorez
#         input_scorez += 1


# number_one = a[0]
# number_two = 0
#
# solution = find_second_value(a[1],a[0])
# zztop = np.where(score==solution)
# if len(zztop[0]) > 1:
#     number_two = zztop[0][1]
# else:
#     number_two = zztop[0][0]
#
# print(number_one, ' ', number_two)