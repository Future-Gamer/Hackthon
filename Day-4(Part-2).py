def read_grid_from_file(filename):
    with open('day4-input.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def is_good_diagonal(grid, row_a, col_a, row_b, col_b):
    a = symbol_at(grid, row_a, col_a)
    b = symbol_at(grid, row_b, col_b)
    return (a == "M" and b == "S") or (a == "S" and b == "M")

def symbol_at(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return ""
    return grid[row][col]

def check_xmas_at(grid, row, col):
    if grid[row][col] != "A":
        return False
    if not is_good_diagonal(grid, row - 1, col - 1, row + 1, col + 1):
        return False
    if not is_good_diagonal(grid, row - 1, col + 1, row + 1, col - 1):
        return False
    return True

def main():
    grid = read_grid_from_file('day04-input.txt')
    xmas_count = 0
    height = len(grid)
    width = len(grid[0])

    for row in range(height):
        for col in range(width):
            if check_xmas_at(grid, row, col):
                xmas_count += 1

    print("The answer is", xmas_count)

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("Execution time:", time.time() - start_time, "seconds")
