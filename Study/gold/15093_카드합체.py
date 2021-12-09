# def pluscard(m,card):
#     newcard = sorted(card)
#     plus= newcard[0] + newcard[1]
#     newcard[0],newcard[1]= plus,plus
#     if m>1:
#         return pluscard(m-1,newcard)
#     else:
#         return newcard

# n,m = map(int,input().split())
# # 카드 개수 , 카드 합체 횟수
# card= list(map(int,input().split()))

# print(sum(pluscard(m,card)))

n,m = map(int,input().split())

card= list(map(int,input().split()))
total= sum(card)
for i in range(m):
    card= sorted(card)
    total+=card[0]+card[1]
    card[0],card[1] = card[0]+card[1], card[0]+card[1]
print(total)