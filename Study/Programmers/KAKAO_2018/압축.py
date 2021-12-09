

def solution(msg):
    ABC = ['0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    i=0
    answer = []
    while i <len(msg):
        k = 1
        while msg[i:i+k] in ABC :
            if i+k < len(msg) :
                k+=1
            else:
                k+=1
                break

        ABC.append(msg[i:i+k])
        k -=1
        answer.append((ABC.index(msg[i:i+k])))
        i = i+k

    return answer
print(solution('ABABABABABABABAB'))