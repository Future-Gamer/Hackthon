import itertools
from collections import deque

def read_disk_map(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def parse_disk_map(disk_map):
    blocks = []
    file_id = 0
    for i, length in enumerate(disk_map):
        length = int(length)
        if i % 2 == 0:
            # File blocks
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            # Free space blocks
            blocks.extend(['.'] * length)
    return blocks

def compact_disk(blocks):
    free_space_indices = deque(i for i, block in enumerate(blocks) if block == '.')
    free_space_indices.reverse()
    i = len(blocks) - 1

    while free_space_indices:
        free_index = free_space_indices.pop()
        while i > free_index and blocks[i] == '.':
            i -= 1
        if i <= free_index:
            break
        blocks[free_index], blocks[i] = blocks[i], '.'
        i -= 1

    return blocks

def calculate_checksum(blocks):
    return sum(i * int(block) for i, block in enumerate(blocks) if block != '.')

def main():
    filename = 'day9-input.txt'
    disk_map = read_disk_map(filename)
    blocks = parse_disk_map(disk_map)
    compacted_blocks = compact_disk(blocks)
    checksum = calculate_checksum(compacted_blocks)
    print('Filesystem checksum:', checksum)

if __name__ == '__main__':
    main()
