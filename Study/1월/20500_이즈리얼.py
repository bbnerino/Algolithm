import sys
sys.stdin = open('input.txt')

# 15의 배수라는 것은 다 합쳐서 3의 배수 + 맨뒷자리가 5

N = int(input())
dp = [0]*(1516)
# 0 1 2 3 4 5  6  7  8  9   10  11  12   13   14
# 0,0,1,1,3,5, 11,21,43,85,171,341,683,1365 ,2731
# 0
dp[1]= 0
dp[2]= 1
dp[3]= 1

for i in range(4,1516):
    if i%2==0:
        dp[i]= (dp[i-1]*2 +1)%1000000007
    else:
        dp[i]= (dp[i-1]*2 -1)%1000000007

# count=0
# def dfs(strnum):
#     global count
#     if len(strnum) == N:
#         return
#     for one_five in ['1','5']:
#         newnum = strnum + one_five
#         if int(newnum)%15 ==0 and len(newnum)==N:
#             count+=1
#             result.append(newnum)
#             # print(newnum)
#         dfs(newnum)
#
# dfs("")

print(dp[N])