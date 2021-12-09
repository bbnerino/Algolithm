import sys
sys.stdin = open('input.txt')


def dfs(y,x,num):
    global count
    dy =[0,0,-1,1]
    dx =[1,-1,0,0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<M and 0<=nx<N:
            if graph[ny][nx]<num:
                if ny==M-1 and nx==N-1:
                    count+=1
                else:
                    dfs(ny,nx,graph[ny][nx])



M,N = map(int,input().split())
graph =[]
for _ in range(M):
    graph.append(list(map(int,input().split())))
visit = [[0]*M for _ in range(N)]
count =0
dfs(0,0,graph[0][0])
print(count)