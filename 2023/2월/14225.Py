import sys
sys.stdin = open("./2023/2월/input.txt")

from itertools import combinations

N = int(input())
nums = sorted(list(map(int,input().split())))
visited = [False for _ in range(sum(nums)+2)]

for counts in range(1,N+1):
  tmp = list(combinations(nums,counts))
  for i in tmp:
    visited[sum(i)]= True
for i in range(1,len(visited)):
  if not visited[i] :
    print(i)
    exit()