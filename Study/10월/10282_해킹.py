import sys
sys.stdin = open('input.txt')

T = int(input())

import heapq
def bfs(start):
    Q = []
    heapq.heappush(Q,[0,start])  # [count=0 // 시작점]을 넣고 시작
    INF = int(1e9)              # 큰값
    visit = [INF] * (n + 1)     # start부터 n개의 점까지의 최소 거리
    visit[start]=0              # 자기는 0으로 시작

    while Q :                   # Q를 다 비울동안
        count,start = heapq.heappop(Q)  # Q = [count,시작점]
        for s,a in graph[start]:        # [걸리는 시간, 도착점]
            nc = count+s                # nc = 그전의 시간 + 도착점까지의 시간
            if nc<visit[a]:             # 만일 그 값이 원래의 최소거리보다 짧다면
                visit[a]=nc             # 그 값을 바꿔주고
                heapq.heappush(Q,[nc,a])    # Q에 추가 -> heap이기때문에 count가 작은거부터 계산해준다

    count=0     # start로부터 갈수있는 점 개수
    for i in range(len(visit)):
        if visit[i]==INF:   # 간적이 없는 곳이면
            visit[i]=-1     # 안갔다 표시해버리고
        else:               # 간적이 있다면
            count+=1        # count+=1해준다
    # [0, 2, 6]
    return [count,max(visit)]   # 연결된개수 , 가장 먼곳의 거리


for tc in range(T):
    n,d,c = map(int,input().split())    # 컴퓨터개수, 선 개수, 시작점
    graph=[[]for _ in range(n+1)]
    for _ in range(d):                  # 선 개수 만큼
        a,b,s = map(int,input().split())    # 도착점, 시작점, 걸리는 시간
        graph[b].append([s,a])              # 도착점에 [시간,시작점]으로 추가한다.

    print(*bfs(c))
