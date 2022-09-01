print("*********************************")
print("TEMPERATURE CONVERSION PROGRAM")
print("*********************************")
a=0
cel=0
fer=0

print("Enter 1. For Celsius to Fahrenheit")
print("Enter 2. For Fahrenheit to Celsius")
print("Enter 3 to Quit: 2")
a=float(input(""))

if a==1:
    cel=float(input("Enter Celsius Temperature:"))
    fer=(cel*1.8)+32
    print("%f Celsius is equivalent to “%f” Fahrenheit"%(cel,fer))
elif a==2:
    fer=float(input("Enter Fahrenheit Temperature:"))
    cel=(fer-32)/1.8
    print("%f Fahrenheit is equivalent to “%f” Celsius" %(fer,cel))
else:print("you enter 3 good bye")
