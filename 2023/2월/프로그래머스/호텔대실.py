book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
import heapq
def solution(book_time):
  Q = []
  answer = 0
  for [s,e] in book_time:
    end_time = int(e.split(":")[0]+e.split(":")[1])*-1
    start_time = int(s.split(":")[0]+s.split(":")[1])*-1
    heapq.heappush(Q,[end_time,start_time])
  result = [-10000]
  while Q:
    s,e = heapq.heappop(Q)
    if len(result)==0:
      result.append(e)
    else:
      flag= False
      for i in range(len(result)):
        if result[i]-10 <= s:
          result[i]=e
          flag = True
      if not flag:
        heapq.heappush(result,e)
        
  answer = len(result)
  return answer

print(solution(book_time))

# 1520-1420
# 1700-1500
# 1820-1640
# 1920-1410
# 2120-1820