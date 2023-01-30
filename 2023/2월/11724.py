import sys
sys.stdin = open("./2023/2월/input.txt")

N,M = map(int,input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False for _ in range(N+1)]

def dfs(start):
  node_list = graph[start]
  for i in node_list:
    if not visited[i]:
      visited[i]= True
      dfs(i)
      
result = 0
for i in range(1,N+1):
  if not visited[i]:
    result+=1
    dfs(i)

print(result)


