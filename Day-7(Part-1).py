import time

answer = 0

def main():
    process_input()
    print("The answer is", answer)

def process_input():
    global answer
    
    with open("day7-input.txt", "r") as file:
        input_data = file.read().strip()
    
    lines = input_data.split("\n")
    
    for line in lines:
        parts = line.strip().split(":")
        target = int(parts.pop(0))
        tokens = parts.pop(0).strip().split(" ")
        operands = [int(token) for token in tokens]
        operand = operands.pop(0)
        
        if check_math(target, operands[:], operand, "+"):
            answer += target
            continue
        
        if check_math(target, operands[:], operand, "*"):
            answer += target
            continue

def check_math(target, operands, result, operator):
    operand = operands.pop(0)
    
    if operator == "+":
        result += operand
    else:
        result *= operand
    
    if result > target:
        return False
    
    if not operands:
        return target == result
    
    if check_math(target, operands[:], result, "+"):
        return True
    if check_math(target, operands[:], result, "*"):
        return True
    
    return False

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Execution time:", time.time() - start_time, "seconds")
