import sys
sys.stdin =open('input.txt')

A,B = map(int,input().split())
Ay = []
for i in range(1,A+1):
    if A%i ==0:
        Ay.append(i)
By = []
for i in range(1,B+1):
    if B%i ==0:
        By.append(i)

최대공약수 = 0
flag = 0
for i in Ay:
    for j in By:
        if i==j:
            최대공약수 = i

print(최대공약수)
최소공배수 = A//최대공약수 * B//최대공약수 * 최대공약수
# 최소공배수 = A*B//최대공약수
print(최소공배수)
