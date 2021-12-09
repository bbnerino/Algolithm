N,M,K,X = map(int,input().split())
# N= 도시개수 M = 도로개수 K= 거리정보 X = 출발도시
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e) # 방향성이 있다
# [[], [2, 3], [3, 4], [], []] 

def bfs(start):
    global short
    Q = [start]
    visit = [0 for _ in range(N+1)] # 방문여부
    short = [0 for _ in range(N+1)] # 거리계산
    while Q: 
        s = Q.pop(0)
        visit[s]=1 # 방문해주고
        if short[s] > K: # 만약 찾을 거리가 이미 넘었다면 
            break       # 더이상 할 필요가 없다
        for i in graph[s]:  
            if visit[i] ==0: # 방문을 하지 않았다면
                if short[i]==0:  # 거리가 아직 계산이 되지 않았다면
                    short[i] = short[s]+1  # 그 전 거리에서 +1
                    Q.append(i)
                else: # 방문을 했더라도 더 짧은 거리를 찾기
                    short[i] = min( short[i] , short[s]+1)  # 짧은걸로 교체
    return short 

result = bfs(X) # X부터의 거리 계산
# print(result) 
# [0, 0, 1, 1, 2]
if K in result: # 최단거리가 K인 도시 찾기 
    for i in range(len(result)): 
        if result[i] == K:
            print(i)
else:
    print(-1)
