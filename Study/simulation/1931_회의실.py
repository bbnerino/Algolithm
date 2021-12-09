N = int(input())
every = []
big = 0
for _ in range(N):
    s, e = map(int, input().split())
    every.append([s, e])
    big = max(e, big)

# every.sort(key=lambda x: x[0])
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
every.sort(key=lambda x: (x[1], x[0]))

index = every[0][1]
count = 1
which = 1
while index<=big:
    is_in=False
    for i in range(which,len(every)):
        if every[i][0]>= index:
            which = i+1
            index = every[i][1]
            count+=1
            is_in =True
            break
        
    if is_in==False:
        break

print(count)
    



    