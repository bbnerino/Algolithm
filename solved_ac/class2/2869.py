a,b,v =map(int,input().split())
# a-b 하루에 올라가는거 
# v-b 거리
if ((v-b)%(a-b))==0: 
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)