
def marathon(origin,num):
    global solv
    next =origin-num
    if next >=0:
        solv.append(next)
        return marathon(num,next)
    else:
        return solv

N= int(input())
long=0
result=[]
for num in range(N+1):
    solv= [N,num]
    mm=marathon(N,num)
    if len(mm) > long:
        long=len(mm)
        result=mm
print(long)
print(*result)