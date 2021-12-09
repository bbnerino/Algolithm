from collections import deque
import sys
from typing import Tuple
sys.stdin = open('input.txt')

N = int(input())
time = [[0 for _ in range(N)]for _ in range(N)]
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))



for i in range(N):
    for j in range(N):
        if graph[i][j]==9:
            now = [i,j]

def bfs(now):
    Q = deque()
    Q.append(now)
    shark_size = 2
    dy = [-1,0,1,0]
    dx = [0,-1,0,1]
    while Q:
        Progress = False
        for i in range(N):
            for j in range(N):
                if graph[i][j] !=0 and graph[i][j] != 9 and graph[i][j] < shark_size:
                    Progress =True

        if Progress:
            s = Q.popleft()
            graph[s[0]][s[1]]=0
            for i in range(4):
                ny = dy[i]+s[0]
                nx = dx[i]+s[1]
                if 0 <= ny < N and 0 <= nx < N:
                    if graph[ny][nx] < shark_size:
                        Q.append([ny,nx])
                        graph[ny][nx]= 0
                        time[ny][nx] = time[s[0]][s[1]]+1
        else:
            print(time)

bfs(now)