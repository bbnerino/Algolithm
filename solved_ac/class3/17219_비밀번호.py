N,M = map(int,input().split())
site ={}
for i in range(N):
    adress,password = input().split()
    site[adress]=password # 딕셔너리 사용법!

result =[]
for i in range(M):
    wannafind=input()
    result.append(site[wannafind])
for i in result:
    print(i)
