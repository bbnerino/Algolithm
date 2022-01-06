import sys
sys.stdin=open('input.txt')

nums = [True]*10001
nums[1]=False
for i in range(2,10001):
    for j in range(2,10000//i+1):
        nums[i*j] = False
M = int(input())
N = int(input())
result =[]
for i in range(M,N+1):
    if nums[i]==True:
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)