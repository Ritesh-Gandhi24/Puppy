import math
import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)
def write(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
   
# while True:
#     num = input("Enter a number: ") # Taking input from user
#     value = write_read(num)
#     print(value) # printing the value

# cord=input()


# a1,a2=55,50
# x,y=float(cord.split(',')[0]), float(cord.split(',')[1])
# x=abs(111.921-abs(x))
# y=-(abs(y) - 2 + 11.667)

while True:
    a1,a2=80,92.27
    x,y= 10, -115

    pos_offset_theta1= 0
    pos_offset_theta2=0.87
    theta1=math.atan2(y,x) - math.acos((a1**2 - a2**2 + x**2 + y**2)/(2*a1*math.hypot(x,y))) + math.pi/2 - pos_offset_theta1
    theta2=math.acos((x**2 + y**2-a1**2 -a2**2)/(2*a1*a2)) - pos_offset_theta2 - theta1

    theta2=180*theta2/math.pi
    theta1=theta1*180/math.pi
    # if theta1>0:
    #     theta1=theta1+90
    
    # if theta2>0:
    #     theta2=theta2+90;

    # if theta1<0:
    #     print("THETA1         ",theta1)
    #     theta1=90+theta1
    # if theta2<0:
    #     print(theta2)
    #     theta2=90+theta2
    send=f"{round(theta1)},{round(theta2)}"
    print(theta1, theta2)
    write(send)
