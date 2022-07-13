import sys
sys.stdin = open('input.txt')

N = int(input())

sosu = []
for i in range(2,N+1):
    flag = True
    for j in range(2,i):
        if i%j ==0:
            flag = False
    if flag:
        sosu.append(i)


count = 0
for i in range(1,len(sosu)):
    for j in range(len(sosu)-i+1):
        combi = sosu[j:j+i]
        if sum(combi) == N:

            count+=1


print(count)
