triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	


def solution(triangle):

  def find_big_num(index,dpa):  
    triangle_list = triangle[index]
    tmp = []
    for i in range(len(triangle_list)):
      tmp.append(triangle_list[i]+max(dpa[i],dpa[i+1]))
    return tmp


  dpa = triangle[-1]

  for i in range(len(triangle)-2,-1,-1):
    dpa = find_big_num(i,dpa)

  return dpa[0]

print(solution(triangle))

