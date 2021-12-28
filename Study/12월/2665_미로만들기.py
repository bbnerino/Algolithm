import sys
sys.stdin = open('input.txt')

n = int(input())
graph=[]
for _ in range(n):
    ls =list(map(int,input().rstrip()))
    graph.append(ls)

import heapq
def bfs():
    Q = []
    heapq.heappush(Q,[0,0,0])
    visited = [[100000]*n for _ in range(n)]
    visited[0][0] = 0
    while Q:
        change,y,x = heapq.heappop(Q)
        if y==n-1 and x==n-1 :
            print(change)
            exit()

        dy =[0,0,-1,1]
        dx =[1,-1,0,0]
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<n:
                if graph[ny][nx]==1 and change<visited[ny][nx]:
                    visited[ny][nx] = change
                    heapq.heappush(Q,[change,ny,nx])

                if graph[ny][nx]==0  and change+1<=visited[ny][nx]:
                    visited[ny][nx]= change
                    heapq.heappush(Q,[change+1,ny,nx])

bfs()