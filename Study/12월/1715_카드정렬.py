import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
cardlist=[]
for _ in range(N):
    cardlist.append(int(input()))

print(cardlist)