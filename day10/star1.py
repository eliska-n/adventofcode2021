
def is_paired(input_string:str) -> str:
    bracket_list = []
    bracket_dict = {")":"(", "]":"[", "}":"{", ">":"<"}
    result = "fine"
    for i in input_string:
        if i in bracket_dict.values():
            bracket_list.append(i)
        elif i in bracket_dict.keys():
            if bracket_list == []:
                result = i
                break
            elif bracket_dict.get(i) == bracket_list[-1]:
                bracket_list.pop()
            else:
                result = i
                break
    return result
    

def main():
    with open("input.txt", encoding="utf-8") as f:
        rows = [row for row in f.read().split()]
        error_scores = []
        for row in rows:
            if is_paired(row) != "fine":
                d = {")": 3, 
                "]": 57,
                "}": 1197, 
                ">": 25137}
                syntax_error = d[is_paired(row)]
                error_scores.append(syntax_error)
        total_syntax_error = sum(error_scores)
        print(total_syntax_error)

if __name__ == "__main__":
    main()