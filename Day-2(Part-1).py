def is_safe(report):
    increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def main():
    with open("day2-input.txt", "r") as file:
        reports = [list(map(int, line.strip().split())) for line in file]

    safe_reports = sum(1 for report in reports if is_safe(report))

    print("Number of safe reports:", safe_reports)

if __name__ == "__main__":
    main()
