def main():
    process_input()

    total_distance = 0

    off = len(listA)

    for n in range(off):
        total_distance += abs(listB[n] - listA[n])

    print("the answer is", total_distance)

def process_input():
    with open("day1-input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    for line in lines:
        valueA = int(line[0:5])
        valueB = int(line[8:13])

        listA.append(valueA)
        listB.append(valueB)

    listA.sort()
    listB.sort()

if __name__ == "__main__":
    import time
    start_time = time.time()

    listA = []
    listB = []

    main()

    print("execution time: {:.2f}ms".format((time.time() - start_time) * 1000))
