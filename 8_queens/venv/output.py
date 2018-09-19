import numpy as np
from copy import deepcopy

board = np.zeros((8, 8), dtype=np.int)

individual = [(5,1)] # row,col
x = individual[0][0]
y = individual[0][1]

board[x][y] += 1
for itera in range (0,8):
    if (itera != x):
        board[itera][y] += 1 #adds 1 to the first col
    if (itera != y):
        board[x][itera] += 1

def criss_cross(x,y):
    location  = x + y
    location0 = y - x
    for xn in range (0,8):
        if (location-xn <= 7 and location-xn >=0 and location-xn != y):
            alpha = location-xn
            board[xn][alpha] += 1
    for yn in range(0,8):
        if (location0 + yn <= 7 and location0 + yn >=0 and location0+yn !=y):
            beta = location0 + yn
            board[yn][beta] += 1


criss_cross(individual[0][0],individual[0][1])
# print(individual[0][0], individual[0][1])

print(board)

#
# def rotate_counterclockwise(matrix, degree=90):
#     #if degree not in [0, 90, 180, 270, 360]:
#     # raise error or just return nothing or original
#     return rotate_counterclockwise(zip(*matrix)[::-1], degree - 90)
#
# boardz = rotate_counterclockwise(board,270)
# print(boardz)