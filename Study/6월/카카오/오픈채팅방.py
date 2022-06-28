record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# 닉네임 변경 => 나갔다 들어오기 / 닉네임 변경하기
# 기존에 출력된 메시지의 닉네임도 변경하기

def solution(record):
    answer = []
    realanswer = []
    people = {}
    while record:
        tmp = record.pop(0).split()
        if len(tmp)==2:
            [func,id] = tmp
        elif len(tmp):
            [func,id,name] = tmp
            people[id] = name
        if func =='Enter':
            answer.append(['Enter',id])
        if func == 'Leave':
            answer.append(['Leave',id])
    for i in range(len(answer)):
        func,id = answer[i]
        if func == 'Enter':
            realanswer.append("{}님이 들어왔습니다.".format(people[id]))
        if func == 'Leave':
            realanswer.append("{}님이 나갔습니다.".format(people[id]))
    return realanswer

print(solution(record))