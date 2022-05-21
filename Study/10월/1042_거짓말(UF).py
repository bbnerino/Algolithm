import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x]= find(parent[x])
        return parent[x]

def union(x,y):
    a = find(x)
    b = find(y)
    if a<b:
        parent[b]=a
    elif a>b:
        parent[a]=b

N,M = map(int,input().split())
knowPeople = list(map(int,input().split()))[1::]    # 아는 사람들
parent=list(range(N+1))

for i in range(1,len(knowPeople)):
    parent[knowPeople[i]]= knowPeople[0]
if knowPeople:
    king = knowPeople[0]
else:
    king = 0

count = M
partylist =[]
for _ in range(M):
    party = list(map(int,input().split()))[1::]
    partylist.append(sorted(party))

while True:
    check_all = True
    for party in partylist:
        flag = False
        for i in range(len(party)):
            if parent[party[i]] ==king:
                flag=True
                check_all=False
                for j in range(1,len(party)):
                    union(party[0],party[j])
                king = parent[party[0]]

        if flag==False:
            pass
        elif flag==True:
            partylist.remove(party)
            count-=1

    if check_all:
        break

print(count)
