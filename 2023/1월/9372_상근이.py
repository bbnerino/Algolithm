import sys
sys.stdin = open("./2023/1월/input.txt")

# 그래프 이론
# 트리

def dfs(node):
  visted[node] = 1
  for i in graph[node]:
    if visted[i] == 0:
      route.append(i)
      dfs(i)

tc = int(input())
for _ in range(tc):
  N,M = map(int,input().split())
  graph = [[] for _ in range(N+1)]
  for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
  visted = [0]*(N+1)


  start = 1
  route = [start]
  dfs(start)
  print(len(route)-1)
  

