a, b ,c= map(int,input().split())
big =""
if a < b and a<c :
    small=a
elif b<c and b<a :
    small=b
else :
    small =c
print(small)
