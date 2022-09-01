ageH=0
ageD=0
ageH=float(input("Input a dog's age in human year: "))
if(ageH<3):
    ageD=float(10.5*ageH)
elif(ageH>2):
    ageD=float((ageH-2)*4+21)
else:print("WRONG INPUT!!!")
print("The dog's age in dog's years is ",ageD)
