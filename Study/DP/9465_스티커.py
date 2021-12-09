T= int(input())
result = []
for _ in range(T):
    n = int(input())
    dp = [list(map(int,input().split())), list(map(int,input().split()))]

    if n==1:
        result.append(max(dp[0][0],dp[1][0]))
        continue
    
    dp[0][1]+= dp[1][0] # 두번째 값 = 두번째값 + 첫번째 값
    dp[1][1]+= dp[0][0]

    for i in range(2,n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2]) # 앞의 것과 앞앞 것 중 큰거에 더해줌
        dp[1][i] += max(dp[0][i-1], dp[0][i-2]) 
    
    result.append(max(dp[0][n-1], dp[1][n-1])) # 마지막 값 두개중 큰게 답
for r in result:
    print(r)
