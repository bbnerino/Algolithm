import sys
sys.stdin = open('input.txt')

import heapq
def dij(start): # bfs 기반
    INF=int(1e9)
    visit =[INF]*(N+1)
    visit[start]=0
    Q =[]
    heapq.heappush(Q,[0,start])
    while Q:
        count,start = heapq.heappop(Q)
        for w,b in graph[start]:
            nc = count+w
            if nc < visit[b]:
                visit[b]=nc
                heapq.heappush(Q,[nc,b])

    return visit


N,M,X = map(int,input().split())
graph =[[]for _ in range(N+1)]
for _ in range(M):
    a,b,w = map(int,input().split())
    graph[a].append([w,b])

result =[[]]
for i in range(1,N+1):          # 각 다익스트라 결과들을 받아온다
    result.append(dij(i))       # index를 맞춰주기 위해 빈칸도 하나 만들어준다
print(result)
# [[], [1000000000, 0, 4, 2, 6], [1000000000, 1, 0, 3, 7], [1000000000, 2, 6, 0, 4], [1000000000, 4, 3, 6, 0]]

who_big = []                    # 파티의 위치(X)에서  i번째 집 까지의 거리
for i in range(1,N+1):          #    + i번째 집에서 X까지의 거리 ==> 왕복 거리
    who_big.append(result[X][i]+result[i][X])       # 다 더해주고 최대값을 구한다.
print(max(who_big))


