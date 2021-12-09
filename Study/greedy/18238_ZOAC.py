ENG="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #0~25
zoac= input()
#ZOAC
num_zoac=[]

for i in zoac:
    num_zoac.append( ENG.index(i))
    #[25, 14, 0, 2] 숫자로 바꿔줌
front =0
total=0
for i in range(len(num_zoac)):
    move= abs(front -num_zoac[i]) # 앞자리에서 뺀 값의 절대값
    if move>=13:
        move = 26- move # 13보다 크다면 반대쪽으로 돌린다.
    front =num_zoac[i] # 앞자리를 지금값으로 바꾼다
    total+=move # 토탈 +
print(total)
