def dfs(i,j):
    if 0<=i<x and 0<=j<y:
        if graph[j][i]==1:
            graph[j][i]=0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j+1) # 대각선 네방향 순회
            dfs(i-1,j-1)
            dfs(i+1,j-1)
            dfs(i-1,j+1)
            return True
    else:
        return False

extreme_result=[]
while True:
    x,y = map(int,input().split()) 
    if x==0 and y==0:
        break 
    graph = []
    for ts in range(y):
        graph.append(list(map(int,input().split())))


    result=0
    for i in range(x):
        for j in range(y):
            if dfs(i,j):
                result+=1


    extreme_result.append(result)

for i in extreme_result:
    print(i)
    
    


