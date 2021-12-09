N= int(input())
dp =[0] * (N+1)
if N>3: 
    dp[2]= 1
    dp[3]= 1 
    for i in range(4,N+1):
        two=10**7  # 임의의 큰값 
        three=10**7

        plus_one= dp[i-1] +1  # i-1의 값+1
        
        if i%3==0: # 3의배수일때
            three = dp[i//3] +1 # i/3의 값 
        if i%2==0: 
            two = dp[i//2] +1
        
        dp[i] = min(plus_one,two,three) # 가장작은값을 구한다.
else:
    if N==1:
        dp[N]=0
    elif N==2 or N==3:
        dp[N]=1
print(dp[N])