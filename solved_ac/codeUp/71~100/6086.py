a = int(input())
sum = 0
i = 1
while sum < a:
    sum += i
    i += 1
    if sum>=a:
        print(sum)