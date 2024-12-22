from collections import defaultdict

def read_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def find_regions(garden_map):
    rows, cols = len(garden_map), len(garden_map[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = defaultdict(list)

    def dfs(r, c, plant_type):
        stack = [(r, c)]
        area = 0
        perimeter = 0
        while stack:
            x, y = stack.pop()
            if not (0 <= x < rows and 0 <= y < cols) or visited[x][y] or garden_map[x][y] != plant_type:
                continue
            visited[x][y] = True
            area += 1
            region.append((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and garden_map[nx][ny] == plant_type:
                    stack.append((nx, ny))
                else:
                    perimeter += 1
        return area, perimeter

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = garden_map[r][c]
                region = []
                area, perimeter = dfs(r, c, plant_type)
                regions[plant_type].append((area, perimeter))
    
    return regions

def calculate_price(regions):
    total_price = 0
    for plant_type, region_data in regions.items():
        for area, perimeter in region_data:
            total_price += area * perimeter
    return total_price

def main():
    garden_map = read_map('day12-input.txt')
    regions = find_regions(garden_map)
    total_price = calculate_price(regions)
    print(f'Total price for fencing all regions: {total_price}')

if __name__ == "__main__":
    main()
