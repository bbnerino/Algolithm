import sys
sys.stdin =open('input.txt')

N,r,c = map(int,input().split())


count =0
while N >=1:
    original = (2**N)**2        # 총 숫자 개수
    half = (2**N)//2 # 4        # 8칸 중 절반

    if r< half and c< half:     # 북서
        pass                    # 자기자신 +0

    elif r< half and c>=half: # 북동
        count+= original//4     # orign//4 인 16을 더해준다
        c -= half

    elif r >= half and c<half:  # 남서
        count += 2 * original // 4   # 32를 더해준다
        r -= half

    elif r >= half and c>=half: # 동남
        count += 3 * original // 4  #

        r -= half
        c -= half
    N-=1



print(count)