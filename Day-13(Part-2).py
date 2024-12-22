OFFSET = 10 * 1000 * 1000 * 1000 * 1000

def main():
    global minimum_spent_tokens
    minimum_spent_tokens = 0
    
    process_input()
    
    print("The answer is", minimum_spent_tokens)

def process_input():
    with open('day13-input.txt', 'r') as file:
        input_data = file.read().strip()
    
    paragraphs = input_data.split("\n\n")
    
    for paragraph in paragraphs:
        lines = paragraph.split("\n")
        
        parts1 = lines.pop(0).strip().split(",")
        parts2 = lines.pop(0).strip().split(",")
        parts3 = lines.pop(0).strip().split(",")
        
        button_ax = int(parts1.pop(0).replace("Button A: X+", ""))
        button_ay = int(parts1.pop(0).replace(" Y+", ""))
        
        button_bx = int(parts2.pop(0).replace("Button B: X+", ""))
        button_by = int(parts2.pop(0).replace(" Y+", ""))
        
        prize_x = int(parts3.pop(0).replace("Prize: X=", ""))
        prize_y = int(parts3.pop(0).replace(" Y=", ""))
        
        process_machine(button_ax, button_ay, button_bx, button_by, OFFSET + prize_x, OFFSET + prize_y)

def process_machine(button_ax, button_ay, button_bx, button_by, prize_x, prize_y):
    global minimum_spent_tokens

    a_clicks_x_multiplier = button_ax * button_by
    a_clicks_y_multiplier = -(button_ay * button_bx)
    prize_x_multiplied = prize_x * button_by
    prize_y_multiplied = -(prize_y * button_bx)

    a_clicks_multiplier_combined = a_clicks_x_multiplier + a_clicks_y_multiplier
    prize_multiplied_combined = prize_x_multiplied + prize_y_multiplied

    if prize_multiplied_combined % a_clicks_multiplier_combined != 0:
        return  # has no solution
    
    a_clicks = prize_multiplied_combined // a_clicks_multiplier_combined
    b_clicks = (prize_x - (button_ax * a_clicks)) / button_bx
    
    if b_clicks != int(b_clicks):
        return  # has no solution
    
    minimum_spent_tokens += a_clicks * 3 + b_clicks

if __name__ == "__main__":
    main()
