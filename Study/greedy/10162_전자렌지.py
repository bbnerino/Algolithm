#a=300 b=60 c= 10
T= input()
if T[-1]!="0":
    print(-1)
else:
    t= int(T)
    print(t//300,end=" ")
    t -= 300*(t//300)
    print(t//60,end=" ")
    t -= 60*(t//60)
    print(t//10,end=" ")
    t -= 60*(t//10)
    