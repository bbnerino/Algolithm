# N= int(input())
# numbers= list(map(int,input().split()))

# biggerlength=[]
# for i in range(len(numbers)):
#     count=0
#     small=numbers[i]
#     if len(numbers)-i >count:
#         for j in range(i,len(numbers)):
#             if numbers[j]>=small:
#                 small=numbers[j]
#                 count+=1
#             else:
#                 biggerlength.append(count)
#                 break
#     else:
#         break

# for i in range(len(numbers)):
#     count=0
#     big = numbers[i]
#     if len(numbers)-i > count:
#         for j in range(i,len(numbers)):
#             if numbers[j]<=big :
#                 big =numbers[j]
#                 count+=1
#             else:
#                 biggerlength.append(count)
#                 break 
#     else:
#         break
# print(max(biggerlength))

N= int(input())
numbers= list(map(int,input().split()))
# emptylist=[0]*(N-1)
emptylist=""
for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        # emptylist[i] = 1
        emptylist+="u"
    elif numbers[i]== numbers[i+1]:
        # emptylist[i] = 0
        emptylist+="s"
    else:
        # emptylist[i] = -1
        emptylist+="d"

# [-1, 1, 0, -1, 0, 1, -1, 1]
# ususuusd
long=[]
long.append(emptylist.split("d"))
long.append(emptylist.split("u"))
print(long)
verylong=0
for i in long[0]:
    if len(i)> verylong:
        verylong=len(i)
for i in long[1]:
    if len(i)> verylong:
        verylong=len(i)
print(verylong+1)