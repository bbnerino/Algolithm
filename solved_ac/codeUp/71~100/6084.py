h,b,c,s = map(int,input().split())
# 44100 16 2 10
mb = h*b*c*s/8/1024/1024
print(f"{mb:.1f} Mb")