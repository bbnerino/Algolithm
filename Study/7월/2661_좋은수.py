import sys
sys.stdin = open('input.txt')

N = int(input())
def dfs(num):
    nums = ['1', '2', '3']
    if len(num) == N:
        print(num)
        quit()
    for i in nums:
        if len(num)>0:
            if num[-1] != i:
                if check(num+i):
                    dfs(num+i)
        else:
            dfs(num+i)
    pass

def check(num):
    last = len(num)
    for length in range(1, len(num) // 2 +1):  # 자리수
        if num[last-length:last] == num[last-length*2:last-length]:
                return False
    return True

dfs('')


