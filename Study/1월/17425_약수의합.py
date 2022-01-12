import sys
sys.stdin = open('input.txt')
input= sys.stdin.readline


INF = 1000000
dp = [0]*(INF+1)
for i in range(1,INF+1): # 1부터 하나씩 모든 약수들을 적는 칸에 추가해준다.
    for j in range(1,INF//i+1):
        dp[i*j]+=i

for i in range(1,INF+1):
    dp[i] += dp[i-1]

T = int(input())

for _ in range(T):
    print(dp[int(input())])


