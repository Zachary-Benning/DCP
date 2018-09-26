# Consider a list (list = []). You can perform the
# following commands:
#
# 1.insert i e: Insert integer e at position i.
# 2.print: Print the list.
# 3.remove e: Delete the first occurrence of integer e.
# 4.append e: Insert integer e at the end of the list.
# 5.sort: Sort the list.
# 6.pop: Pop the last element from the list.
# 7.reverse: Reverse the list.
# Initialize your list and read in the value of n
# followed by n lines of commands where each command
# will be of the 7 types listed above. Iterate through
# each command in order and perform the corresponding
# operation on your list.
#
# Input Format
#
# The first line contains an integer, n, denoting the
# number of commands.
# Each line i of the n subsequent lines contains one of
# the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
# Output Format
#
# For each command of type print, print the list on a
# new line.
# def insert_command(listz, location, value):
#     listz.insert(location, value)
#     return 0
#
#
if __name__ == '__main__':
    N = int(input())
    listz = []
    for x in range(0, N):
        command = input().split()
        if command[0] == "insert":
            listz.insert(int(command[1]), int(command[2]))
        if command[0] == "print":
            print(listz)
        if command[0] == "remove":
            listz.remove(int(command[1]))
        if command[0] == "append":
            listz.append(int(command[1]))
        if command[0] == "sort":
            listz.sort()
        if command[0] == "pop":
            listz.pop()
        if command[0] == "reverse":
            listz.reverse()

