# 괄호를 쳐서 값을 최소로 만들어라

import sys
sys.stdin = open("./2023/1월/input.txt")

# 적혀져 있는 수가 제일 작아진다..
# a - b + c + d - e 
# 일 때, 합이 제일 작기 위해서는 빼기 등호 뒤에 나오는 수를 가장 크게 만들어야 한다.
# '-'로 이 문자를 나눴을 때, 처음의 a는 냅두고, b+c+d는 당연히 b+c+d-e 보다 크다 
# 즉 a - (b+c+d) - e 가 가장 작은 수가 될 것이다.

# 방법 - 를 이용해 문구를 파싱한다.
# [a] - [b+c+d] - [e]
# 파싱한 list 들의 합을 구하고, 계산을 한다.

numlist_split_minus = input().split("-")
def sum_str_cal(str_cal:list):
  # str_cal = 'b+c+d'
  sum = 0
  list_split_plus = str_cal.split("+")
  for str_num in list_split_plus:
    sum+=int(str_num)
  return sum

result = sum_str_cal(numlist_split_minus.pop(0))

while numlist_split_minus:
  result-= sum_str_cal(numlist_split_minus.pop(0))

print(result)