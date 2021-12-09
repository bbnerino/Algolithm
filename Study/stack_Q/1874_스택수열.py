T= int(input()) 
numlist=[]
for ts in range(T):
    numlist.append(int(input()))
# [4, 3, 6, 8, 7, 5, 2, 1]
# 갖고있는값 12345678

stack=[]
result=[]
num=1 # 
for i in range(T): # numlist 하나씩 순회할 것
    # 
    while num <= numlist[i]:  # num이 인덱스보다 작다면
        stack.append(num) # 스택에 추가해준다  1 2 3 4 // 
        result.append("+") # 스택 추가의 표시
        num+=1 # num+1
    if stack[-1] == numlist[i]: # 스택 마지막 값이 인덱스 값이라면
        stack.pop() # 스택에서 빼내고  4를 빼준다  // 123
        result.append("-") # pop 표시 4
    else: # 아무리 빼고 더해도 마지막 값이 인덱스값이 아니라면
        result=["NO"] # 결과값이 나오지 않는다
        break
for i in result:
    print(i)