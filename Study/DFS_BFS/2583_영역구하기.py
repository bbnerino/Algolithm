import sys
sys.stdin = open('input.txt')

def bfs(y,x):
    count = 0
    Q =[[y,x]]
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    graph[y][x]=1
    while Q:
        y,x = Q.pop(0)
        count+=1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<M and 0<=nx<N:
                if graph[ny][nx]==0:
                    graph[ny][nx]=1
                    Q.append([ny,nx])
    return count

M,N,K = map(int,input().split())
graph = [[0]*N for _ in range(M)]

for _ in range(K):
    sx,sy,ex,ey = map(int,input().split())
    for i in range(sy,ey):
        for j in range(sx,ex):
            graph[i][j]=1

result =[]
for i in range(M):
    for j in range(N):
        if graph[i][j]==0:
            result.append(bfs(i,j))
print(len(result))
print(*sorted(result))
