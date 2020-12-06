input_file = open("inputs/day06.input")
as_str = input_file.read()
input_file.close()

split_groups = as_str.split("\n\n")
our_input = [group.strip().split("\n") for group in split_groups]


def questions_answered(group):
    if len(group) == 0:
        return 0
    common = set([char for char in group[0]])

    for person in group[1:]:
        answered = set([char for char in person])
        common &= answered

    return len(common)


print(sum(map(questions_answered, our_input)))
