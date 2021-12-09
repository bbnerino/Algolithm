
def apart(k,n):
    ho_list=list(range(1,n+1)) # 1,2,3,4,5
    for floor in range(1,k+1): # 층마다
        total =0
        for ho in range(n): # 호마다
            total+=ho_list[ho]
            ho_list[ho]=total
    print(ho_list[n-1])

T=int(input())
for i in range(T):
    k=int(input())
    n=int(input())
    apart(k,n)
    
