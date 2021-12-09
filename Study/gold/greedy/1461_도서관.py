N,M= map(int,input().split())
books=list(map(int,input().split()))
# [-39, -37, -29, -28, -6, 2, 11]
left=[] # 음수
right=[] # 양수를 나눈다
for i in books:
    if i >0 :
        right.append(i)
    else:
        left.append(abs(i))
left.sort()  # [6 28 29 37 39] 
right.sort() # [2 11]

new = []

while len(left)>0:
    new.append(left.pop())  # 가장 큰 값을 넣어주고
    for i in range(M-1): # M개중 1개가 빠졌으니 M-1번 pop을 해서 없애준다
        try:
            left.pop()
        except:
            pass        # [39, 29, 6]

while len(right)>0:  
    new.append(right.pop())
    for i in range(M-1):
        try:
            right.pop()
        except:
            pass        # [11]

# [11, 39, 29, 6]
print(2*sum(new)-max(new)) # 가장 큰 값은 두번 순회 안하도록 
