with open("day2\input.txt", encoding="utf-8") as f:
    rows = [row.strip() for row in f]
    depth = 0
    horizontal = 0
    aim = 0
    for log in rows:
        if log.split()[0] == "forward":
            horizontal += int(log.split()[1])
            depth += int(log.split()[1]) * aim
        if log.split()[0] == "down":
            aim += int(log.split()[1])
        if log.split()[0] == "up":
            aim -= int(log.split()[1])
    print(horizontal*depth)
