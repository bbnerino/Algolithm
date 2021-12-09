students = [
[100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]]
 
def sumscore(scores):
    scorelist =[]
    for i in range(len(scores)): # [0] [1] [2]
        sum= 0
        for j in range(len(scores[i])):
            sum+= scores[i][j]
        scorelist.append(sum)
    for score in scorelist:
        print(score)


def ssumscore(scores):
    scorelist =[]
    for i in range(len(scores)): # [0] [1] [2]
        sum= 0
        for j in range(len(scores[i])):
            sum+= scores[j][i]
        scorelist.append(sum)
    for score in scorelist:
        print(score)


sumscore(students)

ssumscore(students)
