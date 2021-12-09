import sys
sys.stdin = open('input.txt')

N,M,H = map(int,input().split())
graph = [[]for _ in range(H)]
visit = [[[0]*N for _ in range(M)] for _ in range(H)]
for i in range(H):
    for _ in range(M):
        graph[i].append(list(map(int,input().split())))

result =0
def bfs(a,b,h,count):
    global result
    Q = [[a,b,h,count]]
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    while Q:
        s = Q.pop(0)
        for j in (0,-1,1):
            height =s[2]+j
            if 0 <= height < H:
                for i in range(4):
                    ny = s[0] + dy[i]
                    nx = s[1] = dx[i]
                    if 0<=ny<M and 0<=nx<N:
                        if graph[height][ny][nx]== 0:
                            graph[height][ny][nx]= 1
                            Q.append([ny,nx,height,s[3]+1])
                            result = max(result,s[3]+1)
    return result

rr = []
flag =1
while True:
    if flag==0:
        break
    for h in range(H):
        for i in range(M):
            for j in range(N):
                if graph[h][i][j]==1 and visit[h][i][j]==0:
                    flag = 1
                    bfs(i,j,h,0)
                    visit[h][i][j]=1
                    continue
    flag = 0
print(graph)
print(visit)


if flag==0:
    print(-1)
if flag==1:
    print(rr)

