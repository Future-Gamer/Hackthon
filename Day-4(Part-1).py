def read_grid_from_file(filename):
    with open('day4-input.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def got_match(grid, row, col, symbol):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return False
    return grid[row][col] == symbol

def check_xmas_to_east(grid, row, col):
    if got_match(grid, row, col + 1, "M") and got_match(grid, row, col + 2, "A") and got_match(grid, row, col + 3, "S"):
        return True
    return False

def check_xmas_to_west(grid, row, col):
    if got_match(grid, row, col - 1, "M") and got_match(grid, row, col - 2, "A") and got_match(grid, row, col - 3, "S"):
        return True
    return False

def check_xmas_to_north(grid, row, col):
    if got_match(grid, row - 1, col, "M") and got_match(grid, row - 2, col, "A") and got_match(grid, row - 3, col, "S"):
        return True
    return False

def check_xmas_to_south(grid, row, col):
    if got_match(grid, row + 1, col, "M") and got_match(grid, row + 2, col, "A") and got_match(grid, row + 3, col, "S"):
        return True
    return False

def check_xmas_to_northeast(grid, row, col):
    if got_match(grid, row - 1, col + 1, "M") and got_match(grid, row - 2, col + 2, "A") and got_match(grid, row - 3, col + 3, "S"):
        return True
    return False

def check_xmas_to_northwest(grid, row, col):
    if got_match(grid, row - 1, col - 1, "M") and got_match(grid, row - 2, col - 2, "A") and got_match(grid, row - 3, col - 3, "S"):
        return True
    return False

def check_xmas_to_southeast(grid, row, col):
    if got_match(grid, row + 1, col + 1, "M") and got_match(grid, row + 2, col + 2, "A") and got_match(grid, row + 3, col + 3, "S"):
        return True
    return False

def check_xmas_to_southwest(grid, row, col):
    if got_match(grid, row + 1, col - 1, "M") and got_match(grid, row + 2, col - 2, "A") and got_match(grid, row + 3, col - 3, "S"):
        return True
    return False

def check_xmas_at(grid, row, col):
    if grid[row][col] != "X":
        return False
    if check_xmas_to_east(grid, row, col) or check_xmas_to_west(grid, row, col) or check_xmas_to_north(grid, row, col) or check_xmas_to_south(grid, row, col) or check_xmas_to_northeast(grid, row, col) or check_xmas_to_northwest(grid, row, col) or check_xmas_to_southeast(grid, row, col) or check_xmas_to_southwest(grid, row, col):
        return True
    return False

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
