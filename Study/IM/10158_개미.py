w,h = map(int,input().split())
antx,anty= map(int,input().split())
second = int(input())

# 개미의 길을 나열을 한다고생각
# 4*6 의 길을 계속 나열해보면 쉬울듯
if ((antx+second)//w )%2==0: # 더해서 길이로 나눠주면 다음 값
    x = (antx+second)% w # 짝수일때는 그냥값
else:   # 홀수일때는 거꾸로
    x = w- (antx+second)% w


if ((anty+second)//h )%2==0:
    y = (anty+second)% h
else:
    y = h- (anty+second)% h

print(x,y)