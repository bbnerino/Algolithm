N= int(input())
p = list(map(int,input().split()))
p = sorted(p) # 1,2,3,3,4
sum=0
gop= N
for i in range(len(p)):
    sum+= p[i]*gop # 1x5 + 2x4 + 3x3 + 3x2 + 4x1
    gop-=1
print(sum)
