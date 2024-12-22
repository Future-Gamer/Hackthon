width = 101
height = 103

verticalDivision = 50   # for width
horizontalDivision = 51 # for height

quadrantA = 0
quadrantB = 0
quadrantC = 0
quadrantD = 0


def main():
    global quadrantA, quadrantB, quadrantC, quadrantD

    process_input()
    
    print("The answer is", quadrantA * quadrantB * quadrantC * quadrantD)


def process_input():
    global quadrantA, quadrantB, quadrantC, quadrantD

    with open("day14-input.txt", "r") as file:
        lines = file.read().strip().split("\n")
    
    for line in lines:
        parts = line.strip().split(" ")
        
        tokensP = parts[0][2:].split(",")
        tokensV = parts[1][2:].split(",")
        
        posX = int(tokensP[0])
        posY = int(tokensP[1])
        velX = int(tokensV[0])
        velY = int(tokensV[1])
        
        bruteX = posX + (100 * velX)
        bruteY = posY + (100 * velY)
        
        finalX = bruteX % width
        if finalX < 0:
            finalX += width
        
        finalY = bruteY % height
        if finalY < 0:
            finalY += height
        
        if finalX == verticalDivision:
            continue
        if finalY == horizontalDivision:
            continue
        
        if finalX < verticalDivision:  # A or C
            if finalY < horizontalDivision:
                quadrantA += 1
            else:
                quadrantC += 1
        else:  # B or D
            if finalY < horizontalDivision:
                quadrantB += 1
            else:
                quadrantD += 1


if __name__ == "__main__":
    main()
