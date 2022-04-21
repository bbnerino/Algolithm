import sys
sys.stdin = open('input.txt')
from collections import deque
N = int(input())
M = int(input())
graph = deque(map(int,input().split()))

result = []


# [vote,idx,key]

for i in range(M):
    man = graph.popleft()
    if len(result) ==0:          # N개 안채워졌으면
        result.append([1,i,man]) # vote, 순서, 사람이름 넣고 다음
        result.sort(key=lambda x: (-x[0], -x[1]))
        continue

    flag = False
    for g in result:
        if g[2]== man: # result 에서 그 사람이 있다면 ?
            flag = True
            g[0] +=1   # vote 추가해주기
            continue

    if not flag :
        if len(result)>=N:
            result.pop()
            result.append([1,i,man])
            result.sort(key=lambda x:(-x[0],-x[1]))
        else:
            result.append([1, i, man])  # vote, 순서, 사람이름 넣고 다음
    result.sort(key=lambda x:(-x[0],-x[1]))

sol = []
for r in result:
    sol.append(r[2])
print(*sorted(sol))

