import sys
sys.stdin = open('input.txt')
from collections import  deque

N,M = map(int,input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

def bfs(y,x):
    Q = deque()
    Q.append([y,x])
    graph[y][x] = 0
    dy = [0,0,-1,1,1,1,-1,-1]
    dx = [-1,1,0,0,-1,1,-1,1]
    while Q :
        y,x = Q.popleft()
        for i in range(8):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] ==1:
                    Q.append([ny,nx])
                    graph[ny][nx] = 0


result = 0

for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            bfs(i,j)
            result+=1

print(result)
