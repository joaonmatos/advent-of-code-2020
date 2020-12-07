def extract_inner_contents(inner):

    if inner == "no other bags.":
        return []
    as_list = inner.split(", ")
    stripped = []
    for bag in as_list:
        if bag[-1] == ".":
            bag = bag[:len(bag) - 1]
        if bag[-1] == "s":
            bag = bag[:len(bag) - 1]
        bag = bag.replace(" bag", "")
        stripped.append(bag)

    for i in range(0, len(stripped)):
        processed = stripped[i].split(" ")
        if len(processed) < 3:
            print(processed)
        stripped[i] = (int(processed[0]) if processed[0] != "no" else 0, " ".join(
            [processed[1], processed[2]]))
    return stripped


def extract_line_contents(line):
    outer, inner = line.split(" contain ")
    if outer[-1] == "s":
        outer = outer[:len(outer) - 1]
    outer = outer.replace(" bag", "")
    inner = extract_inner_contents(inner)
    return outer, inner


def graph_find_color(color, graph, key):
    if key == color:
        return True
    children = graph[key]
    for tup in children:
        _, child_color = tup
        if graph_find_color(color, graph, child_color):
            return True
    return False


input_file = open("inputs/day07.input", "r")
input_text = input_file.read()
input_file.close()
lines = input_text.rstrip().splitlines()

graph = {}
for line in lines:
    outer, inner = extract_line_contents(line)
    graph[outer] = frozenset(inner)

count = 0
for key in graph:
    if graph_find_color("shiny gold", graph, key):
        count += 1

print(count)
# NOTE, it is one too high because of the entry for the shiny gold key
