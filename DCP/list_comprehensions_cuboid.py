# Print a list of all possible coordinates given by
# (i,j,k) on a 3D grid where the sum i+j+k is not equal
# to N.  Here 0<=i<=X ; 0<=j<=Y ; 0<=k<=Z

# X,i
# Y,j
# Z,k
# N

X = 1
Y = 1
Z = 1
N = 2

listy = []

for i in range(0, X+1):
    for j in range(0, Y+1):
        for k in range(0, Z+1):
            if(i + j + k != N):
               listy.append((i,j,k))

print(listy)

