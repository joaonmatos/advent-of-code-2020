import sys

input_file = open("inputs/day01.input", "r")
numbers = [int(line) for line in input_file]
numbers.sort()

for i in range(0, len(numbers)):
    number = numbers[i]

    for j in range(i+1, len(numbers)):
        other = numbers[j]
        if number + other >= 2020:
            break

        for other2 in numbers[j+1:]:
            if number + other + other2 == 2020:
                print(number, other, other2)
                sys.exit(0)
            elif number + other + other2 > 2020:
                break
