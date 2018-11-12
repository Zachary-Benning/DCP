import numpy as np

def sphere(p, value):
    fitness = 0
    for x in range(p):
        fitness += value[x] ** 2
    return round(fitness, 2)


def rose(p, value):
    fitness = 0
    for x in range(p-1):
        fitness += round((100 * ((value[x+1] - value[x] ** 2) ** 2)) + ((value[x] - 1) ** 2), 2)
    return fitness


def ras(p, value):
    fitness = 10 * p
    for x in range(p):
        fitness += (value[x] ** 2) - (10 * np.cos(2*np.pi*value[x]))
    return fitness


def schw(p, value):
    fitness = 418.9829 * p
    for x in range(p):
        fitness += value[x] * np.sin(np.sqrt(abs(value[x])))
    return fitness


def ack(p, value):
    first = 0
    second = 0
    for x in range(p):
        first += value[x] ** 2
        second += np.cos(2*np.pi*value[x])
    fitness = 20 + np.e - 20 * np.exp(-0.2 * np.sqrt((1/p) * first)) - np.exp((1/p) * second)
    return fitness


def grie(p, value):
    first = 0
    second = 0
    for x in range(p):
        first += (value[x] ** 2) / 4000
        second *= np.cos(value[x]/np.sqrt(x))
    fitness = 1 + first - second
    return fitness


def get_stats(function_selected):
    if function_selected == 0:
        # SPherical
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


def create_individual(stats_needed, number_of_genes):
    spawning_individual = []
    for x in range(number_of_genes):
        spawning_individual.append(round(np.random.uniform(stats_needed[0], stats_needed[1]), 2))
    return spawning_individual


def create_population(desired_pop_count, statistics, number_of_genez):
    population = [0] * desired_pop_count
    for x in range(desired_pop_count):
        population[x] = create_individual(statistics, number_of_genez)
    return population


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


def simple_mutator(individual, number_of_attributes, range_of_values):
    mutation_point = np.random.randint(0, number_of_attributes)
    individual[mutation_point] = round(np.random.uniform(-1 * range_of_values, range_of_values), 2)
    return individual


def selection(individual_traits_in_island, number_local_pop_in_island, migrant_pop_size_percentage,
              migrant_groupz, number_of_migrants):
    individuals_for_sex = ['ERROR', 'ERROR']
    for x in range(2):
        y = np.random.randint(0, 100)
        if y <= int(migrant_pop_size_percentage * 100):
            z = np.random.randint(0, number_of_migrants)
            individuals_for_sex[x] = migrant_groupz[z]
        else:
            print("pureblood")
            individuals_for_sex[x] = tournament_style(number_local_pop_in_island, individual_traits_in_island) #individual_traits_in_island[z]
    return individuals_for_sex


def tournament_style(number_in_local_population, population):
    y = [99999] * 5
    for x in range(5):
        y[x] = np.random.randint(0, number_in_local_population)
    current_pop_fitness = [99999] * 5
    for x in range(5):
        current_pop_fitness[x] = sphere(gene_number_selection, population[x])## USING GLOBAL GENE NUMBER SELECTION
    b = list(enumerate(current_pop_fitness))
    c = sorted(b, key=lambda b: b[1])
    for x in range(5):
        if b[x] == c[0]:
            return population[y[x]]


def split_into_island_group(population, number_of_islands, island_population_size):
    island_population = [['N/A' for x in range(island_population_size)] for y in range(number_of_islandz)]
    for y in range(number_of_islands):#2
        for x in range(island_population_size):# 5
            island_population[y][x] = population[x + (y * island_population_size)]
    return island_population


def create_migrant_group(island_pop, number_of_islands, migrant_pop_percentage, island_pop_size):
    migrant_size = int(np.ceil(migrant_pop_percentage*islandz_population_size))
    if migrant_size <= 0:
        migrant_size = 1
    migrant_population = [['N/A' for x in range(migrant_size)] for y in range(number_of_islands)]
    for y in range(number_of_islands):  # 2
        for x in range(migrant_size):  # 5
            z = np.random.randint(2, island_pop_size)
            migrant_population[y][x] = island_pop[y][x + (z - 2)]
    return migrant_population, migrant_size





