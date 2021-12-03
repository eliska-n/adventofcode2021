with open("day2\input.txt", encoding="utf-8") as f:
    rows = [row.strip() for row in f]
    depth = 0
    horizontal = 0
    for log in rows:
        if log.split()[0] == "forward":
            horizontal += int(log.split()[1])
        if log.split()[0] == "down":
            depth += int(log.split()[1])
        if log.split()[0] == "up":
            depth -= int(log.split()[1])
    print(horizontal*depth)
