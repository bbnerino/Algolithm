import sys
sys.stdin = open('input.txt')

R,C = map(int,sys.stdin.readline().split())
graph =[[]for _ in range(R)]
for i in range(R):
    graph[i].extend(map(lambda x:ord(x)-65,sys.stdin.readline().rstrip()))


def dfs(a,b,count):
    global mx
    for i in range(4):
        ny = a+dy[i]
        nx = b+dx[i]
        if 0<=ny<R and 0<=nx<C:
            if visit[graph[ny][nx]]==0 and check[ny][nx]==0:
                visit[graph[ny][nx]]=1
                check[ny][nx]=1
                dfs(ny,nx,count+1)
                visit[graph[ny][nx]]=0
                check[ny][nx]=0
            else:
                if count > mx:
                    mx =count

visit = [0 for _ in range(26)]
visit[graph[0][0]]=1
dy =[0,0,1,-1]
dx =[1,-1,0,0]
mx = 1
check = [[0 for _ in range(C)]for _ in range(R)]
dfs(0,0,1)
print(mx)