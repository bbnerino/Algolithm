import sys
sys.stdin = open('input.txt')

# 15의 배수라는 것은 다 합쳐서 3의 배수 + 맨뒷자리가 5

N = int(input())
dp = [0]*(1516)
# 0 1 2 3 4 5  6  7  8  9   10  11  12   13   14
# 0,0,1,1,4,9,19,40,83,167.338,679,1361,2726,5457

dp[1]= 0
dp[2]= 1
dp[3]= 1
dp[4]= 4
# dp[5] =

for i in range(5,1516):
    dp[i] = (dp[i-1]*2 + i-4)%1000000007
# print(dp[6])
count=0
def dfs(strnum):
    global count
    if len(strnum) == N:
        return
    for one_five in ['1','5']:
        newnum = strnum + one_five
        if int(newnum)%15 ==0 and len(set(newnum))!=1:
            count+=1
            # print(newnum)
        dfs(newnum)

dfs("")
print(count)