n="start"
result=[]
while n!=".":
    n=input()
    stack=[]
    yorn=""
    for i in n:
        if i =="[" or i=="(":
            stack.append(i)
        elif i ==")":
            if len(stack)!=0:
                if stack[-1]== "(":
                    stack.pop()
                else:
                    yorn="no"
                    break
            else:
                yorn="no"
                break
        elif i =="]":
            if len(stack)!=0:
                if stack[-1]=="[":
                    stack.pop()
                else:
                    yorn="no"
                    break
            else:
                yorn="no"
                break
    if yorn=="":
        if len(stack)==0:
            yorn="yes"
        else:
            yorn="no"
    result.append(yorn)
for i in result[0:-1]:
    print(i)

