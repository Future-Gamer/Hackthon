from collections import defaultdict, deque

# Function to read the input file and create the grid
def read_input(file_path):
    with open(file_path, 'r') as file:
        garden = [line.strip() for line in file]
    return garden

# Initialize variables
garden = []
processed = []
width = 0
height = 0
current_symbol = ""
area_size = 0
top_border_plots = defaultdict(list)  # by row
bottom_border_plots = defaultdict(list)  # by row
left_border_plots = defaultdict(list)  # by col
right_border_plots = defaultdict(list)  # by col
result = 0

def main():
    global garden, processed, width, height, result

    process_input()

    for row in range(height):
        for col in range(width):
            process_plot(row, col)
    
    print("The answer is", result)

def process_input():
    global garden, processed, width, height

    garden = read_input('day12-input.txt')

    height = len(garden)
    width = len(garden[0])

    processed = [[False] * width for _ in range(height)]

def process_plot(row, col):
    global current_symbol, area_size, top_border_plots, bottom_border_plots, left_border_plots, right_border_plots, result

    if processed[row][col]:
        return
    
    processed[row][col] = True

    current_symbol = garden[row][col]
    area_size = 0
    top_border_plots = defaultdict(list)
    bottom_border_plots = defaultdict(list)
    left_border_plots = defaultdict(list)
    right_border_plots = defaultdict(list)
    
    walk_from(row, col)
    
    result += area_size * find_number_of_sides()

def walk_from(row, col):
    points_to_walk = deque([create_point(row, col)])
    
    while points_to_walk:
        point = points_to_walk.pop()
        
        if point is None:
            return
        
        global area_size
        area_size += 1
        
        row = point['row']
        col = point['col']

        try_catch_neighbor(row, col, -1,  0, points_to_walk)
        try_catch_neighbor(row, col,  1,  0, points_to_walk)
        try_catch_neighbor(row, col,  0, -1, points_to_walk)
        try_catch_neighbor(row, col,  0,  1, points_to_walk)

def try_catch_neighbor(base_row, base_col, delta_row, delta_col, points_to_walk):
    neighbor_row = base_row + delta_row
    neighbor_col = base_col + delta_col

    if neighbor_row < 0:
        push_to_top_border_plots(base_row, base_col)
        return
    if neighbor_col < 0:
        push_to_left_border_plots(base_row, base_col)
        return
    if neighbor_row == height:
        push_to_bottom_border_plots(base_row, base_col)
        return
    if neighbor_col == width:
        push_to_right_border_plots(base_row, base_col)
        return
    
    if garden[neighbor_row][neighbor_col] != current_symbol:
        if neighbor_row < base_row:
            push_to_top_border_plots(base_row, base_col)
            return
        if neighbor_col < base_col:
            push_to_left_border_plots(base_row, base_col)
            return
        if neighbor_row > base_row:
            push_to_bottom_border_plots(base_row, base_col)
            return
        if neighbor_col > base_col:
            push_to_right_border_plots(base_row, base_col)
            return
    
    if processed[neighbor_row][neighbor_col]:
        return

    processed[neighbor_row][neighbor_col] = True
    points_to_walk.append(create_point(neighbor_row, neighbor_col))

def create_point(row, col):
    return {"row": row, "col": col}

def push_to_top_border_plots(row, col):
    top_border_plots[row].append(col)

def push_to_bottom_border_plots(row, col):
    bottom_border_plots[row].append(col)

def push_to_left_border_plots(row, col):
    left_border_plots[col].append(row)

def push_to_right_border_plots(row, col):
    right_border_plots[col].append(row)

def find_number_of_sides():
    sides = 0
    for border_plots in [top_border_plots, bottom_border_plots, left_border_plots, right_border_plots]:
        sides += find_number_of_sides_this(border_plots)
    return sides

def find_number_of_sides_this(border_plots):
    sides = 0
    for col_list in border_plots.values():
        sides += find_number_of_sides_this_list(col_list)
    return sides

def find_number_of_sides_this_list(col_list):
    col_list.sort()
    new_list = []
    
    while col_list:
        candidate = col_list.pop(0)
        previous = new_list[-1] if new_list else None
        
        if previous is None:
            new_list.append(candidate)
        elif candidate - previous == 1:
            new_list.pop()
        
        new_list.append(candidate)
    
    return len(new_list)

if __name__ == "__main__":
    main()
