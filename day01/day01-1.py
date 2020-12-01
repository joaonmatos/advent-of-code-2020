import sys

input_file = open("inputs/day01.input", "r")
numbers = [int(line) for line in input_file]
numbers.sort()

for i in range(0, len(numbers)):
    number = numbers[i]
    for other in numbers[i+1:]:
        if number + other == 2020:
            print(number, other)
            sys.exit(0)
        elif other + number > 2020:
            break
