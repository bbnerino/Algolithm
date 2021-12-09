def bfs(START):
    x_vector = [1,-1,0,0]
    y_vector = [0,0,1,-1]
    Q = [START]
    while Q:
        s = Q.pop(0)
        y,x = s[0],s[1]
        for i in range(4): # 네방향 벡터를 이용해서 넓이 우선탐색
            nx = x+ x_vector[i]
            ny = y+ y_vector[i]
            if nx<0 or nx>M-1 or ny<0 or ny>N-1: # 범위밖
                continue # 벡터 다시 구하기
            if graph[ny][nx] ==0: # 다음 값이 1이 아니면 
                continue # 다시
            if graph[ny][nx] ==1: # 1이면
                graph[ny][nx]= graph[y][x]+1 # 이전값에 +1
                Q.append([ny,nx])

    return graph[N-1][M-1]
N,M = map(int,input().split())
graph=[]
for _ in range(N):
    ma=[]
    ma.extend(map(int,input()))
    graph.append(ma)
START = [0,0]
print(bfs(START))
