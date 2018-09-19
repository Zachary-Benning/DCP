#drawing board and filling it
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

board = np.zeros((8, 8), dtype=np.int)

individual = [(3,4)] # row,col
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

#DNA display modified for chess
w=10
h=10
# fig=plt.figure(figsize=(8, 8))
# columns = 1
# rows = 1

img = board

#plt.grid(color='k', which='minor', axis='both')
#fig.add_subplot(rows, columns, 1)
plt.imshow(img)
plt.show()