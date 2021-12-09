T= int(input())

result=[]
for ts in range(T):
    length= int(input())
    before = input()   
    after = input()

    B2W=0
    W2B=0
    total=0
    for i in range(len(before)):
        if before[i]== "W" and after[i]=="B":
            W2B +=1
        elif before[i]=="B" and after[i]=="W":
            B2W +=1
    
    while B2W!=0 and W2B!=0:
        B2W-=1
        W2B-=1
        total+=1
    result.append(total+B2W+W2B)
for i in result:
    print(i)