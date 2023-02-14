import sys
sys.stdin = open("./2023/2월/input.txt")
import heapq
input = sys.stdin.readline

T = int(input())
dict = {}
result = 0


for _ in range(T):
  input_list = list(input().split())
  TYPE,PERSON,COUNT = input_list[0],input_list[1],int(input_list[2])
  
  input_list = input_list[3:]

  if TYPE=="1":
    tmp = []
    if PERSON in dict.keys():
      tmp = dict[PERSON]
      
    for item in input_list:
      heapq.heappush(tmp,int(item)*-1)
    dict[PERSON] = tmp  
  elif TYPE=="2":
    for _ in range(COUNT):
      try:
        result += heapq.heappop(dict[PERSON])*-1
      except:
        # pass ... 와씨 ......
        break
        

print(result)
