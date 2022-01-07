import sys
sys.stdin = open('input.txt')
from itertools import combinations


nums = [0,1,2,3,4,5,6,7,8,9]


result =[]
for i in range(1,11): # 한자리수부터 10자리수(9876543210) 까지 만들어줘야한다.
    combi = list(combinations(nums,i))
    while combi:
        numlist = combi.pop(0)  # 하나씩 뽑아서
        re = ""
        for j in range(len(numlist)-1,-1,-1):# 뒷자리 수부터 하나씩 더해주기
            re+=str(numlist[j])
        result.append(int(re))

result = sorted(result) # 정렬해주게 되면 작은 수부터 나열된다.


N = int(input())

try:
    print(result[N])
except:
    print(-1)


