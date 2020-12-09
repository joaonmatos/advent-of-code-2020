class BoundedQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.list = [None] * self.capacity
        self.start_index = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        index = self.actual_index(self.start_index + self.size)
        if not self.is_full():
            self.size += 1
        else:
            self.start_index = self.actual_index(self.start_index + 1)
        self.list[index] = element

    def pop(self):
        if self.is_empty():
            return
        self.size -= 1
        self.start_index = self.actual_index(self.start_index + 1)

    def front(self):
        if self.is_empty():
            return None
        return self.list[self.start_index]

    def actual_index(self, index):
        return index if index < self.capacity else index - self.capacity

    def __iter__(self):
        if self.start_index + self.size < self.capacity:
            return self.list[self.start_index:self.start_index + size]
        else:
            return self.list[self.start_index:] + self.list[:self.actual_index(self.start_index + self.size)]


input_file = open("inputs/day09.input")
our_input = [int(line) for line in input_file]
input_file.close()

last_seen = BoundedQueue(25)
preamble = our_input[:25]
rest = our_input[25:]
for item in preamble:
    last_seen.push(item)

for item in rest:
    sums = set()
    for i, e1 in enumerate(last_seen.__iter__()):
        for e2 in last_seen.__iter__()[i:]:
            sums.add(e1 + e2)
    if item not in sums:
        print(item)
        break
    last_seen.push(item)
