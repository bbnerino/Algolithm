import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

N = int(input())
cardlist=[]

for _ in range(N):
    cardlist.append(int(input()))
cardlist = sorted(cardlist)     # 입력 받고 정렬 한번 한다.
count =0


while cardlist:         # cardlist가 빌때까지!
    try:    # heapqpop으로 뽑으면 가장 작은 값 두개가 뽑아진다.
        mix = heapq.heappop(cardlist)+heapq.heappop(cardlist)
        count += mix
            # 가장 얇은 카드 뭉치의 합은 묶여서 다시 넣어진다.
        heapq.heappush(cardlist,mix)

    except: # 두개가 못뽑아진다 == 한개 남았을 때는 끝난 거라서 출력하면서 끝
        print(count)



