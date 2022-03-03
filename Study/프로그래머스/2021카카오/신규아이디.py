
new_id = "z-+.^."


def solution(new_id):
    # 1번
    answer = new_id.lower()
    # 2번
    tmp =''
    for i in answer:
        if i.isdigit() or i.isalpha() or i=="." or i=="-" or i=="_":
                tmp+=i
    answer= tmp

    # 3번
    while True:
        if ".." in answer:
            answer=answer.replace("..",".")
        else:
            break

    # 4번
    if len(answer)>1:
        while True:
            if answer[0] == ".":
                answer = answer[1::]
            if answer[-1]==".":
                answer = answer[:-1]
            break
    else:
        if answer[0] == ".":
            answer = ""


    # 5번
    if answer=="":
        answer="a"
    # 6번
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1]==".":
            answer = answer[:14]
    # 7번
    while len(answer)<3:
        answer = answer + answer[-1]
    return answer

print(solution(new_id))