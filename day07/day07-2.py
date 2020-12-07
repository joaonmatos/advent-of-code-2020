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


def graph_find_num_children(color, graph):
    children = graph[color]
    count = 0
    for tup in children:
        num, child_color = tup
        grandchildren = graph_find_num_children(child_color, graph)
        count += num * (1 + grandchildren)
    return count


input_file = open("inputs/day07.input", "r")
input_text = input_file.read()
input_file.close()
lines = input_text.rstrip().splitlines()

graph = {}
for line in lines:
    outer, inner = extract_line_contents(line)
    graph[outer] = frozenset(inner)

print(graph_find_num_children("shiny gold", graph))
