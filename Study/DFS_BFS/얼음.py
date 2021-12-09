# p) 145 얼음이 얼마나 붙어있나 0끼리 묶인 개수 구하기
N,M = map(int,input().split())
graph =[]
for i in range(N):
    graph.append(list(map(int,input())))
result=0


def dfs(x,y):
    if  0<=x<N and  0<= y<M:
        if graph[x][y]==0:
            graph[x][y]=1
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
    else:
        return False
    
for i in range(N):
    for j in range(M):
        if dfs(i,j)==True:
            result+=1
print(result)