import sys
sys.stdin = open('input.txt')
from itertools import combinations

L,C = map(int,input().split())
word = list(map(str,input().split()))
coll = list(map(list,combinations(word,L))) # 조합을 써서 6개중 4개를 중복없이 뽑기 6*5*4*3/4*3*2*1 = 15개

for c in coll:      # 하나씩 확인
    check = False   # 모음이 있는지 확인
    count = 0       # 자음 개수 확인용

    for mo in 'aeiou':      # a e i o u 가
        if mo in c:         # c안에 있다면
            check=True      # 모음 체크 확인
            count+=1        # 모음 개수를 늘린다

    if check==True:     # 모음이 있다면?
        if L-count>=2:  # 전체개수 - 모음 개수 = 자음 개수
            c.sort()    # *** sorted 함수는 저장이 안된다  
            continue

                   # 모음이 없거나 자음이 2개 보다 적다면
    c.clear()       # c= [] 빈리스트로 만든다

coll.sort()             # 순서대로 정렬

for c in coll:
    if c:                       # 빈값이 아니라면
        for i in range(L):      # 각자리를
            print(c[i],end='')  # 출력한다.
        print()

