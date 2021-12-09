garo,sero =map(int,input().split())
storenum =int(input())
store =[]
for _ in range(storenum+1):
    way, length = map(int,input().split())
    x=0
    y=0
    if way==1:
        x= length
        y= 0
    elif way ==2:
        x = length
        y = sero
    elif way ==3:
        y = length
        x = 0
    elif way ==4:
        x = garo
        y = length
    store.append([y,x])
# [[0, 4], [2, 0], [5, 8]]
me =store.pop()
# [5,3]
total=[]
for i in range(len(store)):
    short=100
    if me[0]==store[i][0] or me[1]==store[i][1]:
        short= abs(me[0]-store[i][0]) + abs(me[1]-store[i][1])
    elif me[1]!=garo and store[i][1]==0:
        short= me[1]+ me[0]-store[i][0]
    else:
        for time in range(2):
            if time==0:
                clock = me[0]+me[1]+store[i][0]+ store[i][1]
            elif time==1:
                nonclock = (garo-me[1]) + (garo-store[i][1]) + me[0] + store[i][0]
        short = min(clock,nonclock)
    total.append(short)           
            
print(sum(total))


