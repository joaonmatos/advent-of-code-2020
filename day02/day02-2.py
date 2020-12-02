def process_line(line):
    policy, password = line.split(":")
    password = password.strip()
    limits, char = policy.split(" ")
    lower, higher = [int(n) - 1 for n in limits.split("-")]
    return (password[lower] == char) != (password[higher] == char)


with open("inputs/day02.input", "r") as in_file:
    count = 0
    for line in in_file:
        if process_line(line):
            count += 1
    print(count)
