# import numpy as np
# from collections import Counter
#
# import numpy as np
# from collections import Counter
#
# def diagonal_check(z):
#   internal_count = 0
#   for x in range(0,8):
#       for y in range(0,8):
#           if abs(z[x] - z[y]) == abs(x-y) and x != y:
#               internal_count += 1
#   return internal_count
#
# def horizontile_check(z):
#   internal_count = 0
#   a = Counter(z)
#   for x in range(0,8):
#       if(a[x] > 1):
#           internal_count += a[x] * (a[x] -1)
#   return internal_count
#
# board = np.zeros((8, 8), dtype=np.int)
# print(board)
#
# def fill_board(z):
#     return board
# # #[1,0,0,0,0,0,0,0] = (0//location,1//value@)
# # def update_board_state(row, col, board):
# #     for x in range (0,8):
# #         #horiz
# #         board[x][row] += 1
# #         #verticle
# #         board[col][x] += 1
# #         #top left -> bottomw right
# #         for y in range (0,8):
# #             if(y == 0):
# #                 pass
# #             elif(x == y):
# #                 board[x-1][y] += 1
# #                 #board[x][y] += 1
# #
# #         #diag
# #
# #     board[col][row] -= 2
# #     print(board)
# #
# # update_board_state(3,2,board)
# ## how big is the search space include in the paper
# ####each gene 8^16 has poss of 1-64 or 0-63
# def create_population(size_of_population):
#     population = np.random.randint(0, 8, size=(size_of_population, 8))
#     for beta in range (0, size_of_population):
#         print('{:>3}'.format(beta + 1), " individual: ", population[beta], ' - ',
#               '{:>2}'.format(horizontile_check(population[beta]) + diagonal_check(population[beta])))
#
# #create_population(100)

import numpy as np
import time

start = time.time()
for x in range(0,100000000):
    y = 72/9
end = time.time()
print(end-start)

start = time.time()
for x in range(0,100000000):
    y = np.abs(31)
end = time.time()
print(end-start)

#issue abs is signficantly slower