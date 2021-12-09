def bfs(graph,start):
    visited = [0 for _ in range(T + 1)]
    connect = []
    visited[start]=1
    Q=[start]
    while Q:
        s = Q.pop(0)
        connect.append(s)
        for i in graph[s]:
            if visited[i] == 0:
                Q.append(i)
                visited[i]=1
    return connect

T= int(input())
line=int(input())

graph=[[]for _ in range(T+1)]
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
for ts in range(line):
     s,e=map(int,input().split())
     graph[s].append(e)
     graph[e].append(s)


print(bfs(graph,1)) # [1, 2, 5, 3, 6] 1 제외한 4개의 컴퓨터 
print(len(bfs(graph,1))-1) # 1