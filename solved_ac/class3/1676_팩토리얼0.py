N = int(input())
total =1
for i in range(1,N+1):
    total*=i # 팩토리얼 구하기
total = str(total) # 문자열로 바꿔서

count =0
i = len(total)-1 
while True: # 맨뒤에서부터 0개수 세기
    if total[i]=='0':
        count+=1
        i-=1
    else:
        break
print(count)