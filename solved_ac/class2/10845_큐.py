
# def Q(what):
#     global Que,result
#     if what[0:4]=="push":
#         Que.append(int(what[5]))
#     elif what=="front":
#         if len(Que)==0:
#             print(-1)
#         else:
#             print(Que[0])
#     elif what=="pop":
#         if len(Que)>0:
#             print(Que.pop(0))
#         else:
#             print(-1)
#     elif what=="size":
#         print(len(Que))

#     elif what=="empty":
#         if len(Que)==0:
#             print(1)
#         else:
#             print(0)
#     elif what =="back":
#         if len(Que)==0:
#             print(-1)
#         else:
#             print(Que[-1])

# Que=[]
# T = int(input())
# for ts in range(T):
#     Q(input())
from sys import stdin

N = int(stdin.readline())
Que = []
for i in range(N) :
    A = stdin.readline().split()

    if A[0] == 'push' : Que.append(A[1])

    elif A[0] == 'pop' : 
        if Que : print(Que.pop(0))
        else : print(-1)

    elif A[0] == 'size' : print(len(Que))

    elif A[0] == 'empty' :
        if len(Que) == 0 : print(1)
        else : print(0)
            
    elif A[0] == 'front' :
        if len(Que) == 0 : print(-1)
        else : print(Que[0])
    
    elif A[0] == 'back' :
        if len(Que) == 0 : print(-1)
        else : print(Que[-1])