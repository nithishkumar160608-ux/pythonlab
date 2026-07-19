from itertools import combinations
list=[-1,2.7,-3,4,2.5]
print("positive combination")
for r in range(l,len(list)+1):
    for combo in combinations(list,r):
        if all(num>0 for num in combo):
            print(combo)
