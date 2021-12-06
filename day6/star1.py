
with open("input.txt", encoding="utf-8") as f:
    strings = [row.split(",") for row in f]
    strings = strings[0]
fishes = [int(fish) for fish in strings] # O:)
    
print(fishes)

prevd = {i: fishes.count(i) for i in range(9)}
print(prevd)

for i in range(80):     # star1
#for i in range(256):   # star2
    nextd = {j: 0 for j in range(9)}
    for key, value in prevd.items():
        if key > 0:
            nextd[key-1] = nextd[key-1] + value
        if key == 0:
            nextd[8] = value
            nextd[6] = nextd[6] + value
            
    prevd = nextd

population = sum(prevd.values())
print(prevd)
print(population)