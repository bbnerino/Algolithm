N= int(input())
def bfs(x,y):
    Q = [[x,y]] # 첫 값 넣기
    dy = [1,-1,0,0] # 백터값
    dx = [0,0,1,-1]
    while Q: 
        s= Q.pop(0) # Q 뽑아서
        for i in range(4): # 네  방향 순회
            ny = s[0]+dy[i]
            nx = s[1]+dx[i]
            if ny<0 or ny>=N or nx<0 or nx>=N:
                continue
            if newgraph[ny][nx]==0:
                continue
            else: # ny,nx가 범위내에 있고, 그 값이 1인경우 
                newgraph[ny][nx]=0 # 바꿔주고
                Q.append([ny,nx]) # 큐에 넣어준다

# graph 만들기
graph =[]
high=0 # 그래프 내 최대값
for ts in range(N): 
    line = list(map(int,input().split()))
    if high < max(line): # 가장 큰 값 찾기
        high=max(line)
    graph.append(line)

result = [] # 정답
#  1부터 가장 큰 값까지 순회하면서
for rain in range(1,high+1): 
    newgraph = [[0 for _ in range(N)] for _ in range(N)] 
    # 새로운 그래프를 생성해서 1과 0으로 이루어지게 만든다
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= rain: # 만약 그래프[i][j] 값이 비보다 크면
                newgraph[i][j]=1    # 육지(1)가 된다
            else:                   # 비가 더 많이오면
                newgraph[i][j]=0    # 바다(0)가 된다
    
    safezone=0 # 육지 개수
    for i in range(N): 
        for j in range(N): 
            if newgraph[i][j]==1: # 1인지역에서만 bfs를 순회
                safezone+=1 # 1이 하나라도 있으면 육지+1
                bfs(i,j) 
                 
    result.append(safezone)
print(result)
print(max(result))
   
