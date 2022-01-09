import sys
sys.stdin=open('input.txt')
input =sys.stdin.readline
from heapq import heappop,heappush

N = int(input())
graph=[]
for _ in range(N):
    s,e = map(int,input().split())
    graph.append([s,e])

graph.sort()

room = [0]  # 끝나는 시간을 기록한다.
for i in range(N): # N 개의 회의를 하나씩 순회하면서
    if graph[i][0]>= room[0]:   # 가장 빨리 끝나는 회의보다 늦게 시작하면?
        heappop(room)           # 그 회의자리에 다음 회의 끝나는 시간을 넣어준다.
        heappush(room,graph[i][1])
    else:                       # 다음 회의가 가장 빨리 끝나는 회의보다 늦다? (진행중)
        heappush(room,graph[i][1])  # 새로운 방에 추가해준다.

print(len(room)) # 총 방의 갯수를 구해준다.