import sys
sys.stdin = open('input.txt')

import heapq
def dij(start):
    H = []
    heapq.heappush(H,[0,start])
    while H:
        dis,start = heapq.heappop(H)
        for next_dis , next_start in graph[start]:
            new_dis = next_dis + dis
            if new_dis< visit[next_start]:
                visit[next_start]=new_dis
                heapq.heappush(H,[new_dis,next_start])



T = int(input())
for tc in range(T):
    N,E = map(int,input().split()) #
    graph =[[]for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        graph[s].append([w,e])

    INF = int(1e9)
    visit =[INF for _ in range(N+1)]
    dij(0)
    print('#{} {}'.format(tc+1,visit[N]))