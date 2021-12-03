#https://adventofcode.com/2021/day/1

from input import input

list = input.split("\n")
increased = 0
for i in range(len(list)-3):
    if (int(list[i+1]) + int(list[i+2]) + int(list[i+3])) > (int(list[i]) + int(list[i+1]) + int(list[i+2])):
        increased += 1

print(increased)