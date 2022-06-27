nums = [1,2,7,6,4]
from itertools import combinations

def prime_num(n):
    result = list(range(2,n+1))
    for i in range(2,n+1):
        for j in range(2,n//i+1):
            if i*j in result:
                result.remove(i*j)
    return result

def solution(nums):
    primenums = prime_num(3*max(nums))
    print(primenums)
    result =[]
    combis = list(combinations(nums,3))
    for combi in combis :
        tmp=sum(combi)
        if tmp in primenums and tmp not in result:
            result.append(tmp)
    return len(result)

print(solution(nums))
