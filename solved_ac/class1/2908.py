#상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 
# 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 
# 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

a,b = map(int,input().split())
# print(len(str(a))) ====3
def reverse(x):
    sum = 0
    k = len(str(x))
    while x > 0:
        sum += (x%10)*(10**(k-1))
        x //= 10
        k -= 1
    return sum
if reverse(a)> reverse(b)  :
    print(reverse(a))
else    :
    print(reverse(b))
