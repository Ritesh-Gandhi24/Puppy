
import tkinter as tk
import serial

root = tk.Tk()
canvas = tk.Canvas(root, width=1500, height=800, borderwidth=0, highlightthickness=0,
                   bg="black")
canvas.grid()

value=0
prev=0
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1)
def arduino_handler():
    try:
        global value
        global prev
        data = arduino.readline()
        data=str(data)
        print(data[2: data.index('r')-1])
        value=int(data[2: data.index('r')-1])
        
    except Exception as e:
        pass
    root.after(5, arduino_handler)

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle


def update_colour():
    if (value-8>=0):
        canvas.create_circle(400, 150, 120, fill="green", outline="")
    else:
        canvas.create_circle(400, 150, 120, fill="red", outline="")
    canvas.update()

    if (value & 0b00000100 == 4):
        canvas.create_circle(1000, 150, 120, fill="green", outline="")
    else:
        canvas.create_circle(1000, 150, 120, fill="red", outline="")
    canvas.update()

    if (value & 0b00000010 == 2):
        canvas.create_circle(400, 550, 120, fill="green", outline="")
    else:
        canvas.create_circle(400, 550, 120, fill="red", outline="")
    canvas.update()

    if (value & 0b00000001 == 1):
        canvas.create_circle(1000, 550, 120, fill="green", outline="")
    else:
        canvas.create_circle(1000, 550, 120, fill="red", outline="")
    canvas.update()
    root.after(10, update_colour)

try:
    if (value-1000>=0):
        canvas.create_circle(400, 150, 120, fill="green", outline="")
    else:
        canvas.create_circle(400, 150, 120, fill="red", outline="")
    canvas.update()

    if ((value%1000)-100>=0):
        canvas.create_circle(1000, 150, 120, fill="green", outline="")
    else:
        canvas.create_circle(1000, 150, 120, fill="red", outline="")
    canvas.update()

    if ((value%100)-10>=0):
        canvas.create_circle(400, 550, 120, fill="green", outline="")
    else:
        canvas.create_circle(400, 550, 120, fill="red", outline="")
    canvas.update()

    if (value%10):
        canvas.create_circle(1000, 550, 120, fill="green", outline="")
    else:
        canvas.create_circle(1000, 550, 120, fill="red", outline="")
    canvas.update()

    canvas.create_text(400, 300, text="Front-Left", fill="white", font=('Helvetica 25 bold'))
    canvas.create_text(1000, 300, text="Front-Right", fill="white", font=('Helvetica 25 bold'))
    canvas.create_text(400, 700, text="Back-Left", fill="white", font=('Helvetica 25 bold'))
    canvas.create_text(1000, 700, text="Back-right", fill="white", font=('Helvetica 25 bold'))
    canvas.pack()

    root.title("Doggo_ground_detect")
    root.after(0, arduino_handler)
    root.after(0, update_colour)
    root.mainloop()
except Exception as e:
    pass



