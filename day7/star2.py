import numpy as np

def main():
    with open("input.txt", encoding="utf-8") as f:
        crabs = f.read().split(",")
    crabsint = [int(crab) for crab in crabs]
    first_quartile = int(np.quantile(crabsint, 0.25))
    third_quartile = int(np.quantile(crabsint, 0.75))
    fuels = []
    for middlecrab in range(first_quartile, third_quartile):
        diffs = [abs(crab - middlecrab) for crab in crabsint]
        diffs2 = [sum([x for x in range(1, diff+1)]) for diff in diffs ]
        fuel = sum(diffs2)
        fuels.append(fuel)
        
    result = min(fuels)
    print(result)

if __name__ == "__main__":
    main()