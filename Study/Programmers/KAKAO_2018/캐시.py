import sys
sys.stdin = open('input.txt')

def solution(cacheSize, cities):
    answer = 0
    newlist = []
    while cities:
        plus = (cities.pop(0)).lower()
        if plus in newlist:
            answer+=1
            newlist.remove(plus)
            newlist.append(plus)
        else:
            answer+=5
            newlist.append(plus)

        if len(newlist)>cacheSize:
            newlist.pop(0)

    return answer


cacheSize = 5
cities =["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# print(cacheSize)
# print(cities)
print(solution(cacheSize,cities))