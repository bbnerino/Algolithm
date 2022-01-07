import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
N = int(input())
graph = []
Q = deque()
for i in range(N):
    ls = list(map(int, input().split()))
    graph.append(ls)
    for j in range(N):
        if graph[i][j]==1:
            Q.append([0,i,j,[[i,j]] ] )

def bfs1(y,x,ground):
    queue = deque()
    queue.append([y,x])
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    while queue:
        y,x = queue.popleft()
        graph[y][x] = ground
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] ==1:
                    queue.append([ny,nx])
ground = 2
for i in range(len(Q)):
    bridge,i,j,first = Q[i]
    if graph[i][j]==1:
        bfs1(i,j,ground)
        ground+=1

def bfs2():
    dy = [0,1]
    dx = [1,0]
    while Q:
        bridge,y,x,visited = Q.popleft()
        vvvv = [[10000]*N for _ in range(N)]
        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if graph[ny][nx]==0 and [ny,nx] not in visited:
                    visited.append([ny, nx])
                    Q.append( [bridge + 1, ny, nx, visited])
                color = graph[visited[0][0]][visited[0][1]]
                if graph[ny][nx]!=color and graph[ny][nx]>0:
                    print(bridge)
                    exit()
bfs2()

