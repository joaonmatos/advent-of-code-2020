max_id = -1
our_input = open("inputs/day05.input", "r")

for seat in our_input:
    front, back = 0, 128
    left, right = 0, 8

    for char in seat:
        if char == "F":
            back -= (back - front) // 2
        elif char == "B":
            front += (back - front) // 2
        elif char == "L":
            right -= (right - left) // 2
        elif char == "R":
            left += (right - left) // 2
    
    if front * 8 + left > max_id:
        max_id = front * 8 + left

print(max_id)

