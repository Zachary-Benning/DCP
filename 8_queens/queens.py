# need to have a memory for the 92 solutions,

#there are only 92 solutions, took chess masters 2 years ... the entire community
#find 1 correct board configuration
#
# #64 mapping structure above and beyond?!
# #
# 21 is worst for row conflicts

import numpy as np
from collections import Counter

#class Individual(object):
gene = [0,1,2,3,4,5,6,7]
#genex = np.zeros((2,8),int)
#print(genex)
#for x in range(0,8):

# DNA =             [(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y)], fitness score,
# attracation gene
# 3 -> 0 OR 4
# 5 -> 1 OR 2
# 4 -> 9 OR 6
# 8 -> 4 OR 9
# 2 -> 7 OR 7
# 0 -> 8 OR 1
# 1 -> 5 OR 3
# 9 -> 6 OR 0
# 6 -> 2 OR 5
# 7 -> 3 OR 8

# for x in range(0,5):
#     np.random.shuffle(gene)
#     print(gene)

def diagonal_check(z):
  internal_count = 0
  for x in range(0,8):
      for y in range(0,8):
          if abs(z[x] - z[y]) == abs(x-y) and x != y:
              internal_count += 1
  return internal_count

def mutation(gene):
    x= np.random.randint(0, 8, None, int)
    y= (np.random.randint(0, 8, None, int) + x) % x
    print(x, y)
    print(gene)
    gene[x] = y
    print(gene)

mutation(gene)

def horizontile_check(z):
  internal_count = 0
  a = Counter(z)
  for x in range(0,8):
      if(a[x]>1):
          internal_count += a[x] * (a[x] -1)
  return internal_count


def create_population(size_of_population,max_value_in_gene, num_gene_per_individual):
    return (np.random.randint(0, (max_value_in_gene + 1), size=(size_of_population,num_gene_per_individual)))


def fitness(individual):
    return horizontile_check(individual) + diagonal_check(individual) #need to ad ver* check
#variance analysis __ probability class

#collect data 30 times for two should have 90,000 data points 30 * 1000 * 3(worst,best,averge fitness pts)


def print_population(size_of_population, population):
    for beta in range (0,size_of_population):
        print('{:>3}'.format(beta + 1), " individual: ", population[beta], ' - ',
              '{:>2}'.format(fitness(population[beta])))



def selection(literal_population,style,population_size):
    return 0
#def mutation
#def crossover
    # if parent2[array] not in child1
#def repopulate


# population_size = 6
# population = create_population(population_size,5,8)
# score = np.zeros(population_size,int)
# print(score)
# for x in range (0,population_size):
#     score[x] = fitness(population[x])
# print(score)


# print(list(enumerate(score)))
# a = min(enumerate(score), key=(lambda x: x[1]))
# best_value_location = a[0]
# print(best_value_location)
# print(population)
# print("Best fitnesss")
# print(population[best_value_location])
#
# print(population)



#crowding eliminating clumps by niches probability for destroying could include crowded clump -- fitness sharing another principle
#survival -- age and survival based on age
#pareto optimization curves
#look for pareto front ... line that are showing the best values for each of the given attributes paretofront=fence
#everything on the pareto fence are said to be pareto optimized

#print_population(population_size,population)
#print(population[0])
#print(horizontile_check([0,1,2,3,4,5,6,7])+diagonal_check([0,1,2,3,4,5,6,7]))
# f = open('/home/zac/Desktop/python_101/8_queens/sampleText.txt','a')
# for xy in range (0, population_size):
#     for xx in range(0,1):
#         f.write('\n %03d' % a[xx])
# f.close()
