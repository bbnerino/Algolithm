import sys
sys.stdin = open('input.txt')
from itertools import permutations



def dfs():
    global count
    for i in range(1,len(nums)+1):              # 1자리부터 nums길이까지의 순열을
        combi = list(set(permutations(nums,i)))
        while combi:
            strnums = combi.pop()
            strnum = ''
            for s in strnums:
                strnum+=s
            if sosu(int(strnum)) and visited[int(strnum)]:
                count+=1
                visited[int(strnum)]= False

def sosu(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True



c = int(input())
for _ in range(c):
    original=input()        # 1276543
    nums = list(original)   # [1,2,7,6,5,4,3]
    visited =[True]*(10**len(nums)) # 8자리 까지중 중복 제거
    count = 0               # 총 소수 갯수
    dfs()
    print(count)

