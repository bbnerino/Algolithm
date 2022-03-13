import sys
sys.stdin = open('input.txt')
from itertools import product
from collections import deque
# 중복 순열

numlist = list(range(1,10))

perlist = list(product(numlist,numlist,numlist,numlist))
# 1~9까지의 값들로 이루어진 4자리 중복순열

def crossCard(list) : # 시계방향으로 네번 돌려서 네자리 수 중 가장 작은 수를 찾아내는 함수
    Nlist = deque(list) # 로테이트를 위한 데큐 사용
    small = 10000
    for _ in range(4): # 시계방향으로 4번 돌리기
        Nlist.rotate()
        num = ''
        for i in Nlist:
            num += str(i)
        if small>= int(num):
            small = int(num)
    return small

result = []

for ilist in perlist:   # 중복순열 하나씩 다 확인해서
    result.append(crossCard(ilist)) # 결과값만 저장해준다.

result = list(set(result)) # 중복값을 빼주기 위한 list(set()) 함수 사용
result.sort()               # 정렬시켜주고

input = list(map(int,input().split()))
tmp = crossCard(input)      # input으로 들어온 값의 위치가 어딨는지 찾아준다.
print(result.index(tmp) +1)