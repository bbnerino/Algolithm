import sys
sys.stdin = open('input.txt')

sentence = list(input())
s = 0
start= 0
while s < len(sentence): # 문자열 끝까지 하나씩 확인하는데
                        # 무슨 경우든 한자리씩은 이동한다.
    if sentence[s] =="<":   # 만약 괄호 시작이면
        s+=1
        while sentence[s]!=">": # 닫히는게 아닐때 진행되게한다.
            s+=1                # => 닫히는게 나올때까지
        s+=1                    # 만일 닫혔다면 한자리 이동

    elif sentence[s].isalnum() : # isalnum() =
                                 # 문자열이 숫자 영어 한글로 되어있으면 true
        start = s                # 문자열이 시작이 된다면 첫 값을 저장하기
        while s< len(sentence) and  sentence[s].isalnum(): # 끝나던지 띄워쓰기 나올떄까지
            s +=1
        new = sentence[start:s] # 범위지정해주고
        new.reverse()           # reverse = 거꾸로 만드는 함수
        sentence[start:s] = new # 원래 자리에 new 넣어주기

    else: # 공백이면
        s+=1
print("".join(sentence))        # 리스트를 빈칸없이 출력되게만들기



