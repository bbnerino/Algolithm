import sys
sys.stdin = open("./2023/2월/input.txt")
import heapq

V,E = map(int,input().split())
graph = [[]for _ in range(V+1)]
INF = 1e9
dist = [[INF]*(V+1) for _ in range(V+1)]
# a->b 의 거리 

H = []
for _ in range(E):
  a,b,l = map(int,input().split())
  graph[a].append([l,b])
  dist[a][b] = l
  heapq.heappush(H,[l,a,b])

while H:
  l,s,e = heapq.heappop(H)
  if (s==e):
    print(l)
    break
  if dist[s][e] < l:
    continue

  for nl,ne in graph[e]:
    new_l = l + nl
    if new_l < dist[s][ne]:
      dist[s][ne] = new_l
      heapq.heappush(H,[new_l,s,ne])

else:
  print(-1)





