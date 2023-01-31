
def solution(n, computers):
    answer = 0
    visited = [[False]*(n) for _ in range(n)]
    
    def dfs(y,x):
      visited[y][x] = True
      for i in range(n):
        if computers[x][i] == 1 and not visited[x][i]:
          dfs(x,i)    
     
    for i in range(n):
      for j in range(n):
        if computers[i][j] and not visited[i][j]:
          answer+=1
          dfs(i,j)

    return answer

n = 3
computers = 	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
#  1 1 0 
#  1 1 0 
#  0 0 1
print(solution(n,computers))