import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline
N = int(input())
graph =[]
for _ in range(N):
    graph.append(int(input()))
graph.sort()

newgraph = []
for i in range(N-1):
    newgraph.append(graph[i+1]-graph[i])

# 9 6 6 60 의 최대공약수?

min = min(newgraph)

result =[]
for i in range(2,min+1):
    for n in newgraph:
        if n%i !=0:
            break
        result.append(i)
print(*sorted(list(set(result))))
