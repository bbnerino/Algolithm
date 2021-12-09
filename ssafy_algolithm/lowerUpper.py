def low_and_up(word):
    word = list(word)
    for i in range(len(word)):
        if i%2 ==1 :
            word[i]= word[i].upper() # 홀수만 받아 대문자로
    for j in word:
        print(j,end="") # [word] 출력하기 
    print() 

low_and_up('apple')
low_and_up('banana')