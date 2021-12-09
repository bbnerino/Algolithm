N=int(input())
peoples=[]
score=[]
for i in range(N):
    x,y = map(int,input().split())
    peoples.append((x,y))

for i in range(N):
    count=1
    for j in range(N):
        if peoples[i][0] < peoples[j][0] and peoples[i][1]<peoples[j][1]:
            count+=1
    score.append(count)

for i in score:
    print(i,end=" ")
    



    

        

    

