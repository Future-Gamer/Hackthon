width = 101
height = 103

map_grid = []

all_guards = []

time = 0


def main():
    global time

    process_input()

    set_map()
    
    while True:
        time += 1    
        clashes = move_guards()

        if not clashes:
            show_map()
            break
    
    print("If there is a xmas tree in the picture above, the answer is", time)        


def process_input():
    with open("day14-input.txt", "r") as file:
        lines = file.read().strip().split("\n")
    
    for line in lines:
        parts = line.strip().split(" ")
        
        tokens_p = parts[0][2:].split(",")
        tokens_v = parts[1][2:].split(",")
        
        pos_x = int(tokens_p[0])
        pos_y = int(tokens_p[1])
        vel_x = int(tokens_v[0])
        vel_y = int(tokens_v[1])
        
        guard = { "posX": pos_x, "posY": pos_y, "velX": vel_x, "velY": vel_y }
        
        all_guards.append(guard)


def set_map():
    global map_grid

    for row in range(height):
        line = [0] * width
        map_grid.append(line)


def move_guards():
    for guard in all_guards:
        clashes = move_guard(guard)
        
        if clashes:
            return True 
    return False


def move_guard(guard):
    global time, map_grid
                
    brute_x = guard["posX"] + (time * guard["velX"])
    brute_y = guard["posY"] + (time * guard["velY"])
    
    final_x = brute_x % width
    if final_x < 0:
        final_x += width
    
    final_y = brute_y % height
    if final_y < 0:
        final_y += height
    
    if map_grid[final_y][final_x] == time:
        return True
    
    map_grid[final_y][final_x] = time
    
    return False


def show_map():
    global map_grid, time

    print("")
    
    for line in map_grid:
        s = ""
        for number in line:
            s += "X" if number == time else "."
        print(s)
    print("")


if __name__ == "__main__":
    main()
