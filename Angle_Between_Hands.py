h,m=map(int,input().split(":"))
angle=((30*h)-(11/2*m))
if angle<0:
    angle=angle*-1
t=angle
k=abs(t-360)
if t<k:
    print(t)
else:
    print(k)