import sys
def nonrepeat(n):
    n = str(n)
    check =[0 for _ in range(10)]
    for i in n:
        if check[int(i)]==0:
            check[int(i)]=1
        else:
            return False
    return True

q=[]
big=0
while True:
    num = int(sys.stdin.readline())
    if num==0:
        break
    big = max(num,big)
    q.append(num)


numlist = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27]
i=28
while len(numlist) <= big:
    i = str(i)
    check = [0 for _ in range(10)]
    TF = True
    for j in i:
        if check[int(j)]==0:
            check[int(j)]=1
        else:
            TF=False
            break
    if TF:
        numlist.append(int(i))
    i=int(i)
    i+=1

for i in q:
    print(numlist[i])