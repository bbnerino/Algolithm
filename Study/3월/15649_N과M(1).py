import sys
sys.stdin = open('input.txt')
from itertools import permutations

N,M = map(int,input().split())

nlist = list(range(1,N+1))

result = list(permutations(nlist,M))

for i in result:
    print(*i)