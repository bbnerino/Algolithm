a,b,c =map(int,input().split())
def son_ik(a,b,c):
    if b<c:
        n = (a//(c-b)) +1
        print(n)
    else:
        print(-1)
son_ik(a,b,c)