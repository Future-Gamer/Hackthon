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

def main():
    rules, updates = parse_input('day5-input.txt')
    correct_updates = [update for update in updates if is_correct_order(update, rules)]
    middle_pages = [find_middle_page(update) for update in correct_updates]
    result = sum(middle_pages)
    print("The sum of the middle page numbers of correctly-ordered updates is:", result)

if __name__ == "__main__":
    main()
