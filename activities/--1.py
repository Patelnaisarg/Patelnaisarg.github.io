print("hello world")
num1=float(input("enter the first number"))
opp=input("enter the operation for arithmetic calculatio==>+,-,*,/")
num2=float(input("enter the second number"))
result=0
if(opp=='+'):
  result=num1+num2
elif(opp=='-'):
  result=num1-num2
elif(opp=='*'):
   result=num1*num2
elif(opp=='/'):
 result=num1/num2
else:print("wrong input!!")

print("your answer ==>",result)