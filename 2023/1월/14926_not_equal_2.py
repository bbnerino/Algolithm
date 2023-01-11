import sys
sys.setrecursionlimit(2*(10**5))

N = int(input())
graph = [[] for _ in range(N+1)]

visited = [[0]*(N+1) for _ in range(N+1)]


for i in range(1,N+1):
  for j in range(1,N+1):
    if i!=j :
      graph[i].append(j)
# [[], [2, 3, 4, 5], [1, 3, 4, 5], [1, 2, 4, 5], [1, 2, 3, 5], [1, 2, 3, 4]]

def dfs(start_node):
  print("a{0}".format(start_node),end=" ")
  while graph[start_node]:
    i = graph[start_node].pop(0)
    if visited[start_node][i] == 0: # 방문을 안했다 
      visited[start_node][i] = 1
      visited[i][start_node] = 1
      dfs(i)
              


# visited[1][N] = 1
# visited[N][1] = 1
dfs(1)
print("a1")

