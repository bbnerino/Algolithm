

# def square(graph):
#     global zero_count,one_count
#     for i in range(N):
#         for j in range(N):

#             if graph[i][j]==0:
#                 zero_count += 1
#                 x = 1
#                 while i<N-1 and j<N-1: 
#                     if graph[i+1][j+1]==0:
#                         x+=1
#                         i+=1
#                         j+=1
#                     else:
#                         break

#                 for p in range(i-x+1,i+1):
#                     for q in range(j-x+1,j+1):
#                         graph[p][q]=2
#                         graph[q][p]=2

#             if graph[i][j]==1:
#                 one_count += 1
#                 x = 1
#                 while i<N-1 and j<N-1: 
#                     if graph[i+1][j+1]==1:
#                         x+=1
#                         i+=1
#                         j+=1
#                     else:
#                         break
#                 for p in range(i-x+1,i+1):
#                     for q in range(j-x+1,j+1):
#                         graph[p][q]=2
#                         graph[q][p]=2

#     return [zero_count,one_count]

# zero_count=0
# one_count=0
# N= int(input())
# graph=[]
# for _ in range(N):
#     graph.append(list(map(int,input().split())))
# print(square(graph))
