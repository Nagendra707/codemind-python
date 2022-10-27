def fun(n):
    t=n**0.5
    if(n%t==0):
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if fun(i):
        s+=i
print(s)