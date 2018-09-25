if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    average_score = 0
    for x in range(0,3):
        average_score += student_marks[query_name][x]
    average_score = average_score/3.00
    print('{0:.2f}'.format(average_score))