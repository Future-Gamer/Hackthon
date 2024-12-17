NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

BLOCKED = 0
VIRGIN = 1
USED = 2

map = []

width = 0
height = 0

cursor_row = 0
cursor_col = 0
direction = NORTH

def main():
    process_input()
    walk()
    print("The answer is", count_used_spots())

def process_input():
    global width, height, cursor_row, cursor_col, map
    
    with open("day6-input.txt", "r") as file:
        input_data = file.read().strip()
    
    string_map = [list(line.strip()) for line in input_data.split("\n")]
    
    height = len(string_map)
    width = len(string_map[0])
    
    for row in range(height):
        map_line = []
        for col in range(width):
            symbol = string_map[row][col]
            if symbol == "#":
                map_line.append(BLOCKED)
            elif symbol == ".":
                map_line.append(VIRGIN)
            else:
                map_line.append(USED)
                cursor_row = row
                cursor_col = col
        map.append(map_line)

def walk():
    while walk_once():
        pass

def walk_once():
    global cursor_row, cursor_col, direction
    
    if direction == NORTH:
        cursor_row -= 1
        if cursor_row < 0:
            return False
        if map[cursor_row][cursor_col] == BLOCKED:
            cursor_row += 1
            direction = EAST
            return True
        map[cursor_row][cursor_col] = USED
        return True

    if direction == SOUTH:
        cursor_row += 1
        if cursor_row >= height:
            return False
        if map[cursor_row][cursor_col] == BLOCKED:
            cursor_row -= 1
            direction = WEST
            return True
        map[cursor_row][cursor_col] = USED
        return True

    if direction == EAST:
        cursor_col += 1
        if cursor_col >= width:
            return False
        if map[cursor_row][cursor_col] == BLOCKED:
            cursor_col -= 1
            direction = SOUTH
            return True
        map[cursor_row][cursor_col] = USED
        return True

    if direction == WEST:
        cursor_col -= 1
        if cursor_col < 0:
            return False
        if map[cursor_row][cursor_col] == BLOCKED:
            cursor_col += 1
            direction = NORTH
            return True
        map[cursor_row][cursor_col] = USED
        return True

def count_used_spots():
    count = 0
    for row in range(height):
        for col in range(width):
            if map[row][col] == USED:
                count += 1
    return count

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("Execution time:", time.time() - start_time, "seconds")
