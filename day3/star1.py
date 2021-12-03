with open("input.txt", encoding="utf-8") as f:
    numbers = [number.strip() for number in f]


    def getgamma(index):
        nulls = 0
        ones = 0
        for number in numbers:
            if number[index] == "0":
                nulls += 1
            if number[index] == "1":
                ones += 1
        if nulls > ones:
            gamma = "0"
        if ones > nulls:
            gamma = "1"
        return gamma


    def getepsilon(gamma):
        epsilon = ""
        for i in gamma:
            if i == "0":
                epsilon += "1"
            if i == "1":
                epsilon += "0"
        return epsilon


    gamma = ""
    for i in range(len(numbers[0])):
        bit = getgamma(i)
        gamma += bit
    epsilon = getepsilon(gamma)
    
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print (gamma * epsilon)


