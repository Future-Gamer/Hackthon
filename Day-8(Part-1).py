import time

map = []

all_antennas = {}

width = 0
height = 0

all_antinodes = {}

def main():
    process_input()
    
    symbols = list(all_antennas.keys())
    
    for symbol in symbols:
        find_antinodes(all_antennas[symbol])
    
    print("The answer is", len(all_antinodes))

def process_input():
    global width, height
    
    with open("day8-input.txt", "r") as file:
        input_data = file.read().strip()
    
    lines = input_data.split("\n")
    
    row = -1
    
    for raw_line in lines:
        row += 1
        line = raw_line.strip()
        map.append(line)
        
        col = -1
        
        for symbol in line:
            col += 1
            
            if symbol == ".":
                continue
            
            if symbol not in all_antennas:
                all_antennas[symbol] = []
            
            all_antennas[symbol].append({"row": row, "col": col})
    
    height = len(map)
    width = len(map[0])

def find_antinodes(antennas):
    off = len(antennas)
    
    for n in range(off - 1):
        for p in range(n + 1, off):
            a = antennas[n]
            b = antennas[p]
            find_antinodes_for(a, b)

def find_antinodes_for(a, b):
    delta_row = b["row"] - a["row"]
    c_row = a["row"] - delta_row
    d_row = b["row"] + delta_row
    
    delta_col = b["col"] - a["col"]
    c_col = a["col"] - delta_col
    d_col = b["col"] + delta_col

    register_antinode(c_row, c_col)
    register_antinode(d_row, d_col)

def register_antinode(row, col):
    if row < 0 or col < 0 or row >= height or col >= width:
        return
    
    all_antinodes[f"{row}:{col}"] = True

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Execution time:", time.time() - start_time, "seconds")
