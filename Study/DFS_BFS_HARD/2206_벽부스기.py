import sys
sys.stdin = open('input.txt')
N,M = map(int,input().split())
graph=[[] for _ in range(N)]
for i in range(N):
    a = input()
    graph[i].extend(map(int,a))

from collections import deque
def bfs(y,x):
    Q = deque()
    Q.append([0,y,x])
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    while Q:
        count,y,x = Q.pop(0)
        for i in range(4):
            ny = dy[i]+ y
            nx = dx[i]+ x
            if 0<=ny<N and 0<= nx <M:
                pass