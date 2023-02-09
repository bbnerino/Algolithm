import sys
sys.stdin = open("./2023/2월/input.txt")
import heapq

V,E = map(int,input().split())
graph = [[]for _ in range(V+1)]

for _ in range(E):
  a,b,l = (map(int,input().split()))
  heapq.heappush(graph[a],[l,b])
def dfs(start_point,count):
  for length,end_point in graph[start_point]:
    if count+length  < visited[end_point]:
      visited[end_point] = count+length

      if end_point == i :
        result.append(count+length)
        break

      else:
        dfs(end_point,count+length)

result = []
for i in range(1,V+1):  
  visited = [1000000 for _ in range(V+1)]
  dfs(i,0)
  result.append(visited[i])

if(len(result)==0):
  print(-1)
else:
  print(min(result))



