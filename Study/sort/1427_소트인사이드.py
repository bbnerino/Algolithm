N = input()
nums=[[]for _ in range(10)] # 0~9까지 숫자 들어갈 자리를 만들어주고
for i in N: # 한자리씩 nums의 자리로 넣어준다
    num = int(i) 
    nums[num].append(num) 
# [[], [1], [2], [3], [4], [], [], [], [], []]
for i in range(9,-1,-1): # 뒤에서부터 
    while nums[i]: # 리스트가 빌때까지
        print(nums[i].pop(),end="") # 팝으로 출력해준다
    