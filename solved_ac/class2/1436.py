six=str(666)
n= int(input())
if n<10:
    if n<=6:
        print(str(n)+six)
    elif 6<n<=9:
        print(six+str(n))
if 10<=n<100:
    if 60<=n<66:    
        print(str(n)+six)
    else: 
        print(str(n)[0]+six+str(n)[1])
if 100<=n<1000:
    n=str(n)
    if n[1]=='6' :
        print(n[0]+n[1]+six+n[2])
    if n[0]=='6' :
        print(n[0]+n[1]+six+n[2])
    else:
        print(n+six)
else:
    print(str(n)+six)