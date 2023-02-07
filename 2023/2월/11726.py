import sys
sys.stdin = open("./2023/2월/input.txt")



N = int(input())
dp  = [0 for _ in range(N+1)]
dp[1] = 1
if(N>2):
  dp[2] = 2
  for i in range(3,N+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[N]%10007) 