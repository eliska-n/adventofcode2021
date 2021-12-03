with open("input.txt", encoding="utf-8") as f:
    numbers = [number.strip() for number in f]


    def oxygen(numbers):
        index = 0
        while len(numbers) > 1:
            nulls = 0
            ones = 0
            for number in numbers:
                if number[index] == "0":
                    nulls += 1
                if number[index] == "1":
                    ones += 1
            if nulls > ones:
                rating = "0"
            if ones > nulls:
                rating = "1"
            if nulls == ones:
                rating = "1"
            newnums = []
            for number in numbers:
                if number[index] == rating:
                    newnums.append(number)
            numbers = newnums
            index += 1
        return int(numbers[0], 2)

    def carbdiox(numbers):
        index = 0
        while len(numbers) > 1:
            nulls = 0
            ones = 0
            for number in numbers:
                if number[index] == "0":
                    nulls += 1
                if number[index] == "1":
                    ones += 1
            if nulls < ones:
                rating = "0"
            if ones < nulls:
                rating = "1"
            if nulls == ones:
                rating = "0"
            newnums = []
            for number in numbers:
                if number[index] == rating:
                    newnums.append(number)
            numbers = newnums
            index += 1
        return int(numbers[0], 2)

    result = oxygen(numbers) * carbdiox(numbers)
    print(result)