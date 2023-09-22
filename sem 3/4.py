a1,b1=map(int,input().split())
a=a1
b=b1
while a!=0 and b!=0:
    if a>b:
        a=a%b
    elif a<b:
        b=b%a
    else:
        a=0
        b=b
d=a+b
print(a+b)

x=0
y=0
for i in range (-20,20):
    x=i
    y=(d-a1*x)/b1
    print(x,y)

