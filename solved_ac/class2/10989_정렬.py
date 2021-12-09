import sys
input=sys.stdin.readline
print=sys.stdout.write

n=int(input())
count = [0] *10001
for i in range(n):
    b = int(input())
    count[b]+=1
# [5, 2, 3, 1, 4, 2, 3, 5, 1, 7]

for i in range(len(count)):
    if count[i]>0:
        for j in range(count[i]):
            print('%s\n' % str(i))


    