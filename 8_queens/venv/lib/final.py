# need to have a memory for the 92 solutions,
#there are only 92 solutions, took chess masters 2 years ... the entire community
#find 1 correct board configuration
# #64 mapping structure above and beyond?!

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


#make one return statement makes code better
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


def cross_over(first_individual, second_individual):
    cross_point = np.random.randint(1, n_queens - 1)
    temp_first_individual = [0] * n_queens
    temp_second_individual = [0] * n_queens
    # Creates a temporary list of second individual in an accetable cross over way
    for x in range(n_queens):
        temp_first_individual[x] = second_individual[(x + 1) % n_queens]
        temp_second_individual[x] = first_individual[(x + cross_point) % n_queens]
    # remove all elements in temp that exist in individual pre crossover_pt
    to_remove_list = []
    print(cross_point)
    print(first_individual, "first_individual")
    print(temp_second_individual)
    print(second_individual, "second_individual")
    print(temp_first_individual)
    print('h', to_remove_list, "h")
    for x in range(n_queens):
        if temp_second_individual[x] in first_individual[:cross_point]:
            to_remove_list.append(x)
    print('h', to_remove_list, "h")


def one_pt_cross_over(first_individual, second_individual):
    cross_point = 3#np.random.randint(1, n_queens - 1)
    temp_first_individual = first_individual
    temp_second_individual = second_individual
    off_spring = [0] * n_queens

    cross_point_check = [0] * cross_point
    for y in range(cross_point):
        cross_point_check[y] = temp_second_individual[y]
    print(cross_point_check)


    for x in range(n_queens):
        if x < cross_point:
            off_spring[x] = temp_first_individual[x]
            print(x)
        if x >= cross_point:
            off_spring[x] = temp_second_individual[x]
    print('cross point:: ', cross_point)
    print('first individual:: ', first_individual)
    print('second individual:: ', second_individual)
    print('offspring:: ', off_spring)


def selection(): return 0


population_size = 6
population = create_population(population_size, 0)
print(one_pt_cross_over(population[0], population[1]))
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