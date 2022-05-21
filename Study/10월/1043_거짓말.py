import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
knowPeople = list(map(int,input().split()))[1::]    # 아는 사람들

count = M                                           # 시작 count = M
partylist =[]                                       # 모든 파티리스트

for _ in range(M):
    party = list(map(int,input().split()))[1::]

    flag=0                                          # flag ?
                                            # -> 파티리스트에 추가할지 말지

    for i in party:                         # 파티간사람들 하나하나 확인
        if i in knowPeople:                 # 그 사람이 아는 사람들 중에 있다면?
            knowPeople.extend(party)        # 아는사람에 추가해준다
            flag=1                          # flag=1로 전체 파티리스트에 추가해준다
            count-=1                        # 전체 count-1
            break                           # i - 한명이라도 아는 사람이라면 더 돌 필요X

    if flag==0:                             # 그 파티에 진실을 아는사람이 없다면
        partylist.append(party)             # 파티리스트에 추가해준다


                                            # 파티리스트를 계속 돌려서
                                            # 모든 파티리스트에 아는사람이 없을때까지 돌린다

allCheck=False                                 # 전부 다 돌 경우 1
while allCheck == False:                          # 전부 안돌았을 경우 반복하겠다

    allCheck=True                                  # 전체를 다 돌았는데
    for party in partylist:                 # 파티하나하나 확인
        for i in party:                     # 파티원중에 진실을 아는사람이 있다면?
            if i in knowPeople:
                knowPeople.extend(party)    # 아는사람에 그사람들 추가
                partylist.remove(party)     # 파티리스트에서 제거
                count-=1                    # count-1
                allCheck=False              # 전체를 다 돌지 않았다로 체크
                break                       #
print(count)


