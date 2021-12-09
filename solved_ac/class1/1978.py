n = int(input())
nums =list(map(int,input().split()))

def sosu(nums):
    if 1 in nums:
        nums.remove(1)
    for num in nums:
        for j in range(2,num):
            if num%j ==0:
                nums.remove(num)
                if num not in nums:
                    return sosu(nums)
    return len(nums)

        
print(sosu(nums))   
        


        