
T = int(input())
result=[]
for _ in range(T):
    cloth ={}
    same =[]
    N = int(input())
    for _ in range(N):
        name,category = input().split()

        if category not in same:
            cloth[category]=0
            same.append(category)
        cloth[category]+=1
#  {'headgear': 2, 'eyewear': 1}

    total=1
    for key,value in cloth.items():
        total*= value+1
    result.append(total-1)

for i in result:
    print(i)

