x,y,w,h = map(int,input().split())
result=[x,y,w-x,h-y]
print(min(result))