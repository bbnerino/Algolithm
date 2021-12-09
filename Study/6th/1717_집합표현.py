import sys
sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x]= find(parent[x])
        return parent[x]

def union(x,y):
    a = find(x)
    b = find(y)
    if a<b:
        parent[b]=a
    elif a>b:
        parent[a]=b


N,M = map(int,input().split())
parent = list(range(N+1))

for _ in range(M):
    know,a,b = map(int,input().split())

    if know==0:
        union(a,b)

    elif know==1:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')