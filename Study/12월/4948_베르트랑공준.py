import sys
sys.stdin=open('input.txt')


sosu = [True]*(123456*2+1)

for i in range(2,123456):
    for j in range(2,123456*2//i+1):
        sosu[i*j]=False

while True:
    n = int(input())
    if n!=0:
        print(sosu[n+1:2 * n + 1].count(True))
    else:
        exit()