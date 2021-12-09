import sys
sys.stdin= open('input.txt')

from collections import  deque
from itertools import permutations
N = int(input())
nums = list(map(int,input().split()))
ca_list = list(map(int,input().split()))

calculation =[]
for i in range(4):
    if i ==0:
        for _ in range(ca_list[i]):
            calculation.append('+')
    elif i ==1:
        for _ in range(ca_list[i]):
            calculation.append('-')
    elif i ==2:
        for _ in range(ca_list[i]):
            calculation.append('*')
    elif i ==3:
        for _ in range(ca_list[i]):
            calculation.append('/')

permu_calculation = list(map(list,permutations(calculation,len(calculation))))

result =[]

while permu_calculation:
    this_calcultation = deque(permu_calculation.pop())
    new_nums = deque(nums[:])
    first = new_nums.popleft()
    while new_nums:
        what = this_calcultation.popleft()
        second = new_nums.popleft()
        if what=='+':
            first += second
        elif what == '-':
            first-= second
        elif what == '*':
            first *= second
        elif what == '/':
            if first<0:
                first = -1* (abs(first)//second)
            else:
                first //= second
    result.append(first)

# print(result)
print(max(result))
print(min(result))


