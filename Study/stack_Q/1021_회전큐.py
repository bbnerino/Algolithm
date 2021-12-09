N,M = map(int,input().split())
findlist = list(map(int,input().split()))
# 2,9,5
Q = list(range(1,N+1))
count=0
while findlist:
    index = findlist.pop(0)
    # 찾을값 뽑아주기
    # 현재위치 q의 젤 왼쪽
    if index == Q[0]:
        Q.pop(0)
        pass
    else:
        if Q.index(index) < len(Q)/2:
            while index != Q[0]:
                Q.append(Q.pop(0))
                count+=1
            Q.pop(0)
        else:
            while index != Q[0]:
                Q.insert(0,Q.pop())
                count+=1
            Q.pop(0)
print(count)

