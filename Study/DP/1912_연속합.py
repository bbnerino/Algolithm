N = int(input())
numlist = list(map(int,input().split()))
dp = [0 for _ in range(N)]
dp[0]= numlist[0]
for i in range(1,N):
    dp[i]= max(dp[i-1]+numlist[i],numlist[i])
print(max(dp))
