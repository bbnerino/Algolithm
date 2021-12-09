n=int(input())
nums=[]
for i in range(n,0,-1):
    str_i=str(i)
    result= i*1
    for j in range(len(str_i)):
        result+=int(str_i[j])
    
    if result ==n:
        nums.append(i)

if len(nums) !=0:
    print(min(nums))
else:
    print(0)
