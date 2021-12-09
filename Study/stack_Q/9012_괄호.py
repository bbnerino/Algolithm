T= int(input())
result=[]
for ts in range(T):
    stack=[]
    gualho=input()
    yesno=""

    for i in gualho:
        if i == "(":
            stack.append("(")
        if i== ")":
            if len(stack)==0:
                yesno="NO"
                break
            else:
                stack.pop()
    if yesno=="":
        if len(stack)==0:
            yesno="YES"
        else:
            yesno="NO"
    result.append(yesno)
for i in result:
    print(i)