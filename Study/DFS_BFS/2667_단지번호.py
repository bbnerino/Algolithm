import sys
sys.stdin = open('input.txt')

N = int(input())
graph=[[]for _ in range(N)]
for _ in range(N):
    graph[_].extend(input())

def bfs(y,x):
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    Q = [[y,x]]
    count = 1
    while Q:
        s =Q.pop(0)
        graph[s[0]][s[1]]='0'
        for i in range(4):
            ny = s[0]+ dy[i]
            nx = s[1]+ dx[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx]=='1':
                    graph[ny][nx]='0'
                    count+=1
                    Q.append([ny,nx])
    countlist.append(count)



countlist=[]
apart =0
for i in range(N):
    for j in range(N):
        if graph[i][j]=='1':
            bfs(i,j)
            apart+=1


print(apart)
for r in sorted(countlist):
    print(r)