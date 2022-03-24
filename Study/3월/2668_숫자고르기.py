import sys
sys.stdin = open('input.txt')

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

print(nums)