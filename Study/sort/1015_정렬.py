N = int(input())
nums = list(map(int,input().split()))
newnums=[]
for i in range(N):
    newnums.append([i,nums[i]])
# [[0, 2], [1, 3], [2, 1]]

sortnums = sorted(newnums,key=lambda x:(x[1]))
# 번호랑 순서랑 같이 저장하면 , 중복값도 사용가능
result=[]
for i in newnums:
    result.append(sortnums.index(i))
print(*result)



