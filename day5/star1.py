from collections import Counter

def getpoints(coordinates):
    points = []
    for ((x1, y1), (x2, y2)) in coordinates:
        #horizontal
        if y1 == y2:
            l = [[x, int(y1)] for x in range(min(int(x1),int(x2)), max(int(x1),int(x2))+1)]
            points.append(l)
        #vertical
        elif x1 == x2:
            l = [[int(x1), y] for y in range(min(int(y1),int(y2)), max(int(y1),int(y2))+1)]
            points.append(l)
    return points

def count(points):
    count = 0
    for point in points:
        if point.danger >= 2:
            count += 1
    return count

def main():
    with open("inputtest.txt", encoding="utf-8") as f:
        rows = [row.strip() for row in f]
    lines = [line.split(" -> ") for line in rows]
    coordinates = [[coordinate.split(",") for coordinate in line] for line in lines]
    # linie není linie, ale seznam bodů, kterými prochází
    flatpoints = [point for line in getpoints(coordinates) for point in line]
    danger = Counter(map(tuple, flatpoints))
    print(sum(1 for c in danger.values() if c >= 2))

if __name__ == "__main__":
    main()