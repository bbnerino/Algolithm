import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from heapq import heappush,heappop

N = int(input())
M = int(input())

graph = [[]for _ in range(N+1)]
for _ in range(M):
    a,b,d = map(int,input().split())
    heappush(graph[a],[d,b])

def bfs(START):
    route = [START] # 다녀온 길을 체크합니다.
    Q = [[0,START,route]]   # [총 경로의 길이, 현재위치, 경로] 순서로 bfs를 순회합니다

    while Q :
        cnt, start, route = heappop(Q)
        if start == END:    # 만일 도착지가 목적지라면
            print(cnt)      # 출력하고 끝냅니다.
            print(len(route))
            print(*route)
            return
        while graph[start]: # 원래라면 for 문으로 전부 순회를 할텐데
            distance,end = heappop(graph[start])    # 순회하지 못하게 그냥 없애버립니다.
            if end not in route:                # 다음 목적지가 route에 없으면
                heappush(Q,[cnt+distance,end,route+[end]])  # Q에 넣고 진행합니다.

START, END = map(int,input().split())
bfs(START)
