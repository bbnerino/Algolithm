


a,b=map(int,input().split())
a_list=[]
b_list=[]
for i in range(1,a+1):
    if a%i  ==0:
        a_list.append(i)
for i in range(1,b+1):
    if b%i ==0:
        b_list.append(i)

result=[]

for i in a_list:
    for j in b_list:
        if i==j :
            result.append(i)

maxre =max(result)

print(maxre)
print(maxre* a//maxre * b//maxre)

