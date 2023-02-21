import sys
sys.stdin = open("./2023/2월/input.txt")

T=int(input())

for _ in range(T):
  N = int(input())
  X의부모 = [0 for _ in range(N+1)]
  for _ in range(N-1):
    s,e = map(int,input().split())
    X의부모[e] = s
  
  A,B = map(int,input().split())
  A의부모들 = [A]
  B의부모들 = [B]

  # 16 => 10 => 4 => 8 
  아이 = A
  while X의부모[아이]>0:
    A의부모들.append(X의부모[아이])
    아이 = X의부모[아이]
  
  아이 = B
  # 7 => 6 => 4 => 8
  while X의부모[아이]>0:
    B의부모들.append(X의부모[아이])
    아이 = X의부모[아이]
  
  # [16,10,4,8]
  # [7,6,4,8]
  # 8부터 함께 노드가 내려가는데 4까지 동일하다 
  # 공통 조상 => 4,8 가까운것은 4

  result = -1
  try :
    while A의부모들[result] == B의부모들[result]:
      result-=1
  except:
    pass
  print(A의부모들[result+1])

  
