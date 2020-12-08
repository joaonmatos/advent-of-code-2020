

def test_program(program, tested_index):
    acc = 0
    ic = 0
    executed = set()
    loop = False

    while ic < len(program):
        if ic in executed:
            loop = True
            break
        executed.add(ic)

        op, arg = program[ic]
        if ic == tested_index and op != "acc":
            op = "nop" if op == "jmp" else "jmp"
        if op == "acc":
            acc += arg
            ic += 1
        elif op == "jmp":
            ic += arg
        elif op == "nop":
            ic += 1

    return loop, ic, acc


input_file = open("inputs/day08.input")
program = [line.strip().split(" ") for line in input_file]
input_file.close()
program = [(line[0], int(line[1])) for line in program]

for i in range(0, len(program)):
    loop, ic, acc = test_program(program, i)
    if not loop:
        print(loop, i, acc)
