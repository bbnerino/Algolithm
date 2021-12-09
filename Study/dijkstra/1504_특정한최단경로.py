import sys
sys.stdin = open('input.txt')

import heapq
def bfs(start):
    Q = []
    heapq.heappush(Q,[0,start])
    INF = int(1e9)
    visit = [INF for _ in range(N+1)]
    visit[start]=0
    while Q:
        w1,s = heapq.heappop(Q)
        for w2,e in graph[s]:
            nw = w1+w2
            if nw < visit[e]:
                visit[e]=nw
                heapq.heappush(Q,[nw,e])

    return visit

N,E = map(int,input().split())
graph = [[]for _ in range(N+1)]
for _ in range(E):
    s,e,w = map(int,input().split())
    graph[s].append([w,e])
    graph[e].append([w,s])
start,end = map(int,input().split())


sss = bfs(start)
eee = bfs(end)

if sss[end] == int(1e9) or eee[N]==int(1e9) or eee[1]==int(1e9) or sss[1]==int(1e9) or sss[N]==int(1e9):
    print(-1)
else:
    print(sss[end]+min((sss[1]+eee[N]),(eee[1]+sss[N])))


