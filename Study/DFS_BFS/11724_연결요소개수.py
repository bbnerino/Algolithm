import sys

def bfs(num):
    Q = [num]
    while Q:
        s = Q.pop(0)
        for i in graph[s]:
            if visit[i]==0:
                Q.append(i)
                visit[i]=1

N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count=0
visit = [0 for _ in range(N+1)]
for i in range(1,N+1):
    if visit[i]==0:
        bfs(i)
        count+=1
sys.stdout.write(str(count))