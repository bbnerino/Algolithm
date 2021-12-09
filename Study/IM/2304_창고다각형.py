N= int(input())

point=[]
for ts in range(N):
    w,h = map(int,input().split())
    point.append([w,h])
point.sort(key=lambda x:(x[0]))
# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

small = point[0][1] # 4
stack = [point[0]]
area = 0

for i in range(len(point)):
    if point[i][1] > small:
        area += (point[i][0]-stack.pop()[0])*small
        small = point[i][1]
        stack.append(point[i])
# 최대값 전까지
big=stack.pop() # 8 10 

reverse = point[::-1]
stack.append(reverse[0])
small = reverse[0][1]

for i in range(len(reverse)):
    if reverse[i][1] > small:
        area += (stack.pop()[0]-reverse[i][0])*small
        small = reverse[i][1]
        stack.append(reverse[i])
top=[]
for i in range(len(point)):
    if point[i][1] == big[1]:
        top.append(point[i][0])
if len(top)>1:
    area+=(top[-1]-top[0]+1)*big[1]
else:
    area+= big[1]
print(area)