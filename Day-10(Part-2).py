import time

def read_map(file_name):
    with open(file_name, 'r') as file:
        topo_map = [list(map(int, line.strip())) for line in file.readlines()]
    return topo_map

def create_cell(digit):
    return {
        "height": int(digit),
        "trailheads": []
    }

def process_input(input_data):
    table = []
    for line in input_data.split('\n'):
        row = [create_cell(digit) for digit in line.strip()]
        table.append(row)
    
    width = len(table[0])
    height = len(table)
    return table, width, height

def start_trails(table, height, width):
    for row in range(height):
        for col in range(width):
            cell = table[row][col]
            if cell["height"] != 0:
                continue
            cell["trailheads"].append(f"{row}~{col}")

def continue_trails(table, height, width):
    for target_height in range(9):
        continue_trails_from(table, target_height, height, width)

def continue_trails_from(table, target_height, height, width):
    for row in range(height):
        for col in range(width):
            cell = table[row][col]
            if cell["height"] != target_height:
                continue
            
            continue_trail_this(table, target_height + 1, cell["trailheads"], row - 1, col, height, width)
            continue_trail_this(table, target_height + 1, cell["trailheads"], row + 1, col, height, width)
            continue_trail_this(table, target_height + 1, cell["trailheads"], row, col - 1, height, width)
            continue_trail_this(table, target_height + 1, cell["trailheads"], row, col + 1, height, width)

def continue_trail_this(table, target_height, trailheads, row, col, height, width):
    if row < 0 or col < 0 or row >= height or col >= width:
        return
    
    cell = table[row][col]
    if cell["height"] != target_height:
        return
    
    for trailhead in trailheads:
        cell["trailheads"].append(f"{trailhead}|{row}~{col}")

def count_ratings(table, height, width):
    ratings = 0
    for row in range(height):
        for col in range(width):
            cell = table[row][col]
            if cell["height"] == 9:
                ratings += len(cell["trailheads"])
    return ratings

def main():
    with open("day10-input.txt", 'r') as file:
        input_data = file.read().strip()
    
    table, width, height = process_input(input_data)
    start_trails(table, height, width)
    continue_trails(table, height, width)
    
    answer = count_ratings(table, height, width)
    print("the answer is", answer)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"execution time: {time.time() - start_time:.2f} seconds")
