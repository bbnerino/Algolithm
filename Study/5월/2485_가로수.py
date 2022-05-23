import sys
sys.stdin = open('input.txt')

N = int(input())
difference  = []
before = 0
for _ in range(N):
    this = int(input())
    if before!=0:
        difference.append(this-before)
    before = this

# 최소 공배수를 구해서 각 차이의 N-1 개 씩해서 더하면 총개수를 구할 수 있다.

def LCM(lst)  : # 최소공배수 구하기
    small = lst[0] # 1부터  가장 작은 수까지 다 찾아보는데
    result = 0

    for num in range(1,small+1):
        flag = True
        for i in difference:
            if i%num !=0:
                flag = False
                break
        if flag:
            result = num
    return result

lcm = LCM(difference)
result = 0
for i in difference:
    result += i//lcm-1
print(result)


