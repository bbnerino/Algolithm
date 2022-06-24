
numbers = [1,2,3,4,6,7,8,0]
def solution(numbers):
    allnums = [1,2,3,4,5,6,7,8,9,0]
    answer = -1
    for i in numbers:
        allnums.remove(i)
    answer = sum(allnums)
    return answer

print(solution(numbers))