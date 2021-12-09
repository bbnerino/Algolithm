N= int(input())
if N>=3:
    dp=[0 for _ in range(N+1)]
    dp[1]=1 # 한자리 -> 1
    dp[2]=1 # 두자리 -> 10
    for i in range(3,N+1):
        dp[i]=dp[i-1]+dp[i-2]
    print(dp[N])
else: # N이 1와 2일때 따로 구하기
    if N==1:
        print(1)
    elif N==2:
        print(1)
