from statistics import median

def main():
    with open("input.txt", encoding="utf-8") as f:
        crabs = f.read().split(",")
    crabsint = [int(crab) for crab in crabs]
    middlecrab = median(crabsint)
    diffs = [abs(crab - middlecrab) for crab in crabsint]
    result = sum(diffs)
    print(result)

if __name__ == "__main__":
    main()