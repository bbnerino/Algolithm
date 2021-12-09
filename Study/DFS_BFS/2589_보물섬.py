import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
graph =[[] for _ in range(N)]
for i in range(N):
    graph[i].extend(input())


def bfs(a,b,c):
    Q = [[a,b,c]]
    dy =[1,-1,0,0]
    dx =[0,0,1,-1]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[a][b]=c
    count = c
    while Q:
        s= Q.pop(0)
        for i in range(4):
            ny = s[0]+dy[i]
            nx = s[1]+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] =='L' and visit[ny][nx]==0:
                    Q.append([ny,nx,s[2]+1])
                    visit[ny][nx] =s[2]+1
                    count = max(count,s[2]+1)
    return count

result =[]
for i in range(N):
    for j in range(M):
        if graph[i][j]=='L':
            result.append(bfs(i,j,1))
print(max(result)-1)
