def solution(id_list, report, k):
    countlist = {}
    answer = [0 for _ in range(len(id_list))]

    for id in id_list:
        countlist[id] = []

    for i in range(len(report)):
        a, b = report[i].split()
        countlist[b].append(a)
        countlist[b] = list(set(countlist[b]))
    for point in countlist:
        if len(countlist[point]) >= k:
            for i in range(len(countlist[point])):
                idx = id_list.index(countlist[point][i])
                answer[idx] += 1

    return answer