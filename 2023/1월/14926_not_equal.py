import sys
sys.stdin = open("./2023/1월/input.txt")
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N)]
graph_count = 0
for i in range(N):
  for j in range(N):
    if i!=j :
      graph[i].append(j)
      graph_count+=1

result = 99999999999999
# [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]
count2 = 0
now = 0
def dfs(start_node,count,visited):
  global result
  global count2
  for number in graph[start_node]:
    if visited[start_node][number] == 0: # 방문을 안했다 
      visited[start_node][number] = 1
      visited[number][start_node] = 1
      dfs(number,count+str(number+1),visited)
      visited[start_node][number] = 0
      visited[number][start_node] = 0
      if len(count)*2 == graph_count:
        result = min(int(count),result)
        print(sort_result(result))
        exit()
        

def sort_result (result):
  r = ""
  for i in str(result):
    r += "a{0} ".format(i)
  r += "a1"
  return(r)

visited = [[0]*N for _ in range(N)]
dfs(0,"1",visited)
print(sort_result(result))
