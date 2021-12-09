
a=int(input()) # 26

start = a%10 + a//10  # 8
num=0

if num ==0:
    result = a
    result = 10*(result%10)+ (start%10) # 68
    start = result%10 + result//10
    num += 1
while result != a:
    result = 10*(result%10)+ (start%10) # 68
    start = result%10 + result//10
    num += 1
print(num)
