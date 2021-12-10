def main():
    with open("input.txt", encoding="utf-8") as f:
        entries = [row.strip().split(" | ") for row in f]
    count = 0
    for entry in entries:
        output = entry[1].split(" ")
        lengths = list(map(lambda x: len(x), output))
        for l in lengths:
            if l in [2, 3, 4, 7]:
                count += 1
    print(count)

    

if __name__ == "__main__":
    main()