import time

def read_input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read().strip()
        return data.split()
    except FileNotFoundError:
        print("The file was not found.")
        return None

initial_stones = {}
after_five_blinks = {}

def process_input(tokens):
    for token in tokens:
        if token not in initial_stones:
            initial_stones[token] = 0
        initial_stones[token] += 1

def primitive_blink(src_stones):
    new_stones = []
    while src_stones:
        stone = src_stones.pop(0)
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            len_half = len(stone) // 2
            a = str(int(stone[:len_half]))
            b = str(int(stone[len_half:]))
            new_stones.extend([a, b])
        else:
            value = str(2024 * int(stone))
            new_stones.append(value)
    return new_stones

def memorize_after_five_blinks(stone):
    if stone in after_five_blinks:
        return
    stones = [stone]
    for _ in range(5):
        stones = primitive_blink(stones)
    after_five_blinks[stone] = stones
    for new_stone in stones:
        memorize_after_five_blinks(new_stone)

def search():
    dict_stones = initial_stones.copy()
    for _ in range(15):
        dict_stones = smart_blink(dict_stones)
    return sum(dict_stones.values())

def smart_blink(src_dict):
    new_dict = {}
    for stone, count in src_dict.items():
        children = after_five_blinks[stone]
        for child in children:
            if child not in new_dict:
                new_dict[child] = 0
            new_dict[child] += count
    return new_dict

def main():
    input_file = 'day11-input.txt'  # Specify your input file path here
    tokens = read_input_file(input_file)
    if tokens is not None:
        process_input(tokens)
        for stone in list(initial_stones.keys()):
            memorize_after_five_blinks(stone)
        print("The answer is", search())

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Execution time:", time.time() - start_time, "seconds")
