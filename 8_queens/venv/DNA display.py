#compare generation model vs currently only 2 children made with 98 old...
import numpy as np
import matplotlib.pyplot as plt
# w=2
# h=10
# fig=plt.figure(figsize=(8, 8))
# columns = 1
# rows = 1
# for i in range(1, columns*rows +1):
#     img = np.random.randint(10, size=(h,w))
#     print(img)
#     fig.add_subplot(rows, columns, i)
#     plt.imshow(img)
#
# plt.show()
w=2
h=10
fig=plt.figure(figsize=(8, 8))
columns = 1
rows = 1

valueboy = 3
title = 'Fitness Score: ' + str(valueboy)

img = [[0.5,0.5],[1.5,1.5],[2.5,2.5],[3.5,3.5],[4.5,4.5],[5.5,5.5],[6.5,6.5],[7.5,7.5],[8.5,8.5],[9.5,9.5]]

fig.add_subplot(rows, columns, 1)

# doesnt work but usefull ... img.grid(color='r', linestyle='-', linewidth=2)
#plt.grid(color='k', which='both', axis='both',markeredgewidth=1)
plt.imshow(img)
plt.title(title)
plt.text(1.75, .025, r'Generation: 100')
plt.text(1.75, .525, r'Attractiveness Score: 100')

plt.show()