info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


def solution(info, query):
    applicants = []
    for inf in info:
        tmp ={}
        lan, field, career , food, rank = inf.split()
        tmp['rank'] = int(rank)
        tmp['lan'] = lan
        tmp['field'] = field
        tmp['career'] = career
        tmp['food'] = food
        applicants.append(tmp)

    applicants =  sorted(applicants,key=lambda x:(-x['rank']))
    maxi= applicants[0]['rank']
    # 정렬하기 (내림차순)

    answer = []
    for inf in query:
        lan, field, career , food_rank = inf.split(" and ")
        food , rank = food_rank.split()
        checklist = []
        if lan != "-":
            checklist.append(['lan',lan])
        if field != "-":
            checklist.append(['field',field])
        if career != "-":
            checklist.append(['career',career])
        if food  != "-":
            checklist.append(['food',food])

        if int(rank) > maxi:
            answer.append(0)
            continue
        count = 0
        for applicant in applicants :
            if applicant['rank'] < int(rank):
                break
            flag= True
            for check in checklist :
                if applicant[check[0]] != check[1]:
                    flag=False
                    continue
            if flag:
                count+=1
        answer.append(count)
    return answer

print(solution(info,query))