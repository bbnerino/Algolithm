N = int(input())
ABC = [0 for _ in range(26)] 
# A 는 65 번 Z는 90번 -65 로 
#       0 번~ 25번 까지

for ts in range(N):
    word = input()
    for i in range(len(word)): # ABC에 자리수에 맞춰 추가해주기
        ABC[ord(word[i])-65] += 10 ** (len(word)-1-i)

while 0 in ABC: # 모든 0 제거
    ABC.remove(0)
ABC.sort() # 작은수부터 정렬
total=0 # 결과값
start=9 # 9부터 8 7 .. 작아질 것
while ABC:
    total += start*ABC.pop() # 맨뒤, 가장 큰 값에 start값을 곱해서 더해준다
    start-=1
print(total)