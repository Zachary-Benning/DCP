import numpy as np


def sphere(p, value):
    fitness = 0
    for x in range(p):
        fitness += value[x] ** 2
    return round(fitness, 2)


def get_stats(function_selected):
    if function_selected == 0:
        # Spherical
        return sphere, -5.12, 5.12, 0


class Individual:
    """ This will hold the basic structure and data for any individual """
    def __init__(self, number_of_genes, function):
        self.genes_count = number_of_genes
        self.eval = function[0]
        self.left_bound = function[1]
        self.right_bound = function[2]
        self.target = function[3]
        self.DNA = [round(np.random.uniform(self.left_bound, self.right_bound), 2) for genes in range(self.genes_count)]

    def fitness(self):
        value = self.target - self.eval(self.genes_count, self.DNA)
        return value


class Population:
    def __init__(self, population_size, migrant_percentage, number_of_genes, stats):
        self.population = [Individual(number_of_genes, stats).DNA for individuals in range(population_size)]




stats = get_stats(0)
print(stats)
# individual1 = Individual(3, stats)
# print(individual1.left_bound)
# print(individual1.right_bound)
# print(individual1.DNA)
# print(individual1.fitness())
pop1 = Population(2, .1, 3, stats)
#print(pop1.population)
number_of_islands = 3
island_population = [Population(2, .1, 3, stats) for populations in range(number_of_islands)]

for islands in range(number_of_islands):
    print(island_population[islands].population)
# import datetime
#
#
# class User:
#     """A member of friend face"""
#
#     def __init__(self, full_name, birthday):
#         self.name = full_name
#         self.birthday = birthday # yyyymmdd
#         #extra frist and last names
#         name_pieces = full_name.split(" ")
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]
#
#
#     def age(self):
#         """Return the age of the user in years"""
#         today = datetime.date(2001, 5, 12)
#         yyyy = int(self.birthday[0:4])
#         mm = int(self.birthday[4:6])
#         dd = int(self.birthday[6:8])
#         dob = datetime.date(yyyy, mm, dd) # date of birth
#         age_in_days = (today - dob).days
#         age_in_years = age_in_days / 365
#         return int(age_in_years)
#
#
# user1 = User("Bob Builder", "19710315")
#
# print(user1.name)
# print(user1.first_name)
# print(user1.last_name)
# print(user1.birthday)
# print(user1.age())
#
#
# #help(User)