N= int(input())
count=0

for j in range(1,N+1):
    if 0<j<10:
        count+=1
    if 10<=j<100:
        count+=1
    if 100<= j <1000: 
        hun= j//100
        ten= (j-(j//100)*100)//10
        one= j%10
        if hun-ten == ten-one :
            count +=1
print(count)

