from collections import Counter


def polymerize(template, instructions):
    cycles = 0
    while cycles < 10:
        to_insert = []
        for index, letter in enumerate(template[:len(template)-1]):
            double = letter + template[index+1]
            to_insert.append(instructions[double])

        new_template = ""
        for i in range(len(template)):
            new_template += template[i]
            if i < len(to_insert):
                new_template += to_insert[i]
        #restart cycle
        template = new_template
        new_template = ""
        cycles += 1
        
    counts = Counter(template)

    return counts


def main():
    with open("input.txt", encoding="utf-8") as f:
        inputs = [row for row in f.read().split("\n\n")]
    template = inputs[0]
    instructions = {x.split(" -> ")[0]: x.split(" -> ")[1]
                    for x in inputs[1].split("\n")}
    counts = polymerize(template, instructions)
    result = max(counts.values()) - min(counts.values())
    print(result)


if __name__ == "__main__":
    main()
