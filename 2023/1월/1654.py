import sys
sys.stdin = open("./2023/1월/input.txt")

# K 이미 갖고있는 개수 / N 필요한 랜선 개수 


# ##### 1차 시도 
# biggest_number = biggest_number =sum(ropeList)//N 
# while True:
#   result = 0
#   for rope in ropeList:
#     result += rope//biggest_number
#   if result == N:
#     print(biggest_number)
#     break
#   biggest_number-=1

## 이분탐색을 이용하자 

K,N = map(int,input().split())
ropeList = []
for i in range(K):
  ropeList.append(int(input()))

start = 1
end = max(ropeList)

def midNumber():
  return (start+end)//2

def get_sum_rope():
  result = 0
  for rope in ropeList:
    result += rope//mid
  return result

while start<=end:
  mid = midNumber()
  ropes = get_sum_rope()
  if ropes >= N:
    start = mid+1
  elif ropes< N:
    end = mid-1

print(end)
  
  

  



