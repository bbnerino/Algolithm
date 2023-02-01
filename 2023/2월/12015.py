import sys
sys.stdin = open("./2023/2월/input.txt")

N = int(input())
num_list = list(map(int,input().split()))

dp = [0]
# [10,20,10,30,20,50]
for num in num_list :
  if num > dp[-1]:
    dp.append(num)
  else:
    left = 0
    right = len(dp)
    
    while left < right:
      mid = (left+right)//2
      if dp[mid] < num:
        left = mid+1
      else:
        right = mid
    dp[right] = num

print(len(dp)-1)