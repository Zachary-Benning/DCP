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


def create_individual(stats_needed, number_of_genes, number_of_islands):
    spawning_individual = ['N/A'] * number_of_genes
    for x in range(number_of_genes):
        spawning_individual[x] = round(np.random.uniform(stats_needed[0], stats_needed[1]), 2)
    if number_of_islands == 0:
        print('YOUR POPULATION DROWNED ... GOOD JOB')
        exit(0)
    else:
        current_location = np.random.randint(0, number_of_islands)
    migrant_status = 0
    return spawning_individual, current_location, migrant_status


def create_population(desired_pop_count, statistics, number_of_genez, number_of_locations):
    population = [0] * desired_pop_count
    for x in range(desired_pop_count):
        population[x] = create_individual(statistics, number_of_genez, number_of_locations)
    return population


def prompt():
    print()
    print()
    print()
    print("*******************************************************************************************")
    print("*******************************************************************************************")
    print("*******************************************************************************************")
    print("*** Welcome to Project 2 Where we use Island models to solve famous benchmark functions ***")
    print("*******************************************************************************************")
    print("*******************************************************************************************")
    print("*******************************************************************************************")
    print("******************* Please select one of the following functions to test ******************")
    print("*************************** Press 0 for Spherical *****************************************")
    print("*************************** Press 1 for Rosenbrock ****************************************")
    print("*************************** Press 2 for Rastrigin *****************************************")
    print("*************************** Press 3 for Schwefel ******************************************")
    print("*************************** Press 4 for Ackley ********************************************")
    print("*************************** Press 5 for Griewangk *****************************************")
    function_number = input('*************************************')
    print("*******************************************************************************************")
    print("*******************************************************************************************")
    print("*******************************************************************************************")
    print("************* How many genes do you want in an individual?  (1 - 100) *********************")
    gene_number = input('*************************************')
    island_count = input('****************************** How many islands? ')
    pop_count = input('********************** How big do you want the total population')
    print("*******************************************************************************************")
    print("*******************************************************************************************")
    print("*******************************************************************************************")
    print()
    print()
    print()
    return int(function_number), int(gene_number), int(island_count), int(pop_count)


#function_selection, gene_number_selection, number_of_islandz, number_of_total_population = prompt()
function_selection = 0
gene_number_selection = 3
number_of_islandz = 5
number_of_total_population = 500
stats = get_stats(function_selection)
current_pop = create_population(number_of_total_population, stats, gene_number_selection, number_of_islandz)
#print(current_pop)


#print(current_pop_fitness)

#sort into islands

#############ADD COUNTER for later loops
island = [['N/A' for x in range(number_of_total_population)] for y in range(number_of_islandz)]
island_counter = [9999] * number_of_islandz
for y in range(0, number_of_islandz):
    z = 0
    for x in range(0, number_of_total_population):
        if current_pop[x][1] == y:
            island[y][z] = current_pop[x]
            z += 1
    island_counter[y] = z


# print('island_counter', island_counter)
# for x in range(len(island)):
#     print('island %d' % x, island[x])
percentage_migrant_population = .15
migrant_population_size = [9999999] * number_of_islandz
for x in range(number_of_islandz):
    migrant_population_size[x] = int(np.floor(island_counter[x] * percentage_migrant_population))


#print('migrant_pop_size', migrant_population_size)

# create migrants
migrant_group = [['MigrantN/A' for x in range(migrant_population_size[y])] for y in range(number_of_islandz)]
for y in range(number_of_islandz):
    cap = migrant_population_size[y]
    for x in range(cap):
        i_x = np.random.randint(0, island_counter[y])
        migrant_group[y][x] = island[y][i_x][0]


# for x in range(number_of_islandz):
#     print('migrant_group', migrant_group[x], len(migrant_group[x]))
#
# print(island[0])
# print(island[1])
# print(migrant_group[0])
# print(migrant_group[1])

## DO percentage approach

# island_counter[y] / island_counter[y] + 10  OR 10 / island_counter[y] + 10
# for x in range(number_of_islandz):
#     print(island_counter[x] / (island_counter[x] + 10), 10 / (island_counter[x] + 10))


### Migrant group is for the group behind it i.e. island[0] merges with migrant[1] ...
# breed

def one_pt_cross_over(individual_one, individual_two, number_of_attributes):
    cross_pt = np.random.randint(1, number_of_attributes - 1)
    #print(cross_pt)
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
            z = np.random.randint(0, number_local_pop_in_island)
            individuals_for_sex[x] = individual_traits_in_island[z]#individual_traits_in_island[0][z][0]
    return individuals_for_sex


#### cleans up island
#print('size of island', len(island[0]))
better_island = []
#print(island[0][499])
for x in range(0, 499):
    if island[0][x] != 'N/A':
        better_island.append(island[0][x][0])
print('after cleaning',better_island)
print('len of island', len(better_island))
save_this_crap = len(better_island)


for x in range(len(better_island)//2):
    parents = selection(better_island, len(better_island), percentage_migrant_population, migrant_group[0], migrant_population_size[0])
    child_uno, child_dos = one_pt_cross_over(parents[0], parents[1], gene_number_selection)
    simple_mutator(child_uno, gene_number_selection, stats[1])
    simple_mutator(child_dos, gene_number_selection, stats[1])
    better_island.append(child_uno)
    better_island.append(child_dos)


print('newpop', len(better_island))
print(better_island)

# kill
current_pop_fitness = [99999] * len(better_island)

for x in range(len(better_island)):
    #print('%i : ' % x, sphere(3, current_pop[x][0]))
    current_pop_fitness[x] = sphere(gene_number_selection, better_island[x])

print(current_pop_fitness)
### GET Best number == original island size ... remove the rest


# a = min(enumerate(current_pop_fitness), key=(lambda x: x[1]))
# print(a)
b = list(enumerate(current_pop_fitness))
print(b)
c = sorted(b, key=lambda b: b[1])
print(len(c), 'better island', len(better_island))
print(c[0][0], c[0][1])
better_island_second = [000000] * save_this_crap
for x in range(save_this_crap):
    better_island_second[x] = better_island[c[x][0]]
print(better_island_second)

## modularlize and get running for every island

######################
# migrate
# fitness sharing
# crowding

