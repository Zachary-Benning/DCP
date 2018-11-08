# individual [x-value, age, island_location, migrant_status, fitness]
# migrant status 0 = false 1 = true :: truth = is a migrant
import numpy as np


def f_spherical(input):
    return round(input ** 2, 8), 0


def f_rosenbrock(input):
    return (100 * ((input[0] - input[1] ** 2) ** 2)) + ((input[0]-1) ** 2), 2.048


def f_rastrigin(input):
    return 0


def f_schwefel(input):
    return 0


def f_ackley(input):
    return 0


def f_griewangk(input):
    return 0


def create_adult_individual(positive_edge_parameter, number_of_islands, benchmark_func, island_pop_track,
                            number_of_attributes):
    value = [999] * number_of_attributes
    starting_fitness = 0
    for x in range(0, number_of_attributes):
        value[x] = round(np.random.uniform(positive_edge_parameter * (-1), positive_edge_parameter), 8)
        starting_fitness += fitness_calc(benchmark_func, value[x])
    starting_fitness = round(starting_fitness / 2.0, 2)
    newborn_age = 0
    if number_of_islands == 0:
        current_location = 0
        island_pop_track[current_location] += 1
    else:
        current_location = np.random.randint(0, number_of_islands)
        island_pop_track[current_location] += 1
    migrant_status = 0
    return value, newborn_age, current_location, migrant_status, starting_fitness, island_pop_track


# here we are trying to stress the value by squaring the results of the difference
def fitness_calc(benchmark_func, x):
    __results = benchmark_func(x)
    return round(__results[0] - __results[1] ** 2, 2)


def create_population(population_size, number_of_islands, positive_edge_parameter, benchmark_func, individual_attributes):
    population = [0] * population_size
    if number_of_islands == 0:
        island_population_tracker = [0]
    else:
        island_population_tracker = [0] * number_of_islands
    for x in range(0, population_size):
        population[x] = create_adult_individual(positive_edge_parameter, number_of_islands,
                                                benchmark_func, island_population_tracker, individual_attributes)
    return population


# #########################################################
# ####################### GUTS ############################
population_size_declared = 2
number_of_islands_declared = 1
positive_edge_parameter_declared = 2.048
benchmark_func_declared = f_spherical
attributes_for_individual = 5
# #########################################################

current_population = create_population(population_size_declared, number_of_islands_declared,
                                       positive_edge_parameter_declared, benchmark_func_declared, attributes_for_individual)


print(current_population)

def dummy_func():
    return 0
#
# pop_fitness = 0
# for x in range(0, population_size_declared):
#     pop_fitness += current_population[x][4]
# #print(round(pop_fitness/300, 2))
#
#
# island = [['N/A' for x in range(population_size_declared)] for y in range(number_of_islands_declared)]
# for y in range(0, number_of_islands_declared):
#     z = 0
#     for x in range(0, population_size_declared):
#         if current_population[x][2] == y:
#             island[y][z] = current_population[x]
#             z += 1
#
#
# for x in range(len(island)):
#     print(island[x])


#                      pass in island[0][0][0] and change [0][x][0]
def one_pt_cross_over(individual_one, individual_two, number_of_attributes):
    cross_pt = np.random.randint(1, number_of_attributes - 1)
    print(cross_pt)
    child_one = [0] * number_of_attributes
    child_two = [0] * number_of_attributes
    for x in range(number_of_attributes):
        if x <= cross_pt:
            child_one[x] = individual_one[x]
            child_two[x] = individual_two[x]
        if x > cross_pt:
            child_one[x] = individual_two[x]
            child_two[x] = individual_one[x]
    return child_one, child_two


def simple_mutator(individual, number_of_attributes, range_of_values):
    mutation_point = np.random.randint(0, number_of_attributes)
    individual[mutation_point] = round(np.random.uniform(-1 * range_of_values, range_of_values), 8)
    return individual

