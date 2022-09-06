a=int(input())
b=int(input())
a1=0
for i in range(1,a):
    if a%i==0:
        a1+=i
b1=0
for i in range(1,b):
    if b%i==0:
        b1+=i
if a1==b and b1==a:
    print("Amicable")
else:
    print("Not Amicable")