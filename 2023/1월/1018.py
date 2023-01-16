import sys
sys.stdin = open("./2023/1월/input.txt")

N,M = map(int,input().split())
graph =  []
for _ in range(N):
  graph.append(list(input()) )

def search_board(y,x):
  count = []
  for START_WORD in ["W","B"]:
    tmp = 0
    for i in range(y,y+8):
      for j in range(x,x+8):
        if (i+j)%2 ==0: 
          if graph[i][j]!=START_WORD:
            tmp+=1
        else:
          if graph[i][j]==START_WORD:
            tmp+=1
    count.append(tmp)
  return min(count)

result = []
for i in range((N-8)+1):
  for j in range((M-8)+1):
    result.append(search_board(i,j))
print(min(result))
