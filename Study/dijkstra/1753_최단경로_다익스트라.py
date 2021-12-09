import sys
sys.stdin= open('input.txt')
input = sys.stdin.readline
import heapq

INF = int(1e9)
heap =[]

def dijkstra(start):
    heapq.heappush(heap,[0,start])
    visit[start]= 0 # 첫 점은 0이다
    while heap:
        w,v = heapq.heappop(heap)
        for next_w,next_v in graph[v]:
            nw = next_w + w
            if nw < visit[next_v]:
                visit[next_v]=nw
                heapq.heappush(heap,[nw,next_v])

#### 입력받기
V,E = map(int,input().split())
start= int(input())
graph = [[]for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([w,v])

    # [w,v] -> 거리, 목적지
visit = [INF for _ in range(V+1)]
dijkstra(start)


for i in range(1,len(visit)):
    if visit[i] != INF:
        print(visit[i])
    else:
        print('INF')
