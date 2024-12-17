from collections import deque

def read_map(file_name):
    with open(file_name, 'r') as file:
        topo_map = [list(map(int, line.strip())) for line in file.readlines()]
    return topo_map

def is_valid(x, y, topo_map):
    return 0 <= x < len(topo_map) and 0 <= y < len(topo_map[0])

def find_paths(x, y, topo_map, target=9):
    if topo_map[x][y] != 0:
        return 0
    
    queue = deque([(x, y, 0)])  # (x, y, height)
    visited = set([(x, y)])
    score = 0
    
    while queue:
        cx, cy, height = queue.popleft()
        
        if height == target:
            score += 1
            continue
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny, topo_map) and (nx, ny) not in visited and topo_map[nx][ny] == height + 1:
                visited.add((nx, ny))
                queue.append((nx, ny, height + 1))
    
    return score

def calculate_scores(topo_map):
    scores = []
    for x in range(len(topo_map)):
        for y in range(len(topo_map[0])):
            if topo_map[x][y] == 0:  # Only start from trailheads (height 0)
                score = find_paths(x, y, topo_map)
                if score > 0:
                    scores.append(score)
    return scores

def sum_of_scores(file_name):
    topo_map = read_map(file_name)
    scores = calculate_scores(topo_map)
    return sum(scores)

# Usage example:
file_name = 'day10-input.txt'
print(sum_of_scores(file_name))
