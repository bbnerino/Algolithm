
a=int(input())
num=[1]
i=1
if a==1:
    print(1)

while i!=a:
    num.append(num[-1]+ 6*i)
    
    if num[i-1]<a<=num[i]:
        print(i+1)
        break
    else:
        i+=1
    
    
