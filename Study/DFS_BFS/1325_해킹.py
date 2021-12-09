import sys
sys.stdin = open('input.txt')

import copy
N,M = map(int,input().split())
graph =[[]for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[y].append(x)


def dfs():
    global count
    s = stack.pop()
    while ngraph[s]:
        k = ngraph[s].pop()
        stack.append(k)
        count+=1
        dfs()

result =[]
for i in range(1,N):
    stack=[i]
    count=0
    ngraph =copy.deepcopy(graph)
    dfs()
    result.append(count)

rrr= []
mx = max(result)
for i in range(len(result)):
    if result[i] == mx:
        rrr.append(i+1)

print(*rrr)


