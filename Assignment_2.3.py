"""2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data."""


def computepay(h,r):
    if h < 0 or r < 0:
        return None
    elif h > 40:
        return (40*r+(h-40)*1.5*r)
    else:
        return (h*r)
    
try:
    hrs = raw_input("Enter Hours:")
    hour = float(hrs)
    r = raw_input("please input your rate:")
    rate = float(r)
    p = computepay(hour,rate)
    print (p)
except:
    print ("Please,input your numberic")
