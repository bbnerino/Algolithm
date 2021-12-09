n=int(input())

if n>1: # n이 1일때를 위해서 넣어
    dp =[0 for _ in range(n+1)] # 메모리제이션
    dp[1]=1 
    dp[2]=3

    for i in range(3,n+1): # 2,3,4,5.. n-1
        dp[i] = dp[i-1]+ dp[i-2]*2 
        # dp로 찾아보면 i의값은 전 + 2전전의 값을 갖는다
    print(dp[n]%10007)
else:
    print(1)