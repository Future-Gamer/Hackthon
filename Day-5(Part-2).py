def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    rules = []
    updates = []
    is_update_section = False

    for line in lines:
        line = line.strip()
        if not line:
            is_update_section = True
            continue
        if is_update_section:
            updates.append(list(map(int, line.split(','))))
        else:
            rules.append(tuple(map(int, line.split('|'))))
    
    return rules, updates

def is_correct_order(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def reorder_update(update, rules):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([node for node in update if in_degree[node] == 0])
    ordered_update = []

    while queue:
        node = queue.popleft()
        ordered_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_update

def main():
    rules, updates = parse_input('day5-input.txt')
    incorrect_updates = [update for update in updates if not is_correct_order(update, rules)]
    reordered_updates = [reorder_update(update, rules) for update in incorrect_updates]
    middle_pages = [find_middle_page(update) for update in reordered_updates]
    result = sum(middle_pages)
    print("The sum of the middle page numbers of correctly-ordered updates is:", result)

if __name__ == "__main__":
    main()
