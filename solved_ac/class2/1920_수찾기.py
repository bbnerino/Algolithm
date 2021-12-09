N = int(input())
numlist = sorted(list(map(int, input().split())))
M = int(input())
findlist = list(map(int, input().split()))

def binary(start,end):
    if start>end:
        return 0
    m = (start+end)//2
    if i == numlist[m]:
        return 1
    elif i < numlist[m]:
        return binary(start,m-1)
    elif i > numlist[m]:
        return binary(m+1,end)

for i in findlist:
    start=0
    end = N-1
    print(binary(start,end))

    # result = []
# for i in range(M):

#     start = numlist[0]
#     end = numlist[-1]
#     index = findlist[i]
#     s = 0
#     e = N - 1
#     if start <= index <= end:
#         center = round(N / 2)

#         while True:
#             if index == numlist[center]:
#                 result.append(1)
#                 break
#             elif index > numlist[center]:
#                 s = center
#                 center = round((s + e) / 2)
#             elif index < numlist[center]:
#                 e = center
#                 center = round((s + e) / 2)
#             if s>e:
#                 result.append(0)
#     else:
#         result.append(0)
# for i in result:
#     print(i)