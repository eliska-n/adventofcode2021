from statistics import median

def is_paired(input_string:str) -> list:
    bracket_list = []
    bracket_dict = {")":"(", "]":"[", "}":"{", ">":"<"}
    correct = True
    for i in input_string:
        if i in bracket_dict.values():
            bracket_list.append(i)
        elif i in bracket_dict.keys():
            if bracket_list == []:
                correct = False
            elif bracket_dict.get(i) == bracket_list[-1]:
                bracket_list.pop()
            else:
                correct = False
    if correct == True:
        if bracket_list != []:
            return bracket_list
    if correct == False:
        return "complete or false"

def get_score(complementary:list) -> int:
    score = 0
    d = {")": 1, 
    "]": 2,
    "}": 3, 
    ">": 4}
    for i in complementary:
        num = (score * 5) + d[i]
        score = num
    return score
    

def main():
    with open("input.txt", encoding="utf-8") as f:
        rows = [row for row in f.read().split()]
    scores = []
    for row in rows:
        incomplete = is_paired(row)
        if isinstance(incomplete, list):
            bracket_dict = {"(":")", "[":"]", "{":"}", "<":">"}
            complementary = [bracket_dict[i] for i in incomplete]
            complementary.reverse()
            score = get_score(complementary)
            scores.append(score)
    middle_score = median(scores)
    print(middle_score)

if __name__ == "__main__":
    main()