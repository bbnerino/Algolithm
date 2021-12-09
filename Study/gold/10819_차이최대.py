from itertools import permutations
# 조합 구하기 함수

def calculate(nums): # 계산하기 함수
    total=0
    for i in range(len(nums)-1):
        total += abs(nums[i]-nums[i+1])
        # 차이만큼 더해주기
    return total 

N = int(input())
nums= list(map(int,input().split()))

newnums=list(permutations(nums,N)) 
# 모든 조합의 개수가 저장됨
#  (20, 1, 15, 8, 4, 10), (20, 1, 15, 8, 10, 4), (20, 1, 15, 4, 8, 10)..
result = [] # 결과값에 
for i in newnums: # 모든 조합을 돌면서 
    result.append(calculate(i)) # 계산하기 함수로 계산해줌

print(max(result))