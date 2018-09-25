# Given the names and grades for each student in a
# Physics class of N students, store them in a nested
# list and print the name(s) of any student(s) having
# the second lowest grade.

# Note: If there are multiple students with the same
# grade, order their names alphabetically and print
# each name on a new line.

#2<=N<=5
#There will always be one or more students having
# the second lowest grade.

# Print the name(s) of any student(s) having the
# second lowest grade in Physics; if there are
# multiple students, order their names
# alphabetically and print each one on a new line.

if __name__ == '__main__':
    number_of_students = int(input())
    students_name_grades = []
    for _ in range(number_of_students):
        name = input()
        score = float(input())
        students_name_grades.append((name, score))
    score_roster = []
    for x in range(0, number_of_students):
        score_roster.append(students_name_grades[x][1])
    worst_score = min(score_roster)
    while worst_score == min(score_roster):
        score_roster.remove(min(score_roster))
    second_min = min(score_roster)
    list_students_second_last_names = []

    for x in range(0, number_of_students):
        if students_name_grades[x][1] == second_min:
            list_students_second_last_names.append(students_name_grades[x][0])
    solution = sorted(list_students_second_last_names)
    for x in range(0, len(solution)):
        print(solution[x])

