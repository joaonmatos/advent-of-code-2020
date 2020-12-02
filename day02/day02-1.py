def process_line(line):
    policy, password = line.split(":")
    limits, char = policy.split(" ")
    lower, higher = [int(n) for n in limits.split("-")]
    return password.strip().count(char) in range(lower, higher+1)


with open("inputs/day02.input", "r") as in_file:
    count = 0
    for line in in_file:
        if process_line(line):
            count += 1
    print(count)
