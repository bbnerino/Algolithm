
N,M= map(int,input().split())
nums = list(map(int,input().split()))
result=[]
dp = [nums[0]]
for i in range(1,len(nums)):
    dp.append( dp[i-1] + nums[i])
dp.insert(0,0)
# [0, 5, 9, 12, 14, 15]
for ts in range(M):
    s,e = map(int,input().split())
    # 1, 3 -> 0,1,2
    result.append(dp[e]-dp[s-1])
for i in result:
    print(i)