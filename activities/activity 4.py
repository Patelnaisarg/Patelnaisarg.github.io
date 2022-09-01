x=0
y=0
a=0
b=0

x,y = input("Enter two integers:").split(",")
a=float(x)
b=float(y)
if a%2==0 or a%3==0:
    if b%2==0 or b%3==0:
        ans=a*b
else:ans=a+b
print("Divisible By 2 or 3(%d,%d)->%d" %(a,b,ans))
