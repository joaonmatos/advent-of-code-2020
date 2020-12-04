import re

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
validation_rules = [
    lambda doc: required_keys <= doc.keys(),
    lambda doc: int(doc["byr"]) in range(1920, 2003),
    lambda doc: int(doc["iyr"]) in range(2010, 2021),
    lambda doc: int(doc["eyr"]) in range(2020, 2031),
    lambda doc: re.match("^1([5-8][0-9]|9[0-3])cm$", doc["hgt"]
                         ) or re.match("^(59|6[0-9]|7[0-6])in$", doc["hgt"]),
    lambda doc: re.match("^#([0-9]|[a-f]){6}$", doc["hcl"]),
    lambda doc: doc["ecl"] in ["amb", "blu",
                               "brn", "gry", "grn", "hzl", "oth"],
    lambda doc: doc["pid"].isdigit() and len(doc["pid"]) == 9
]

num_valid = 0
for document in documents:

    valid = True
    for i, rule in enumerate(validation_rules):
        if not rule(document):
            if i == 4:
                print(document)
            valid = False
            break
    if valid:
        num_valid += 1

print(num_valid)