#####NOTE:########## Make sure island_number is a multiple of population size
function_selection = 0
gene_number_selection = 2
number_of_islandz = 2
number_of_total_population = 12
percentage_migrant_population = .1
islandz_population_size = number_of_total_population // number_of_islandz

stats = get_stats(function_selection)
general_population = create_population(number_of_total_population, stats, gene_number_selection)
islandz_population = split_into_island_group(general_population, number_of_islandz, islandz_population_size)
migrantz_population, migrantz_size = create_migrant_group(islandz_population, number_of_islandz,
                                                          percentage_migrant_population, islandz_population_size)

# print(islandz_population[0])
# print(migrantz_population[0])

########################################################################################################################
########################################################################################################################
########################################################################################################################
for x in range(1):
    print('--->', islandz_population[0])
    male, female = selection(islandz_population[0], islandz_population_size, percentage_migrant_population,
                             migrantz_population[1], migrantz_size)
    #note always pass through migrantz n + 1 mod island_number
print('male/female', male, female)
# print(islandz_population)
# print(migrantz_population)

########################################################################################################################
########################################################################################################################
########################################################################################################################

# #run_generation(bob, stats, migrant_group, migrant_population_size, number_of_islandz, island_counter, x)
#
# def run_generation(island, stats, migrant_group, migrant_population_size, number_of_islandz, island_count, trigger):#, better_island):
#     best_island = [[[0] * gene_number_selection for x in range(island_count[y])] for y in range(number_of_islandz)]
#     for island_number in range(number_of_islandz):
#         better_island = []
#         for x in range(0, number_of_total_population):
#             if island[island_number][x] != 'N/A':
#                 better_island.append(island[island_number][x][0])
#         island_size_pre_birthing = len(better_island)
#
#         #############################################################################
#         print('better island ', better_island)
#         #############################################################################
#
#         for x in range(len(better_island)//2):
#             parents = selection(better_island, len(better_island), percentage_migrant_population,
#                                 migrant_group[island_number], migrant_population_size[island_number])
#             child_uno, child_dos = one_pt_cross_over(parents[0], parents[1], gene_number_selection)
#             simple_mutator(child_uno, gene_number_selection, stats[1])
#             simple_mutator(child_dos, gene_number_selection, stats[1])
#             better_island.append(child_uno)
#             better_island.append(child_dos)
#
#         current_pop_fitness = [99999] * len(better_island)
#         for x in range(len(better_island)):
#             current_pop_fitness[x] = sphere(gene_number_selection, better_island[x])
#         ###########################
#         #if trigger == 299 or trigger == 0:
#         average_is = 0
#         for x in range(len(better_island)):
#             average_is += current_pop_fitness[x]
#         average_is /= len(better_island)
#         print(round(average_is, 2))
#         ###########################
#         b = list(enumerate(current_pop_fitness))
#         c = sorted(b, key=lambda b: b[1])
#         better_island_second = [000000] * island_size_pre_birthing
#         for x in range(island_size_pre_birthing):
#             better_island_second[x] = better_island[c[x][0]]
#         for y in range(0, island_count[island_number]):
#             for z in range(0, gene_number_selection):
#                 best_island[island_number][y][z] = better_island_second[y][z]
#     return best_island

# def run_for_a_while(islandz):
#     for x in range(5):
#         print(x)
#         bob = run_generation(islandz, stats, migrant_group, migrant_population_size, number_of_islandz, island_counter, x)
#         if x > 1:
#             return run_generation(bob, stats, migrant_group, migrant_population_size, number_of_islandz, island_counter, x)
#         else:
#             return bob
#
# #############################
# #######################
# #######
# # NEXT TO DO CLEAN ISLAND UP SO RECURSIVE WORKS
# #############
#         # if x % 10 == 0:
#         #     print(x / 300, '%')
#
#
#     # print(islandz[0])
#     # print(islandz[1])
#     # print(islandz[2])
#     # print(len(islandz[1]))
#
# run_for_a_while(island)
# ######################
# # migrate
# # fitness sharing
# # crowding
#
