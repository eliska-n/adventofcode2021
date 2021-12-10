def main():
    with open("input.txt", encoding="utf-8") as f:
        entries = [row.strip().split(" | ") for row in f]
    
    alldigits = []
    for entry in entries:
        output = entry[1].split(" ")
        hint = entry[0].split(" ")
        one = [x for x in hint if len(x)==2]
        four = [x for x in hint if len(x)==4]

        decoded = ""
        for digit in output:
            if len(digit) == 2:
                decoded += "1"
            if len(digit) == 3:
                decoded += "7"
            if len(digit) == 4:
                decoded += "4"
            if len(digit) == 5:
                if one[0][0] in digit and one[0][1] in digit:
                    decoded += "3"
                else:
                    countfour = sum([1 for letter in four[0] if letter in digit])
                    if countfour == 3:
                        decoded += "5"
                    if countfour == 2:
                        decoded += "2"
            if len(digit) == 6:
                if one[0][0] in digit and one[0][1] in digit:
                    countfour = sum([1 for letter in four[0] if letter in digit])
                    if countfour == 4:
                        decoded += "9"
                    else:
                        decoded += "0"
                else:
                    decoded += "6"
            if len(digit) == 7:
                decoded += "8"
        decoded = int(decoded)
        alldigits.append(decoded)
    result = sum(alldigits)
    print(result)

if __name__ == "__main__":
    main()
