import sys
sys.stdin = open('input.txt')

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
