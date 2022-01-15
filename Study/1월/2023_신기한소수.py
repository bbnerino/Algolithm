import sys
sys.stdin = open('input.txt')

N = int(input())

nums =[1,2,3,5,7,9] # 마지막 수가 짝수이면 소수가 아니니 빼주는데
                    # 2는 첫자리로는 가능합니다.
def dfs(strnum):
    if len(strnum)==N:      # N자리 숫자면
        print(strnum)  # 출력을 해줍니다.
        return          # 함수 끝

    for n in nums:             # 1,2,3,5,7,9 들을
        newnum = strnum + str(n) # 하나씩 뒷자리로 넣어봅니다.
        if sosu(int(newnum)):   # 이숫자가 소수인지 판단해봅니다.
            dfs(newnum)         # 소수이면 dfs로 들어갑니다.


def sosu(num):  # 소수 판단하기
    if (num==1): # 1은 소수가 아닙니다
        return False
    for i in range(2, int(num**0.5) +1):    #2부터 num의 제곱근까지
        if num%i ==0:       #  하나씩 나눠보다가 나눠지는 값이 있으면
            return False    # 소수가 아닌것
    return True             # 다 통과하면 소수
dfs("")

