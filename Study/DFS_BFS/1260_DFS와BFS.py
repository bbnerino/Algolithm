N,M,V = map(int,input().split())
graph = [[]for _ in range(N+1)]

for i in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(N+1):
    graph[i].sort()

visited_dfs=[0]*(N+1)
visited_bfs =[0]*(N+1)
stack = [V]
Q =[V]

def dfs(start):
    visited_dfs[start]=1
    s = stack.pop()
    print(start,end=" ")

    for i in graph[s]:
        if visited_dfs[i]==0:
            stack.append(i)
            dfs(i)

def bfs(start):
    visited_bfs[start]=1
    while Q:
        s= Q.pop(0)
        print(s,end=" ")
        for i in graph[s]:
            if visited_bfs[i]==0 :
                Q.append(i)
                visited_bfs[i]=1

dfs(V)
print()
bfs(V)