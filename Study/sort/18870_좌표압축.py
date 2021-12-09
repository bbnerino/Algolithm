N = int(input())
nums = list(map(int,input().split()))

newnums = sorted(list(set(nums)))
# 중복을 제거해준다

dic ={}
for i in range(len(newnums)):
    dic[newnums[i]]= i
# {-10: 0, -9: 1, 2: 2, 4: 3}
for i in nums:
    print(dic[i],end=' ')






# numlist = []
# for i in range(len(nums)):
#     numlist.append([i,nums[i]]) # 순서와 번호를 넣는다
# numlist.sort(key=lambda x:x[1])
#
#
# k=0
# new = []
# while numlist:
#     s = numlist.pop(0)
#     flag=0
#     for n in new:
#         if s[1] == n[1]:
#             flag=1
#             break
#     if flag==0:
#         new.append([s[0],s[1],k])
#         k+=1
#     else:
#         new.append([s[0],s[1],n[2]])
#
# new.sort(key=lambda x:x[0])
#
# for i in range(len(new)):
#     print(new[i][2],end=' ')