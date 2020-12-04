documents = []

with open("inputs/day04.input", "r") as our_input:
    document = {}
    for line in our_input:
        if len(line) == 1:
            documents.append(document)
            document = {}
            continue

        params = line.strip().split(" ")
        for param in params:
            key, value = param.split(":")
            document[key] = value

    if len(document) > 0:
        documents.append(document)

required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid = 0
for document in documents:
    if required_keys <= document.keys():
        valid += 1

print(valid)
