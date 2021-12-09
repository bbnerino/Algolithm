def bfs(y,x):
    Q=[[y,x]]
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]
    visit = [[0]*M for _ in range(N)] 
    while Q:
        s= Q.pop(0)
        graph[s[0]][s[1]]=0
        visit[s[0]][s[1]]=1 # 중복으로 인한 시간 초과를 막기위한 visit
        for i in range(4):
            ny = s[0] + dy[i]
            nx = s[1] + dx[i]
            if 0<=ny<N and 0<=nx<M: # 범위 내에 있고
                if graph[ny][nx]==1 and visit[ny][nx]==0:
                    Q.append([ny,nx])
                    visit[ny][nx]=1


T = int(input())
result=[]
for _ in range(T):
    M,N,K = map(int,input().split()) # 입력받기 가로세로 배추개수
    graph = [[0]*M for _ in range(N)] # 그래프 만들기
    cabbage=[]
    for _ in range(K):
        x,y = map(int,input().split()) # x,y 받아서
        cabbage.append([y,x])
        graph[y][x]=1 # 배추로 바꾸기
    count=0 
    for c in cabbage:
        if graph[c[0]][c[1]] ==1:
            bfs(c[0],c[1])
            count+=1
            
    result.append(count)
for i in result:
    print(i)
    