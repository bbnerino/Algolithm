nums_switch = int(input())
switch = list(map(int, input().split()))
nums_students = int(input())


def boy(card):
    todo = []
    for i in range(1, nums_switch + 1):
        if i % card == 0:
            todo.append(i - 1)
            # [2, 5]
    for i in todo:
        if switch[i] == 1:
            switch[i] = 0
        else:
            switch[i] = 1


def girl(card):
    idx = card - 1
    todo = [idx]
    i = 1
    if len(switch)>2:
        while i <= idx < nums_switch - i:
            if switch[idx - i] == switch[idx + i]:
                todo.append(idx - i)
                todo.append(idx + i)
                i += 1
            else:
                break

        for j in todo:
            if switch[j] == 1:
                switch[j] = 0
            else:
                switch[j] = 1


for ts in range(nums_students):
    ses, card = map(int, input().split())
    # 남자 1 여자 2
    if ses == 1:
        boy(card)
    else:
        girl(card)

for i in range(0,len(switch),20):
    print(*switch[i:i+20])