# individual [x-value, age, island_location, migrant_status, fitness]
# migrant status 0 = false 1 = true :: truth = is a migrant
import numpy as np


def f_spherical(x):
    return round(x ** 2, 8), 0


def create_adult_individual(positive_edge_parameter, number_of_islands, benchmark_func, island_pop_track):
    value = [999] * 2
    starting_fitness = 0
    for x in range(0, 2):
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


def create_population(population_size, number_of_islands, positive_edge_parameter, benchmark_func):
    population = [0] * population_size
    if number_of_islands == 0:
        island_population_tracker = [0]
    else:
        island_population_tracker = [0] * number_of_islands
    for x in range(0, population_size):
        population[x] = create_adult_individual(positive_edge_parameter, number_of_islands,
                                                benchmark_func, island_population_tracker)
    return population


# #########################################################
# ####################### GUTS ############################
population_size_declared = 100
number_of_islands_declared = 3
positive_edge_parameter_declared = 5.12
benchmark_func_declared = f_spherical
# #########################################################

current_population = create_population(population_size_declared, number_of_islands_declared,
                                       positive_edge_parameter_declared, benchmark_func_declared)




pop_fitness = 0
for x in range(0, population_size_declared):
    pop_fitness += current_population[x][4]
print(round(pop_fitness/300, 2))

#[0,0,location] = [2]


island = [['N/A' for x in range(population_size_declared)] for y in range(number_of_islands_declared)]
for y in range(0, number_of_islands_declared):
    z = 0
    for x in range(0, population_size_declared):
        if current_population[x][2] == y:
            island[y][z] = current_population[x]
            z += 1


print(island[0])
print(island[1])
print(island[2])
