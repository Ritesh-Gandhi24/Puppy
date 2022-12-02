from turtle import color
import serial
import time
import numpy
import matplotlib.pyplot as plt


# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM4', 9800, timeout=1)
time.sleep(2)
bl = plt.Circle((0.5,0.5), 0.5, color='red')
fl = plt.Circle((0.5,2.5), 0.5, color='red')
br = plt.Circle((2.5,0.5), 0.5, color='red')
fr = plt.Circle((2.5,2.5), 0.5, color='red')
plt.show()


while(1):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        stripped_string = string.strip()
        values = list(stripped_string)
        if(values[0]=='h'):
            fl = plt.Circle((0.5,2.5), 0.5, color='green')
        else:
             fl = plt.Circle((0.5,2.5), 0.5, color='red')

        if(values[1]=='h'):
            fr = plt.Circle((2.5,2.5), 0.5, color='green')
        else:
            fr = plt.Circle((2.5,2.5), 0.5, color='red')
        
        if(values[2]=='h'):
            bl = plt.Circle((0.5,0.5), 0.5, color='green')
        else:
             bl = plt.Circle((0.5,0.5), 0.5, color='red')

        if(values[3]=='h'):
            br = plt.Circle((2.5,0.5), 0.5, color='green')
        else:
            br = plt.Circle((2.5,0.5), 0.5, color='red')

        plt.show()
        plt.pause(0.05)
        plt.clf()

        #num = int(string) # convert the unicode string to an int
        #print(num)


ser.close()