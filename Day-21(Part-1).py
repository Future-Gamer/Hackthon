import itertools
from collections import deque

# Define keypads
numeric_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]

directional_keypad = [
    ['^', 'A'],
    ['<', 'v', '>']
]

# Function to find the position of a key in the keypad
def find_position(keypad, key):
    for row in range(len(keypad)):
        for col in range(len(keypad[row])):
            if keypad[row][col] == key:
                return (row, col)
    return None

# Function to find the shortest path using BFS
def bfs(start, target, keypad):
    queue = deque([(start, "")])
    visited = set()
    visited.add(start)
    
    while queue:
        (current_pos, path) = queue.popleft()
        if current_pos == target:
            return path + "A"
        
        for move, direction in [((-1, 0), '^'), ((1, 0), 'v'), ((0, -1), '<'), ((0, 1), '>')]:
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            if (0 <= new_pos[0] < len(keypad) and 0 <= new_pos[1] < len(keypad[0])
                and keypad[new_pos[0]][new_pos[1]] != ' ' and new_pos not in visited):
                visited.add(new_pos)
                queue.append((new_pos, path + direction))
    
    return None

# Function to calculate the shortest sequence of button presses
def shortest_sequence(code, keypad):
    sequence = ""
    start_pos = find_position(keypad, 'A')
    for key in code:
        target_pos = find_position(keypad, key)
        path = bfs(start_pos, target_pos, keypad)
        sequence += path
        start_pos = target_pos
    return sequence

# Function to calculate the complexity of a code
def calculate_complexity(code, sequence_length):
    numeric_part = int(code[:-1])  # excluding the 'A'
    return sequence_length * numeric_part

# Main function to read input file and calculate total complexity
def main(input_file):
    total_complexity = 0
    
    with open(input_file, 'r') as file:
        codes = file.read().strip().split()
        
        for code in codes:
            sequence = shortest_sequence(code, numeric_keypad)
            sequence_length = len(sequence)
            complexity = calculate_complexity(code, sequence_length)
            total_complexity += complexity
    
    print(f"Total Complexity: {total_complexity}")

# Call main function with input file
if __name__ == "__main__":
    main('day21-input.txt')
