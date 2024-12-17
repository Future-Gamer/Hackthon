def main():
    process_input()

    similarity = 0

    for number in listA:
        count = dictB.get(str(number))
        if count is not None:
            similarity += number * count

    print("the answer is", similarity)

def process_input():
    with open("day1-input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    for line in lines:
        valueA = int(line[0:5])
        stringB = line[8:13]

        listA.append(valueA)

        if stringB not in dictB:
            dictB[stringB] = 0
        dictB[stringB] += 1

if __name__ == "__main__":
    import time
    start_time = time.time()

    listA = []
    dictB = {}

    main()

    print("execution time: {:.2f}ms".format((time.time() - start_time) * 1000))
