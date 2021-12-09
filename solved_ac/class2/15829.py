l=int(input())
eng_list=[]
eng=input()
for i in eng:
    eng_list.append(ord(i)-96)
result=0
up=0
for i in eng_list:
    result+=i*(31**up)
    up+=1
print(result%1234567891)
