N,M = map(int,input().split())

listen = []
saw = []
for n in range(N):
    listen.append(input())
for m in range(M):
    saw.append(input())

same  = list(set(listen) & set(saw))

# 교집합을 구하려면 , set로 바꿔서 &을 사용하면 쉽게 구하기 가능! 
same.sort()
print(len(same))
for i in range(len(same)):
    print(same[i])

