from collections import Counter

def getpoints(coordinates):
    points = []
    for ((x1, y1), (x2, y2)) in coordinates:
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        #horizontal
        if y1 == y2:
            l = [[x, y1] for x in range(min(x1,x2), max(x1,x2)+1)]
            points.append(l)
        #vertical
        elif x1 == x2:
            l = [[x1, y] for y in range(min(y1,y2), max(y1,y2)+1)]
            points.append(l)
        #diagonal
        else:
            x = [x for x in range(min(x1,x2), max(x1,x2)+1)]
            if x1 > x2:
                x.reverse()
            y = [y for y in range(min(y1,y2), max(y1,y2)+1)]
            if y1 > y2:
                y.reverse()

            l = [[x[i], y[i]] for i in range(len(x))]
            points.append(l)
    return points

def count(points):
    count = 0
    for point in points:
        if point.danger >= 2:
            count += 1
    return count

def main():
    with open("input.txt", encoding="utf-8") as f:
        rows = [row.strip() for row in f]
    lines = [line.split(" -> ") for line in rows]
    coordinates = [[coordinate.split(",") for coordinate in line] for line in lines]
    # linie není linie, ale seznam bodů, kterými prochází
    flatpoints = [point for line in getpoints(coordinates) for point in line]
    danger = Counter(map(tuple, flatpoints))
    print(sum(1 for c in danger.values() if c >= 2))

if __name__ == "__main__":
    main()