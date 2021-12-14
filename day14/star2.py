from collections import Counter

def main():
    with open("input.txt", encoding="utf-8") as f:
        inputs = [row for row in f.read().split("\n\n")]
    template = inputs[0]
    instructions = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in inputs[1].split("\n")}
    template_doubles = []
    for index, letter in enumerate(template[:len(template)-1]):
        d = letter + template[index+1]
        template_doubles.append(d)
    c = Counter(map(tuple, template_doubles))
    template_counts = {"".join(k): v for k, v in c.items()}

    counter = 0
    while counter < 40:
        new_counts = {}
        for double, count in template_counts.items():
            insert = instructions[double]
            new_d1 = double[0] + insert
            new_d2 = insert + double[1]
            new_ds = [new_d1, new_d2]
            for new_d in new_ds:
                if new_d in new_counts.keys():
                    new_counts[new_d] += count
                else:
                    new_counts[new_d] = count
        template_counts = new_counts
        new_counts = {}
        counter += 1
    
    letter_counts = {}
    for double, count in template_counts.items():
        for letter in double:
            if letter in letter_counts.keys():
                letter_counts[letter] += count
            else:
                letter_counts[letter] = count
    
    first_letter = template[0]
    last_letter = template[-1]
    letter_counts[first_letter] += 1
    letter_counts[last_letter] += 1
    letter_counts = {k: int(v/2) for k, v in letter_counts.items()}
    
    result = max(letter_counts.values()) - min(letter_counts.values())
    print(result)

if __name__ == "__main__":
    main()