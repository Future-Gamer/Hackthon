# Solution for https://adventofcode.com/2024/day/15 part 1
# Expecting all map borders to be blocked ("#")

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

input_data = read_input_file("day15-input.txt")

map_data = []
width = 0
height = 0

bot_row = 0
bot_col = 0

guide = ""

def main():
    process_input()
    walk()
    print("the answer is", count_boxes_gps())

def process_input():
    global width, height, bot_row, bot_col, guide

    sections = input_data.split("\n\n")
    
    raw_map = sections.pop(0).strip()
    
    raw_lines = raw_map.split("\n")
    
    for raw_line in raw_lines:
        map_data.append(list(raw_line.strip()))
    
    height = len(map_data)
    width = len(map_data[0])
    
    raw_guide = sections.pop(0).strip()
    
    for segment in raw_guide.split("\n"):
        guide += segment.strip()
    
    for row in range(width):
        for col in range(height):
            if map_data[row][col] == "@":
                bot_row = row
                bot_col = col
                return

def walk():
    for direction in guide:
        if direction == "^":
            walk_to(-1, 0)
        elif direction == "v":
            walk_to(1, 0)
        elif direction == ">":
            walk_to(0, 1)
        elif direction == "<":
            walk_to(0, -1)

def walk_to(delta_row, delta_col):
    global bot_row, bot_col

    future_row = bot_row
    future_col = bot_col
    
    while True:
        future_row += delta_row
        future_col += delta_col
    
        future_spot = map_data[future_row][future_col]

        if future_spot == "#":
            return
    
        if future_spot == ".":
            break
    
    while True:
        previous_row = future_row - delta_row
        previous_col = future_col - delta_col
    
        map_data[future_row][future_col] = map_data[previous_row][previous_col]

        future_row = previous_row
        future_col = previous_col
        
        if future_row == bot_row and future_col == bot_col:
            break

    map_data[bot_row][bot_col] = "."
    bot_row += delta_row
    bot_col += delta_col

def count_boxes_gps():
    gps = 0
    for row in range(width):
        for col in range(height):
            if map_data[row][col] == "O":
                gps += 100 * row + col
    return gps

def show_map():
    for line in map_data:
        print("".join(line))

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print(f"execution time: {time.time() - start_time:.4f}ms")
