import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
result=[]
k=0
while nums:
    small = nums.pop(0)
    big = -1
    for i in range(len(nums)):
        if nums[i]>small:
            big= nums[i]
            result.append(big)
            break

    if big==-1:
        result.append(big)
print(*result)
        