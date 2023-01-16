import sys
sys.stdin = open("./2023/1월/input.txt")


N = int(input())
graph = list(map(int,input().split()))


def continuius():
  result = []
  i = graph.pop(0)
  count = 1
  while graph:
    p = graph.pop(0)
    if p == i:
      count+=1
    else :
      if i ==1:
        result.append(count)
      elif i==2:
        result.append(count*(-1))
      i = p
      count =1

  if i ==1:
    result.append(count)
  elif i==2:
    result.append(count*(-1))
  return result

coninus_graph =continuius()

max_count = 0
min_count = 10000000

result = 0
for long in range(1,len(coninus_graph)+1):
  for i in range(len(coninus_graph)-long+1):
    if result< abs(sum(coninus_graph[i:i+long+1])):
      result = abs(sum(coninus_graph[i:i+long+1]))

print(result)