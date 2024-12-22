def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    machines = []
    i = 0
    while i < len(lines):
        a_line = lines[i].strip()
        b_line = lines[i + 1].strip()
        prize_line = lines[i + 2].strip()

        a_x = int(a_line.split()[2].split('+')[1].strip(','))
        a_y = int(a_line.split()[3].split('+')[1])
        b_x = int(b_line.split()[2].split('+')[1].strip(','))
        b_y = int(b_line.split()[3].split('+')[1])
        prize_x = int(prize_line.split()[1].split('=')[1].strip(','))
        prize_y = int(prize_line.split()[2].split('=')[1])

        machines.append(((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))
        i += 4
    return machines

def find_min_tokens(a_x, a_y, b_x, b_y, prize_x, prize_y, max_presses=100):
    min_tokens = float('inf')
    for a_presses in range(max_presses + 1):
        for b_presses in range(max_presses + 1):
            if a_presses * a_x + b_presses * b_x == prize_x and a_presses * a_y + b_presses * b_y == prize_y:
                tokens = a_presses * 3 + b_presses * 1
                if tokens < min_tokens:
                    min_tokens = tokens
    return min_tokens

def main():
    machines = parse_input('day13-input.txt')
    total_tokens = 0
    prizes_won = 0
    
    for a, b, prize in machines:
        min_tokens = find_min_tokens(a[0], a[1], b[0], b[1], prize[0], prize[1])
        if min_tokens != float('inf'):
            total_tokens += min_tokens
            prizes_won += 1
    
    print(f'Total prizes won: {prizes_won}')
    print(f'Total tokens spent: {total_tokens}')

if __name__ == "__main__":
    main()
