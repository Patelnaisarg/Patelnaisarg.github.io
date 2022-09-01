mon=input("Input the name of Month:")
if mon in['january','march','may','july','august','october','december']:
    print("No. of days:31 days")
elif mon in["april","june","septembetr","november"]:
    print("No. of days: 30 days")
elif mon in['february']:
    print("no. of days: 28/29 days")
else:
    print("Wrong input!!!")