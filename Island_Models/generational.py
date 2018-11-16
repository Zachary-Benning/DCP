import numpy as np
import itertools as it


def sphere(p, value):
    fitness = 0
    for x in range(p):
        fitness += value[x] ** 2
    return round(fitness, 2)


def rose(p, value):
    fitness = 0
    for x in range(p-1):
        fitness += (100 * ((value[x+1] - value[x] ** 2) ** 2)) + ((value[x] - 1) ** 2)
    return round(fitness, rounding_places)


def ras(p, value):
    fitness = 10 * p
    for x in range(p):
        fitness += (value[x] ** 2) - (10 * np.cos(2*np.pi*value[x]))
    return round(fitness, rounding_places)


def schw(p, value):
    fitness = 418.9829 * p
    for x in range(p):
        fitness += value[x] * np.sin(np.sqrt(abs(value[x])))
    return round(fitness, rounding_places)


def ack(p, value):
    first = 0
    second = 0
    for x in range(p):
        first += value[x] ** 2
        second += np.cos(2*np.pi*value[x])
    fitness = 20 + np.e - 20 * np.exp(-0.2 * np.sqrt((1/p) * first)) - np.exp((1/p) * second)
    return round(fitness, rounding_places)


def grie(p, value):
    first = 0
    second = 0
    for x in range(p):
        first += (value[x] ** 2) / 4000
        second *= np.cos(value[x]/np.sqrt(x))
    fitness = 1 + first - second
    return round(fitness, rounding_places)


def get_stats(function_selected):
    if function_selected == 0:
        # Spherical
        return -5.12, 5.12, 0
    elif function_selected == 1:
        # Rosenbrock
        return -2.048, 2.048, 1
    elif function_selected == 2:
        # Rastrigin
        return -5.12, 5.12, 0
    elif function_selected == 3:
        # Schwefel
        return -512.03, 511.97, -420.9687
    elif function_selected == 4:
        # Ackley
        return -30, 30, 0
    elif function_selected == 5:
        #Griewangk
        return -600, 600, 0
    else:
        print("ERROR CRITICAL FAILURE:: get_stats invalid function selection")


def create_individual(left_domain, right_domain, number_of_genes):
    spawning_individual = []
    for x in range(number_of_genes):
        spawning_individual.append(round(np.random.uniform(left_domain, right_domain), 2))
    return spawning_individual


def create_population(desired_pop_count, left_domain, right_domain, number_of_genes):
    temp_population = [0] * desired_pop_count
    for x in range(desired_pop_count):
        temp_population[x] = create_individual(left_domain, right_domain, number_of_genes)
    return temp_population


def split_into_island_group(temp_population, number_of_islands, island_population_size):
    temp_island_population = [['N/A' for x in range(island_population_size)] for y in range(number_of_islands)]
    for y in range(number_of_islands):
        for x in range(island_population_size):
            temp_island_population[y][x] = temp_population[x + (y * island_population_size)]
    return temp_island_population


def create_migrant_group(island_pop, number_of_islands, migrant_pop_percentage, island_pop_size):
    migrant_size = int(np.ceil(migrant_pop_percentage * island_pop_size))
    if migrant_size <= 0:
        migrant_size = 1
    migrant_population = [['N/A' for x in range(migrant_size)] for y in range(number_of_islands)]
    for y in range(number_of_islands):  # 2
        for x in range(migrant_size):  # 5
            z = np.random.randint(2, island_pop_size)
            migrant_population[y][x] = island_pop[(y + 1) % number_of_islands][x + (z - 2) - 1]
    return migrant_population, migrant_size


def one_pt_cross_over(individual_one, individual_two, number_of_attributes):
    cross_pt = np.random.randint(1, number_of_attributes - 1)
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


def simple_mutator(individual, number_of_attributes, lb, ub):
    number_of_random_mutations = np.random.randint(1, number_of_attributes)
    for x in range(number_of_random_mutations):
        mutation_point = np.random.randint(0, number_of_attributes)
        individual[mutation_point] = round(np.random.uniform(lb, ub), 2)
    return individual


