def strawberry(num):
    ddalgi = num[2::].zfill(4)
    result=''
    for i in ddalgi:
        if i == '1':
            result+= '딸기'
        else:
            result+='V'
    return result
    # print(result)

T = int(input())
result =[]
for ts in range(T):
    num = int(input()) 
    num = num%28
    if num == 0:
        num=28
    if num<=15:
        pass
    else:
        num = 30 - num
    print(strawberry(bin(num)))
#     result.append(strawberry(bin(num)))
# for r in result:
#     print(r)

