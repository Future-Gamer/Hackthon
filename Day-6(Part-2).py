NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

map = []

width = 0
height = 0

home_row = 0
home_col = 0
cursor_row = 0
cursor_col = 0
direction = NORTH

count_of_loop_paths = 0

current_walk = 0

original_path = []

tested_cells = {}

def main():
    process_input()
    walk_original_path()
    walk_candidate_maps()
    print("The answer is", count_of_loop_paths)

def process_input():
    global width, height, home_row, home_col, cursor_row, cursor_col, map
    
    with open("day6-input.txt", "r") as file:
        input_data = file.read().strip()
    
    string_map = [line.strip() for line in input_data.split("\n")]
    
    height = len(string_map)
    width = len(string_map[0])
    
    for row in range(height):
        map_line = []
        map.append(map_line)
        
        for col in range(width):
            cell = create_cell()
            map_line.append(cell)
            
            symbol = string_map[row][col]
            if symbol == "#":
                cell["blocked"] = True
                continue
            if symbol == ".":
                continue
            
            home_row = row
            home_col = col
            cursor_row = row
            cursor_col = col

def create_cell():
    return {
        "walk_id": 0,
        "blocked": False,
        "walked_north": False,
        "walked_south": False,
        "walked_east": False,
        "walked_west": False
    }

def walk_original_path():
    while walk_original_path_once():
        pass

def walk_original_path_once():
    global cursor_row, cursor_col, direction
    
    original_path.append({"row": cursor_row, "col": cursor_col, "direction": direction})
    
    if direction == NORTH:
        cursor_row -= 1
        if cursor_row < 0:
            return False
        if map[cursor_row][cursor_col]["blocked"]:
            cursor_row += 1
            direction = EAST
        return True

    if direction == SOUTH:
        cursor_row += 1
        if cursor_row >= height:
            return False
        if map[cursor_row][cursor_col]["blocked"]:
            cursor_row -= 1
            direction = WEST
        return True

    if direction == EAST:
        cursor_col += 1
        if cursor_col >= width:
            return False
        if map[cursor_row][cursor_col]["blocked"]:
            cursor_col -= 1
            direction = SOUTH
        return True

    if direction == WEST:
        cursor_col -= 1
        if cursor_col < 0:
            return False
        if map[cursor_row][cursor_col]["blocked"]:
            cursor_col += 1
            direction = NORTH
        return True

def walk_candidate_maps():
    global count_of_loop_paths
    
    home_id = f"{home_row}~{home_col}"
    tested_cells[home_id] = True  # avoids blocking home (later)
    
    while True:
        previous_cell = original_path.pop(0)
        blocking_cell = original_path[0] if original_path else None
        
        if blocking_cell is None:
            return
        
        blocking_cell_id = f"{blocking_cell['row']}~{blocking_cell['col']}"
        
        if blocking_cell_id in tested_cells:
            continue
        
        tested_cells[blocking_cell_id] = True
        map[blocking_cell["row"]][blocking_cell["col"]]["blocked"] = True
        
        walk_candidate_map(previous_cell["row"], previous_cell["col"], previous_cell["direction"])
        
        map[blocking_cell["row"]][blocking_cell["col"]]["blocked"] = False

def walk_candidate_map(start_row, start_col, start_direction):
    global cursor_row, cursor_col, direction, current_walk, count_of_loop_paths
    
    cursor_row = start_row
    cursor_col = start_col
    direction = start_direction
    
    current_walk += 1
    
    while True:
        status = walk_candidate_map_segment()
        
        if status == "out":
            return
        
        if status == "loop":
            count_of_loop_paths += 1
            return

def walk_candidate_map_segment():
    if direction == NORTH:
        return walk_candidate_map_north()
    if direction == SOUTH:
        return walk_candidate_map_south()
    if direction == EAST:
        return walk_candidate_map_east()
    if direction == WEST:
        return walk_candidate_map_west()

def walk_candidate_map_north():
    global cursor_row, direction
    
    while True:
        cursor_row -= 1
        if cursor_row < 0:
            cursor_row += 1
            return "out"
        
        next_cell = map[cursor_row][cursor_col]
        if not next_cell["blocked"]:
            continue
        
        cursor_row += 1
        current_cell = map[cursor_row][cursor_col]
        maybe_reset_cell(current_cell)
        
        if current_cell["walked_north"]:
            return "loop"
        
        current_cell["walked_north"] = True
        direction = EAST
        return ""

def walk_candidate_map_south():
    global cursor_row, direction
    
    while True:
        cursor_row += 1
        if cursor_row == height:
            cursor_row -= 1
            return "out"
        
        next_cell = map[cursor_row][cursor_col]
        if not next_cell["blocked"]:
            continue
        
        cursor_row -= 1
        current_cell = map[cursor_row][cursor_col]
        maybe_reset_cell(current_cell)
        
        if current_cell["walked_south"]:
            return "loop"
        
        current_cell["walked_south"] = True
        direction = WEST
        return ""

def walk_candidate_map_east():
    global cursor_col, direction
    
    while True:
        cursor_col += 1
        if cursor_col == width:
            cursor_col -= 1
            return "out"
        
        next_cell = map[cursor_row][cursor_col]
        if not next_cell["blocked"]:
            continue
        
        cursor_col -= 1
        current_cell = map[cursor_row][cursor_col]
        maybe_reset_cell(current_cell)
        
        if current_cell["walked_east"]:
            return "loop"
        
        current_cell["walked_east"] = True
        direction = SOUTH
        return ""

def walk_candidate_map_west():
    global cursor_col, direction
    
    while True:
        cursor_col -= 1
        if cursor_col < 0:
            cursor_col += 1
            return "out"
        
        next_cell = map[cursor_row][cursor_col]
        if not next_cell["blocked"]:
            continue
        
        cursor_col += 1
        current_cell = map[cursor_row][cursor_col]
        maybe_reset_cell(current_cell)
        
        if current_cell["walked_west"]:
            return "loop"
        
        current_cell["walked_west"] = True
        direction = NORTH
        return ""

def maybe_reset_cell(cell):
    global current_walk
    
    if cell["walk_id"] == current_walk:
        return
    
    cell["walk_id"] = current_walk
    cell["walked_north"] = False
    cell["walked_south"] = False
    cell["walked_east"] = False
    cell["walked_west"] = False

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("Execution time:", time.time() - start_time, "seconds")
