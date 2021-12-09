T= int(input())
nums=[]
for ts in range(T):
    x,y=map(int,input().split())
    nums.append([x,y])
nums.sort(key=lambda x:(x[1],x[0]))

for i in range(T):
    print(*nums[i])