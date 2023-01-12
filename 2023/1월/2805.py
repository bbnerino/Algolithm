import sys
sys.stdin = open("./2023/1월/input.txt")
input = sys.stdin.readline

N,M = map(int,input().split())
trees = list(map(int,input().split()))

start = 0
end = max(trees)

# M 미터를 가져가는 것이 아닌
# 적어도 M 미터.. 어떤 차이가 있을까
while start<=end:
  mid = (start+end)//2
  sum = 0

  for tree in trees:
    if tree-mid>0:
      sum += tree-mid
  
  if sum ==M:
    print(mid)
    exit() 
  elif sum < M:
    end = mid-1
  elif sum > M:
    start = mid+1
print(start,end)