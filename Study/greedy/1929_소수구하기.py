import sys
sys.stdin = open('input.txt')

M,N = map(int,input().split())
nums = [0 for _ in range(N+1)]
sosu = []

for i in range(2,N+1):
    for j in range(2*i,N+1,i):
        nums[j]=1
for i in range(2,len(nums)):
    if nums[i]==0:
        sosu.append(i)

for r in sosu:
    if r>=M:
        print(r)




# for i in range(2,N+1):
#     for j in range(2,N//i+1):
#         try:
#             nums.remove(i*j)
#         except:
#             pass
# for num in nums:
#     if num<M:
#         nums.remove(num)
#
# for n in nums:
#     print(n)
