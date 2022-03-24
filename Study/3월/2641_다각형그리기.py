import sys
sys.stdin = open('input.txt')

N = int(input())
sample = list(map(int,input().split()))
M = int(input())
graph = []
for _ in range(M):
    tmp = list(map(int,input().split()))
    graph.append(tmp)



def square(list):
    dy = [0, 0, -1, 0, 1]
    dx = [0, 1, 0, -1, 0]
    point = []
    start = [0, 0]
    point.append(start)

    for i in list:
        ny = dy[i] + start[0]
        nx = dx[i] + start[1]
        start = [ny,nx]
        point.append(start)
    point.pop()
    return point


def sortsquare(list):
    list.sort(key=lambda x: (x[0]))
    list.sort(key=lambda x: (x[1]))
    return list

sample_square = sortsquare(square(sample))

rrr =[]

for g in graph:
    sortthis = sortsquare(square(g))
    result = []
    y = sample_square[0][0]-sortthis[0][0]
    x = sample_square[0][1]-sortthis[0][1]

    for [i,j] in sortthis:
        result.append([i+y,j+x])
    if sample_square == result:
        rrr.append(g)

print(len(rrr))
for i in rrr:
    print(*i)








