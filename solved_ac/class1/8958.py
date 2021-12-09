n= int(input())
good = []
for ox in range(n):
    ox = input()
    result = []

    for i in range(len(ox)):
        if ox[i] == "X" :
            result.append(0)
        elif i>0 and ox[i] == "O" and ox[i-1] == "O" :
            a = int(result[i-1]) +1
            result.append(a)
        else:
            result.append(1)
    score = 0
    
    for j in range(len(result)):
        score += int(result[j])
    good.append(score)
for i in good:
    print(i)
