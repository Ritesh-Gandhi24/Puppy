from turtle import color
import serial
import time
import numpy
import matplotlib.pyplot as plt


# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM4', 9800, timeout=1)
time.sleep(2)

figure, axs = plt.subplots(2,2)
bl = plt.Circle((0.5,0.5), 0.5, color='red')
fl = plt.Circle((0.5,0.5), 0.5, color='red')
br = plt.Circle((0.5,0.5), 0.5, color='red')
fr = plt.Circle((0.5,0.5), 0.5, color='red')

axs[0,0].set_title('FL')
axs[0,1].set_title('FR')
axs[1,0].set_title('BL')
axs[1,1].set_title('BR')

axs[1,0].add_artist(bl)
axs[1,1].add_artist(br)
axs[0,0].add_artist(fl)
axs[0,1].add_artist(fr)

plt.show()


while(1):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        stripped_string = string.strip()
        values = list(stripped_string)
        
        figure, axs = plt.subplots(2,2)
        if(values[0]=='h'):
            fl = plt.Circle((0.5,0.5), 0.5, color='green')
        if(values[0]=='l'):
            fl = plt.Circle((0.5,0.5), 0.5, color='red')

        if(values[1]=='h'):
            fr = plt.Circle((0.5,0.5), 0.5, color='green')
        if(values[1]=='l'):
            fr = plt.Circle((0.5,0.5), 0.5, color='red')
        
        if(values[2]=='h'):
            bl = plt.Circle((0.5,0.5), 0.5, color='green')
        if(values[2]=='l'):
            bl = plt.Circle((0.5,0.5), 0.5, color='red')

        if(values[3]=='h'):
            br = plt.Circle((0.5,0.5), 0.5, color='green')
        if(values[3]=='l'):
            br = plt.Circle((0.5,0.5), 0.5, color='red')
        
        axs[0,0].set_title('FL')
        axs[0,1].set_title('FR')
        axs[1,0].set_title('BL')
        axs[1,1].set_title('BR')

        axs[1,0].add_artist(bl)
        axs[1,1].add_artist(br)
        axs[0,0].add_artist(fl)
        axs[0,1].add_artist(fr)

        plt.show()
        plt.pause(0.5)
        plt.clf()

        #num = int(string) # convert the unicode string to an int
        #print(num)


ser.close()