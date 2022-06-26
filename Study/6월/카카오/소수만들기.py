nums = [1,2,3,4]


def prime_num(n):
    result = list(range(2,n+1))
    for i in range(2,n+1):
        for j in range(2,n//i+1):
            if i*j in result:
                result.remove(i*j)
    return result

def solution(nums):
    answer = 0
    prime_num(sum(nums))



    return answer

solution(nums)
