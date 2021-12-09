from itertools import combinations

N,S = map(int,input().split())
nums = list(map(int,input().split()))
combi = []
result = []

for i in range(1,len(nums)+1):
    combi.append(list(map(list,combinations(nums,i))))

for c in combi:
    for i in c:
        result.append(sum(i))
print(result.count(S))
