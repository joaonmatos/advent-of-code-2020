input_file = open("inputs/day08.input")
program = [line.strip().split(" ") for line in input_file]
input_file.close()
program = [(line[0], int(line[1])) for line in program]

acc = 0
ic = 0

executed = set()

while ic < len(program):
    if ic in executed:
        print(ic, acc)
        break
    executed.add(ic)

    op, arg = program[ic]
    if op == "acc":
        acc += arg
        ic += 1
    elif op == "jmp":
        ic += arg
    elif op == "nop":
        ic += 1
