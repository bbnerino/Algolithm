T= int(input())
stack=[]
for ts in range(T):
    num=int(input())
    if num==0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))