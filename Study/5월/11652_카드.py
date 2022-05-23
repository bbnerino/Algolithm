import sys
sys.stdin = open('input.txt')

N = int(input())
graph ={}
for _ in range(N):
    tmp = int(input())
    if tmp in graph: #
        graph[tmp]+=1
    else:
        graph[tmp] = 1

# print(graph) ==> {5: 2, 3: 2, 1: 1}
# print(graph.items())
values = list(graph.values())
keys = list(graph.keys())
big = 0
result = 1e20

for i in range(len(values)):
    if values[i]==big and keys[i]<result: # 갯수가 똑같은데 이번 게 더 작다면?
        big = values[i]
        result = keys[i]

    if values[i]>big:
        big=values[i]
        result= keys[i]

print(result)







