from itertools import combinations
lst = [2,-3,6,-7]
print("positive numbers are")
for i in range(1,len(lst)+1):
    for combo in combinations(lst,i):
        if all(x>0 for x in combo):
            print(combo)
