from collections import deque

N= int(input())
def card(cardlist): 
    while cardlist:
        if len(cardlist)==1:
            print(cardlist[0])
            break
        else:
            cardlist.popleft()
            cardlist.append(cardlist.popleft())
# deque 을 이용해야 시간제한이 안걸린다.
Q= deque(list(range(1,N+1)))
card(Q)
