input_file = open("inputs/day06.input")
as_str = input_file.read()
input_file.close()

split_groups = as_str.split("\n\n")
our_input = [group.strip().split("\n") for group in split_groups]


def questions_answered(group):
    answered = set()

    for person in group:
        for question in person:
            answered.add(question)

    return len(answered)


print(sum(map(questions_answered, our_input)))
