import sys
sys.stdin = open('input.txt')
import heapq

N,M,R  = map(int,input().split())
# M = 수색 범위
# 내 근처 M개 수색 가능
items = list(map(int,input().split()))
graph = [[0]*N for _ in range(N)]
for _ in range(R):
    y,x,t= list(map(int,input().split()))
    graph[y-1][x-1] = t
    graph[x-1][y-1] = t

def bfs(start):
    # 시작 지점으로부터 모든 점의 거리 구하기
    Q = [[0,start]]
    visted = [10000]*N
    visted[start] = 0
    while Q:
        length, now = heapq.heappop(Q)
        for i in range(N):
            if graph[now][i]!=0:
                if 0 < graph[now][i] + length < visted[i]:
                    visted[i] = graph[now][i] + length
                    Q.append([graph[now][i]+length, i ])
    result=0
    for i in range(N):
        if visted[i] <= M:
            result+=items[i]
    return result
resultlist =[]
for i in range(N):
    resultlist.append(bfs(i))
print(max(resultlist))



