import re

def extract_and_multiply(memory):
    # Regular expression to find valid mul instructions
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, memory)
    
    total = 0
    for match in matches:
        x, y = map(int, match)
        total += x * y
    
    return total

# Read the corrupted memory from input.txt
with open('day3-input.txt', 'r') as file:
    corrupted_memory = file.read()

# Calculate the total of valid mul instructions
result = extract_and_multiply(corrupted_memory)
print("Total of valid mul instructions:", result)
