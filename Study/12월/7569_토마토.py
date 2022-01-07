import sys
sys.stdin = open('input.txt')
input= sys.stdin.readline
from collections import deque

# 가로 세로 높이
M,N,H = map(int,input().split())
graph = []
zero = 0
Q = deque()
for k in range(H):
    layer = []
    for i in range(N):
        ls  = list(map(int,input().split()))
        layer.append(ls)
        for j in range(len(ls)):
            if ls[j]==1:
                Q.append([0,k,i,j])
            if ls[j]==0:
                zero+=1
    graph.append(layer)

def bfs():
    global result,zero

    dy = [0,0,-1,1,0,0]
    dx = [1,-1,0,0,0,0]
    dz = [0,0,0,0,1,-1]
    result = 0

    while Q :
        count,z,y,x = Q.popleft()
        if zero==0:
            return result
        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]
            nz = z + dz[i]
            if 0<=ny<N and 0<=nx<M and 0<=nz<H :
                if graph[nz][ny][nx] == 0 :
                    zero-=1
                    graph[nz][ny][nx]= count+1
                    Q.append([count+1,nz,ny,nx])
                    if count+1>result:
                        result= count+1
    return (-1)

print(bfs())
