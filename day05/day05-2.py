max_id = -1
our_input = open("inputs/day05.input", "r")

seats = [True] * (128 * 8)

for seat in our_input:
    id_binary = seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    id_int = int(id_binary, base=2)
    seats[id_int] = False

for i, free in enumerate(seats):
    if i == 0:
        if free and not seats[1]:
            print(0)
    elif i == len(seats) - 1:
        if free and not seats[len(seats) - 2]:
            print(len(seats) - 1)
    elif free and not seats[i - 1] and not seats[i + 1]:
        print(i)

