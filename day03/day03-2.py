def check_slope(slope, input_file):
    hor_offset, vert_offset = slope
    hor_cursor = 0
    trees = 0
    for line in our_input[::vert_offset]:
        if line[hor_cursor] == "#":
            trees += 1
        hor_cursor += hor_offset
        hor_cursor %= len(line) - 1
    return trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
our_input = open("inputs/day03.input", "r").readlines()

results = [check_slope(slope, our_input) for slope in slopes]
print(results)

acc = 1
for result in results:
    acc *= result
print(acc)
