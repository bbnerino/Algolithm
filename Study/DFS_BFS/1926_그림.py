import sys
sys.stdin = open('input.txt')

def bfs(y,x):
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    Q = [[y,x]]
    count =1
    while Q:
        s = Q.pop(0)
        graph[s[0]][s[1]]=0
        for i in range(4):
            ny = dy[i]+s[0]
            nx = dx[i]+s[1]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx]==1:
                    graph[ny][nx]=0
                    count+=1
                    Q.append([ny,nx])

    countlist.append(count)


N,M = map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
countlist =[]




for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            bfs(i,j)
if len(countlist)>0:
    print(len(countlist))
    print(max(countlist))
else:
    print(0)
    print(0)
