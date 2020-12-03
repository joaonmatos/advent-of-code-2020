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

our_input = open("inputs/day03.input", "r").readlines()

result = check_slope((3, 1), our_input)
print(result)
