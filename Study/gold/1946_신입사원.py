import sys
input=sys.stdin.readline
# print=sys.stdout.write

N= int(input())
countlist=[]
for NN in range(N): # 2번
    T= int(input()) # 5번, 7번
    result=[]
    for ts in range(T):
        result.append(list(map(int,input().split())))
    total = len(result)
    # [[3, 2], [1, 4], [4, 1], [2, 3], [5, 5]]
    result.sort(key=lambda x:x[0])  
    # for 문 두번 도는 것보단 sort가 낫다.
    # [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
    worst= result[0][1]
    count=1
    for i in range(1,len(result)):
        if worst > result[i][1]:
            count+=1
            worst= result[i][1]
    countlist.append(count)
for i in countlist:
    print(i)


# 시간초과 ------------------------------
# N= int(input())
# total_result=[]
# for NN in range(N): # 2번
#     T= int(input()) # 5번, 7번
#     result=[]
#     for ts in range(T):
#         result.append(list(map(int,input().split())))
#     total = len(result)
#     # [[3, 2], [1, 4], [4, 1], [2, 3], [5, 5]]

#     for i in range(len(result)):
#         yes = 1
#         for j in range(len(result)):
#             if result[i][0] > result[j][0] and result[i][1] > result[j][1]:
#                 yes=0
#         if yes ==0 : 
#             total -=1
#     total_result.append(total)

# for i in total_result:
#     print(i)

