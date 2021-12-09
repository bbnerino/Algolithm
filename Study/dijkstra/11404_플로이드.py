import sys
sys.stdin= open('input.txt')

import heapq
def dij(i):
    Q =[]
    heapq.heappush(Q,[0,i])
    visit = [INF for _ in range(N + 1)]
    visit[i]=0

    while Q:
        count,start = heapq.heappop(Q)
        for nc,ns in graph[start]:
            newcount = count+nc
            if newcount < visit[ns]:
                visit[ns] = newcount
                heapq.heappush(Q,[newcount,ns])
    return visit

N = int(input())
M = int(input())
graph =[[] for _ in range(N+1)]
for _ in range(M):
    a,b,w = map(int,input().split())
    graph[a].append([w,b])
INF = int(1e9)


for i in range(1,N+1):
    result = dij(i)
    for j in range(len(result)):
        if result[j]==INF:
            result[j]=0
    result.pop(0)
    print(*result)
