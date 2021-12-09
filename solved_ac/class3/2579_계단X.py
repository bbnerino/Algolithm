N= int(input())

dp = [0]*N
stair=[]
for ts in range(N):
    stair.append(int(input()))
dp[0]=stair[0]
dp[1]= stair[1]
dp[2]= (dp[1]+stair[2],dp[0])
