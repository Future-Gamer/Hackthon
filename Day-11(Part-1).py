def split_number(n):
    """ Split a number into two halves, remove leading zeros. """
    n_str = str(n)
    mid = len(n_str) // 2
    left = int(n_str[:mid]) if n_str[:mid] != '' else 0
    right = int(n_str[mid:]) if n_str[mid:] != '' else 0
    return left, right

def blink(stones):
    """ Simulate one blink. """
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            left, right = split_number(stone)
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)
    return new_stones

def simulate(stones, blinks):
    """ Simulate multiple blinks. """
    for _ in range(blinks):
        stones = blink(stones)
    return stones

def read_stones_from_file(filename):
    """ Read the initial stones from a file. """
    with open(filename, 'r') as file:
        stones = [int(num) for num in file.read().split()]
    return stones

# Input file name
input_filename = 'day11-input.txt'
blinks = 75

# Read the initial arrangement of stones from the file
stones = read_stones_from_file(input_filename)

# Simulate the blinking
final_stones = simulate(stones, blinks)

# Output the number of stones after 25 blinks
print(f"Number of stones after {blinks} blinks: {len(final_stones)}")
