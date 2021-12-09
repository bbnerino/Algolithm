T=int(input())

def towel(dice,bot):
    if bot == dice[0]:
        top = dice[5]
    elif bot == dice[1]:
        top = dice[3]
    elif bot == dice[2]:
        top = dice[4]
    elif bot == dice[3]:
        top = dice[1]
    elif bot == dice[4]:
        top = dice[2]
    elif bot == dice[5]:
        top = dice[0]
    return top

def cal(dice,bot,top):
    newd = dice[:]
    newd.remove(bot)
    newd.remove(top)
    return max(newd)
    

ev_dice=[]
for ts in range(T):
    ev_dice.append(list(map(int,input().split())))

# [[2, 3, 1, 6, 5, 4], [3, 1, 2, 4, 6, 5], 
# [5, 6, 4, 1, 3, 2], [1, 3, 6, 2, 4, 5], [4, 1, 6, 5, 2, 3]]
result =[]
for six in range(6):#0,1,2,3,4,5
    total=0
    bot = ev_dice[0][six]
    top= 0
    for i in range(T): # 다섯번 반복 할거다.
        top = towel(ev_dice[i],bot)
        total+=cal(ev_dice[i],bot,top)
        bot = top*1
    result.append(total)
print(max(result))