import sys
sys.stdin = open('input.txt')

import copy
def normal_bfs(b,a,RGB):
    Q = [[b,a]]
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    graph[b][a]= countn
    while Q:
        s = Q.pop(0)
        for i in range(4):
            ny = s[0]+ dy[i]
            nx = s[1]+ dx[i]
            if 0<=nx<N  and 0<=ny<N:
                if graph[ny][nx]==RGB:
                    graph[ny][nx]=countn
                    Q.append([ny,nx])

def x_bfs(b,a,RGB):
    Q = [[b, a]]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    xgraph[b][a] = countx
    while Q:
        s = Q.pop(0)
        for i in range(4):
            ny = s[0] + dy[i]
            nx = s[1] + dx[i]
            if 0 <= nx < N and 0 <= ny < N:
                if RGB=='R' or RGB =='G':
                    if xgraph[ny][nx] == 'R' or  xgraph[ny][nx] =='G':
                        xgraph[ny][nx] = countx
                        Q.append([ny, nx])
                elif RGB =='B':
                    if xgraph[ny][nx] == 'B':
                        xgraph[ny][nx] = countx
                        Q.append([ny, nx])

N = int(sys.stdin.readline())
graph=[[]for _ in range(N)]
for i in range(N):
    graph[i].extend(input())
xgraph = copy.deepcopy(graph)


countn=0
countx=0
for i in range(N):
    for j in range(N):
        if not isinstance(graph[i][j],int):
            countn += 1
            normal_bfs(i,j,graph[i][j])


for i in range(N):
    for j in range(N):
        if not isinstance(xgraph[i][j],int):
            countx += 1
            x_bfs(i,j,xgraph[i][j])

print(countn,countx)


