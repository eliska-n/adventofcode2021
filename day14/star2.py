from collections import Counter


def polymerize(template_counts, instructions):
    cycles = 0
    while cycles < 40:
        new_counts = Counter()
        for pair, count in template_counts.items():
            insert = instructions[pair]
            new_ds = [pair[0] + insert, insert + pair[1]]
            for new_d in new_ds:
                new_counts[new_d] += count
        # restart cycle
        template_counts = new_counts
        new_counts = {}
        cycles += 1

    return template_counts


def count_elements(template, polymer):
    letter_counts = Counter()
    for (pair), count in polymer.items():
        for letter in pair:
            letter_counts[letter] += count
    # all letters are repeated twice but the first and the last ones
    first_letter = template[0]
    last_letter = template[-1]
    letter_counts[first_letter] += 1
    letter_counts[last_letter] += 1
    element_counts = {k: int(v/2) for k, v in letter_counts.items()}
    return element_counts


def main():
    with open("input.txt", encoding="utf-8") as f:
        inputs = [row for row in f.read().split("\n\n")]
    template = inputs[0]
    instructions = {x.split(" -> ")[0]: x.split(" -> ")[1]
                    for x in inputs[1].split("\n")}
    template_counts = Counter(template[i]+template[i+1]
                              for i in range(len(template)-1))

    polymer = polymerize(template_counts, instructions)
    element_counts = count_elements(template, polymer)

    result = max(element_counts.values()) - min(element_counts.values())
    print(result)


if __name__ == "__main__":
    main()
