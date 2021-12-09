import sys
sys.stdin =  open('input.txt')

import heapq

def bfs(start,end):
    INF = int(1e9)
    visit = [INF for _ in range(N + 1)]
    visit[start]=0
    Q = []
    heapq.heappush(Q,[0,start])
    while Q:
        w1,s = heapq.heappop(Q)
        for w2,e in graph[s]:
            nw = w1 + w2
            if nw<visit[e]:
                heapq.heappush(Q,[nw,e])
                visit[e]=nw
    return visit


N = int(input())
M = int(input())
graph =[[]for _ in range(N+1)]
for _ in range(M):
    s,e,w = map(int,input().split())
    graph[s].append([w,e])
start,end = map(int,input().split())
# graph.sort()
for g in graph:
    g.sort()
# [[], [[1, 4], [2, 2], [3, 3], [10, 5]], [[2, 4]], [[1, 4], [1, 5]], [[3, 5]], []]
print(bfs(start,end)[end])