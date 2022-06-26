s = "abcabcabcabcdededededede"


def solution(s):
    answer = 1000000

    def divide(n):
        words = []
        TF = True
        for i in range(0, len(s), n):
            words.append(s[i:i + n])
        for w in words:
            if len(w) != n:
                TF = False
                break
        return [TF, words]

    def stringfy(words):
        result = ''
        tmp = words[0]
        cnt = 0
        for w in words:
            if tmp == w:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt) + tmp
                elif cnt == 1:
                    result += tmp
                tmp = w
                cnt = 1
        if cnt > 1:
            result += str(cnt) + tmp
        elif cnt == 1:
            result += tmp
        return result

    for i in range(1,len(s)+1):
        TF,words = divide(i)
        if TF:
            answer = min(answer,len(stringfy(words)))
    return answer
print(solution(s))

