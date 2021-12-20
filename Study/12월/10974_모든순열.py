from itertools import permutations

N = int(input())
nums = list(range(1,N+1))

permu = list(permutations(nums,N))
for i in permu:
    print(*i)