def selection(individual_traits_in_island, number_local_pop_in_island, migrant_pop_size_percentage,
              migrant_group, number_of_migrants, expected_min, number_of_genes, function_selected, lb, ub):
    individuals_for_reproduction = ['ERROR', 'ERROR']
    y = np.random.randint(0, 100)
    if y <= int(migrant_pop_size_percentage * 100):
        z = np.random.randint(0, number_of_migrants)
        individuals_for_reproduction[0] = migrant_group[z]
        individuals_for_reproduction[1] = tournament_style(number_local_pop_in_island, individual_traits_in_island,
                                                           number_of_genes, expected_min, function_selected)
    else:
        individuals_for_reproduction[0] = tournament_style(number_local_pop_in_island, individual_traits_in_island,
                                                           number_of_genes, expected_min, function_selected)
        individuals_for_reproduction[1] = tournament_style(number_local_pop_in_island, individual_traits_in_island,
                                                           number_of_genes, expected_min, function_selected)
    children = one_pt_cross_over(individuals_for_reproduction[0], individuals_for_reproduction[1], number_of_genes)
    for x in range(2):
        simple_mutator(children[x], number_of_genes, lb, ub)
    return individuals_for_reproduction


def tournament_style(number_in_local_population, individuals_on_island, number_of_genes, expected_min, function_selected):
    y = [99999] * 5
    for x in range(5):
        y[x] = np.random.randint(0, number_in_local_population)
    current_pop_fitness = [99999] * 5
    for x in range(5):
        current_pop_fitness[x] = fitness(function_selected, number_of_genes, individuals_on_island[y[x]], expected_min)
    b = list(enumerate(current_pop_fitness))
    c = sorted(b, key=lambda b: b[1])
    for x in range(5):
        if b[x] == c[0]:
            return individuals_on_island[y[x]]


def fitness(f, p, value, expected_min):
    return f(p, value) - expected_min


def generation(island_pop_count, number_of_islands, lb, ub):
    entire_pop_next_gen = [9999] * number_of_islands
    for y in range(number_of_islands):
        next_gen = [99999] * (island_pop_count // 2)
        for x in range(island_pop_count // 2): #add this with elitism((island_pop_count // 2) - 1):
            next_gen[x] = (selection(current_island_population[y], island_capacity, migrant_percentage, current_migrant_population[y],
                           migrant_population_size, target_value, number_of_traits, function_name, lb, ub))
        a = list(it.chain.from_iterable(next_gen))
        entire_pop_next_gen[y] = a
    return entire_pop_next_gen


rounding_places = 2
function_selection = 0
function_name = sphere
left_bound, right_bound, target_value = get_stats(function_selection)
number_of_traits = 3
population_count = 100
number_islands_in_simulation = 5  # make sure it divides twice for the children problem once by number islands once by 2
island_capacity = population_count // number_islands_in_simulation
migrant_percentage = .1
###############################################################################################################
###############################################FUNCTION CHECKER################################################
###############################################################################################################
if population_count % number_islands_in_simulation > 0:
    print("ERROR POP COUNT AND ISLAND COUNT NOT COMPATIBLE")
    exit(0)
###############################################################################################################
###############################################FUNCTION CHECKER################################################
###############################################################################################################
#################### PREP #####################################################################################
population = create_population(population_count, left_bound, right_bound, number_of_traits)
current_island_population = split_into_island_group(population, number_islands_in_simulation, island_capacity)
current_migrant_population, migrant_population_size = create_migrant_group(current_island_population,
                                                                           number_islands_in_simulation,
                                                                           migrant_percentage, island_capacity)
###############################################################################################################
#################### GENERATIONS ##############################################################################
###############################################################################################################
# # picking mates
# children = selection(current_island_population[0], island_capacity, migrant_percentage, current_migrant_population[0],
#                      migrant_population_size, target_value, number_of_traits, function_name)
# #############
for x in range(3000):
    for y in range(number_islands_in_simulation):
        island_fitness_score = 0
        for z in range(island_capacity):
            island_fitness_score += fitness(function_name, number_of_traits, current_island_population[y][z], target_value)
        if y == 0 and x % 100 == 0:
            print('generation: ', x, 'island ', y, island_fitness_score / island_capacity)
            print(current_migrant_population)
    generation_x = generation(island_capacity, number_islands_in_simulation, left_bound, right_bound)
    current_island_population = generation_x
    if x % 30 == 0 and x != 0:
        current_migrant_population, migrant_population_size = create_migrant_group(current_island_population,
                                                                                   number_islands_in_simulation,
                                                                                   migrant_percentage, island_capacity)
print(current_island_population[0])

#### CHECK MIGRANTS CHANGING ALGORITHM

