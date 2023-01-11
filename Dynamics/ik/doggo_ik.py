import math
import serial
import time

# arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1)
# def write(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
   
# Looking from back, BL_abovelink=90+x, BR_abovelink=90-x
#                    BL_below_link=90+x, BR_below_link=90-x




while True:
    x=float(input("Enter the x : "))
    y=float(input("Enter the y : "))
    i=0
    while i<5:
       
        a1,a2=55,50
        a1,a2=80,92
        

        D1= (a1**2 - a2**2 + x**2 + y**2)/(2*a1*math.hypot(x,y))
        # theta1=math.atan2(y,x) - math.acos((a1**2 - a2**2 + x**2 + y**2)/(2*a1*math.hypot(x,y))) + math.pi/2 

        theta1= math.atan2(y,x) +math.atan2(math.sqrt(1-D1*D1), D1) + math.pi/2

        D2 = (-x**2 - y**2+a1**2 +a2**2)/(2*a1*a2)
        theta2=math.atan2(math.sqrt(1-D2*D2), D2)

        theta2=180*theta2/math.pi 
        theta1=theta1*180/math.pi 

        theta1=round(90-theta1)

        if theta1>=90:
            theta2=round(180-theta2)
        else:
            theta2=round(theta2)

        # theta1=90-theta1-10  # for Left legs
        # theta2=180-theta2 # for Left legs
        

        # theta1=90+theta1+10  # for right legs
        # theta2=theta2 # for right legs
     
        send=f"{theta1},{theta2}"
        print(theta1, theta2)
        # write(send)
        i+=1







