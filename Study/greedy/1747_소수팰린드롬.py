N = int(input())
numlist = [0] * 1004000 # 수정
sosu =[]

# 에라토스뭐시기의 체 
for i in range(2,len(numlist)): # 2부터 시작해야함!
    if numlist[i] == 0:
        sosu.append(i)
        for j in range(i,len(numlist),i):
            numlist[j]=1
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
#  89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

def pallin(num):
    num = str(num)
    if len(num)<=1:
        result = True
        return result
    else:
        if num[0]==num[-1]:
            return pallin(num[1:-1])
        else:
            result = False
            return result

for so in sosu:
    if so >= N and pallin(so):
        print(so)
        break





