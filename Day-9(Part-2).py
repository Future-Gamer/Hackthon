def main():
    input_data = read_input("day9-input.txt")
    disk, all_files, search_start_by_space_size = process_input(input_data)
    move_files(disk, all_files, search_start_by_space_size)
    print("the answer is", checksum(disk))

def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

def process_input(input_data):
    disk = []
    all_files = []
    search_start_by_space_size = {str(i): 0 for i in range(1, 10)}
    
    index = -1
    file_id = -1

    while True:
        index += 1
        if index >= len(input_data):
            break
        
        file_length = input_data[index]
        if file_length is None:
            return disk, all_files, search_start_by_space_size
        
        file_id += 1
        all_files.append({"id": file_id, "start": len(disk), "size": int(file_length)})
        
        for _ in range(int(file_length)):
            disk.append(file_id)
        
        index += 1
        if index >= len(input_data):
            break
        
        blank_length = input_data[index]
        for _ in range(int(blank_length)):
            disk.append(-1)  # -1 means blank space
    
    return disk, all_files, search_start_by_space_size

def move_files(disk, all_files, search_start_by_space_size):
    while all_files:
        file = all_files.pop()
        if file is None:
            break
        move_file(disk, file, search_start_by_space_size)

def move_file(disk, file, search_start_by_space_size):
    space_start = find_space_for(disk, file["size"], search_start_by_space_size)
    if space_start == -1 or space_start > file["start"]:
        return
    
    search_start_by_space_size[str(file["size"])] = space_start  # that was the leftmost space
    
    for n in range(file["size"]):
        disk[file["start"] + n] = -1
        disk[space_start + n] = file["id"]

def find_space_for(disk, file_size, search_start_by_space_size):
    after_this = search_start_by_space_size[str(file_size)] - 1
    
    while True:
        space = find_next_space(disk, after_this)
        if space is None:
            return -1
        
        space_size = space["end"] - space["start"] + 1
        
        if space_size >= file_size:
            return space["start"]
        
        after_this = space["end"]

def find_next_space(disk, after_this):
    start = after_this
    
    while True:
        start += 1
        if start >= len(disk) or disk[start] == -1:
            break
    
    end = start
    while end + 1 < len(disk) and disk[end + 1] == -1:
        end += 1
    
    return {"start": start, "end": end}

def checksum(disk):
    result = 0

    for index, file in enumerate(disk):
        if file != -1:
            result += index * file
    
    return result

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("execution time", round(time.time() - start_time, 2), "seconds")
