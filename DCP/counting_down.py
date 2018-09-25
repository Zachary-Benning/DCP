def counting_down(natural_number):
    counter = 1
    natural_number = int(natural_number)
    while counter != natural_number:
        print(counter, end="")
        counter += 1
    print(natural_number)


if __name__ == '__main__':
    n = int(input())
    counting_down(n)
