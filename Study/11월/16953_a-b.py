import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start,target):
    Q = deque()
    Q.append([1,start])
    check= 0
    while Q:
        count,start = Q.popleft()
        if start < target:
            Q.append([count+1,10*start+1])
            Q.append([count+1,start*2])
        if start == target:
            check = count
            break
    if check:
        print(check)
    else:
        print(-1)

start, target = map(int,input().split())
bfs(start,target)
