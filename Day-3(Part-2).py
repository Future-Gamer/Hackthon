import re

def extract_and_multiply(memory):
    # Regular expressions to find valid mul, do, and don't instructions
    mul_pattern = r'mul\((\d+),(\d+)\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    # Split the memory into tokens
    tokens = re.split(r'(\bdo\(\)|\bdon\'t\(\)|mul\(\d+,\d+\))', memory)
    
    total = 0
    enabled = True
    
    for token in tokens:
        if re.match(do_pattern, token):
            enabled = True
        elif re.match(dont_pattern, token):
            enabled = False
        elif re.match(mul_pattern, token):
            if enabled:
                x, y = map(int, re.findall(r'\d+', token))
                total += x * y
    
    return total

# Read the corrupted memory from input.txt
with open('day3-input.txt', 'r') as file:
    corrupted_memory = file.read()

# Calculate the total of valid and enabled mul instructions
result = extract_and_multiply(corrupted_memory)
print("Total of valid and enabled mul instructions:", result)
