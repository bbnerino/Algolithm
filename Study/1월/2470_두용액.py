import sys
sys.stdin =open('input.txt')

input = sys.stdin.readline
N = int(input())
graph = sorted(list(map(int,input().split())))

s, e = 0,N-1

# [-99, -2, -1, 4, 98]
result   =[0,N-1,graph[0]+graph[1]]
while s<e:
    if abs(result[2]) >= abs(graph[s]+graph[e]):
        result = [s,e,graph[s]+graph[e]]

    if graph[s]+graph[e] <= 0:
        s+=1
    elif graph[s]+graph[e]>0:
        e-=1
    else:
        break
print(graph[result[0]],graph[result[1]])

