met=0
hr=0
min=0
sec=0
km=0
mil=0
met=float(input("Input distance (meters):"))
hr=float(input("Input time (hour):"))
min=float(input("Input time(minutes):"))
sec=float(input("Input time(seconds):"))

hour=hr+(min/60)+(sec/3600)
sec=hour*3600

km=met/1000 #conversion meter into km
mil=km/1.609

speedkm=km/hour
speedm=mil/hour
speedme=met/sec

print("your speed in meters/sec is ",speedme)
print("Your speed in km/h is ",speedkm)
print("Your speed in miles/h is ",speedm)