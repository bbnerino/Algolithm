#이항 계수 :? 5C2
a,b=map(int,input().split())
ar=1
br=1
cr=1
for i in range(a,0,-1):
    ar*=i
for j in range(b,0,-1):
    br*=j
for k in range(a-b,0,-1):
    cr*=k
print(ar//(br*cr))
