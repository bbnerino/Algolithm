import sys
sys.stdin = open('input.txt')

N = int(input())

sosu = []
for i in range(2,N):
    flag = True
    for j in range(2,i):
        if i%j ==0:
            flag = False
    if flag:
        sosu.append(i)

nums = list(range(N))

print(sosu)