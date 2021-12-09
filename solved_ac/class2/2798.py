N,M = map(int,input().split())

num_list= list(map(int,input().split()))
num_list= sorted(num_list)

result=0

for first in range(0,len(num_list)):
    for second in range(first+1,len(num_list)):
        for third in range(second+1,len(num_list)):
            summ = num_list[first] +num_list[second] +num_list[third]

            if result <= summ <= M:
                result=summ
                
print(result)
