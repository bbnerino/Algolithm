
def stack(do):
    global result,finish
    if do[0:4] == "push":
        result.append(int(do[5::]))
    if do == "top":
        if len(result)!=0:
            finish.append( result[-1])
        else:
            finish.append(-1)
        
    if do =="size":
        finish.append(len(result))
    if do == "empty":
        if len(result)==0:
            finish.append(1)
        else:
            finish.append(0)
    if do=="pop":
        try: 
            finish.append(result.pop())
        except:
            finish.append(-1)

result=[]
finish=[]
T= int(input())
for ts in range(T):
    do=input()
    stack(do)
for i in finish:
    print(i)