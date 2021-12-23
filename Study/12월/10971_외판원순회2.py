import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import permutations

N = int(input())            # 네명이면?
nums = list(range(N))       # 0,1,2,3 네명 만들어주기
graph =[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
every = list(permutations(nums,N)) # 0,1,2,3 으로 만들수 있는 모든 순열 만들기
# print(every)
result = int(1e9)   # 큰값을 하나 만들어 놓는다
for cycle in every: # 아까만든 순열을 하나씩 돌면서
    count =0        # 길의 합을 구해준다
    for i in range(-1,N-1): # (0,1) (1,2) (2,3) (3,0) 을 계산하기 위한 (-1~3)
        if graph[cycle[i]][cycle[i+1]]==0:  # 만약 길이 막혀있다면
            count = int(1e9)                # count 초기화
        else:                               # 길이 열려있다면
            count += graph[cycle[i]][cycle[i+1]]    # 합해준다
    result = min(count,result)              # 이전과 비교해 최소값을 구해준다
                                            # 닫혀있다면 처음 값 그대로
if result == int(1e9):                      # 열린 길이 없다면
    print(0)                                # 0 출력
else:
    print(result)                           # 아니면 결과값 출력
