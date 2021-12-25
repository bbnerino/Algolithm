import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,M = map(int,input().split())
graph =[]
for _ in range(N):
    ls =[]
    ls.extend(map(int,(list( input().rstrip()))))
    graph.append(ls)

import heapq
def bfs():
    global result
    Q = [[1,False,0,0]]
    visited = [[10000]*M for _ in range(N)]
    visited[0][0]=1
    result=[]
    while Q :
        count,wall,y,x = heapq.heappop(Q)
        if y==N-1 and x==M-1:
            result.append(count)
        dy =[0,0,-1,1]
        dx =[1,-1,0,0]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx]==0 and visited[ny][nx] > count:
                    visited[ny][nx] = count
                    Q.append([count+1,wall,ny,nx])

                elif graph[ny][nx]==1 and visited[ny][nx] > count and wall==False :
                    visited[ny][nx] = count
                    Q.append([count+1,True,ny,nx])

bfs()
if result:
    print(min(result))
else:
    print(-1)