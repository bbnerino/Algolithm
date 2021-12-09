N = int(input())
scores= list(map(int,input().split()))
afterscore = []
result = 0
for score in scores:
    afterscore.append(score/max(scores)*100)

for i in afterscore:
    result+= i


print(result/len(scores))