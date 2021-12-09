bingo=[]
for i in range(5):
    bingo.append(list(map(int,input().split())))
check =[[0]*5 for _ in range(5)]
# 체크판을 만들어 놓음

numls=[] # 입력받기
for i in range(5):
    numls.append(list(map(int,input().split())))
ls=[] # 입력받은거 한줄로 만들기
for nums in range(5):
    for n in range(5):
        ls.append(numls[nums][n])
# ls
#[5, 10, 7, 16, 2, 4, 22, 8, 17, ...]

def BB(ls):
    global bingocount
    count=0
    bingocount=[]
    garo=["a","b","c","d","e"]
    for num in ls:
        for i in range(5):
            for j in range(5):
                if bingo[i][j]==num:
                    # 값을 찾으면 count 늘리고
                    count+=1
                    check[i][j]=1 # 체크를 해준다
                
                if sum(check[i])==5 and garo[i] not in bingocount:
                    bingocount.append(garo[i])
                
                for i2 in range(5):
                    sum2=0
                    for j2 in range(5):
                        sum2+=check[j2][i2]
                        if sum2==5 and i2 not in bingocount:
                            bingocount.append(i2)

                # 대각선들 찾기
                cross=0
                reverse=0
                for c in range(5):
                        cross+=check[c][c]
                        reverse+= check[c][4-c]
                if cross == 5 and "cross" not in bingocount:
                    bingocount.append("cross")
                if reverse == 5 and "reverse" not in bingocount:
                    bingocount.append("reverse")

                if len(bingocount)>=3:
                    print(count)
                    return 
BB(ls)
