# Write a generator function cycle_items(iterable, count) that cycles through
# the items of an iterable a specified number of times.
def cycle_items(iterable, count):
    for _ in range(count):
        for item in iterable:
            yield item


for nr in cycle_items([2, 3, 7], 3):
    print(nr, end=" ")
print()

# Write a generator expression that cycles through the items of an iterable a
# specified number of times (the iterable and the number of times can be chosen
# arbitrarily).
names = ["Jane", "Anna", "Mike"]
cycle_names = (name for _ in range(2) for name in names)
for name in cycle_names:
    print(name, end=" ")
print()


# Write a generator function infinite_counter(start=0, step=1) that generates
# an infinite sequence of numbers, starting from the given start value and
# increasing by step with each iteration. From outside, iterate it in a loop
# that stops after 10 cycles.
def infinite_counter(start=0, step=1):
    while True:
        yield start
        start += step


counter = infinite_counter(step=3)
for _ in range(10):
    print(next(counter), end=" ")
print()


# Write a generator function read_file_in_chunks(filename, chunk_size) that
# reads a large file in chunks of the given size. Assume the file contains
# text data.
def read_file_in_chunks(filename, chunk_size):
    with open(filename) as f:
        while chunk := f.read(chunk_size):
            yield chunk


for file_chunk in read_file_in_chunks("input.txt", 20):
    print(file_chunk)
