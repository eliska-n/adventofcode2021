import pandas as pd
import matplotlib.pyplot as plt

def fold_along_y(points, instruction):
    fold = int(instruction[1])
    new_points = []
    for x, y in points:
        if y < fold:
            new_point = [x, y]

        if y > fold:
            distance = y - fold
            new_y = fold - distance
            if new_y >= 0:
                new_point = [x, new_y]

        if new_point not in new_points:
            new_points.append(new_point)
    
    return new_points

def fold_along_x(points, instruction):
    fold = int(instruction[1])
    new_points = []
    for x, y in points:
        if x < fold:
            new_point = [x, y]

        if x > fold:
            distance = x - fold
            new_x = fold - distance
            if new_x >= 0:
                new_point = [new_x, y]

        if new_point not in new_points:
            new_points.append(new_point)
    
    return new_points


def main():
    with open("input.txt", encoding="utf-8") as f:
        inputs = [row for row in f.read().split("\n\n")]
    points_str = [row.split(",") for row in inputs[0].split("\n")]
    points = [[int(coor) for coor in point] for point in points_str]
    instructions = [row.strip("fold along ").split("=") for row in inputs[1].split("\n")]


    for instruction in instructions:
        if instruction[0] == "y":
            new_points = fold_along_y(points, instruction)
        if instruction[0] == "x":
            new_points = fold_along_x(points, instruction)
        points = new_points

    df = pd.DataFrame(new_points, columns = ["x", "y"])
    plt.scatter(df["x"], df["y"])
    plt.show()


if __name__ == "__main__":
    main()