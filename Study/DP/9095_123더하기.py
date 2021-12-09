T= int(input())
dp=[0 for _ in range(12)] # 11까지 빈값 만들기
dp[1]=1 
dp[2]=2
dp[3]=4
for i in range(4,12):# 4,5...11까지
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    # 공교롭게도 세수의 합이다
result =[]
for ts in range(T):
    n = int(input())
    result.append(dp[n])
for num in result:
    print(num)