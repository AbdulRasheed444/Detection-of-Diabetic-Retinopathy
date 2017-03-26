import Tkinter
import cv2
import PIL
from PIL import ImageTk
from PIL import Image

### MainWindow: Hosts other windows (frames) ###
MainWindow = Tkinter.Tk()
MainWindow.geometry('500x350')
#MainWindow.overrideredirect(1)

### Window "Frames" Dimensions ###
wHeight = 200
wWidth = 450

### Frames of the other Windows ###
firstFrame = Tkinter.Frame(MainWindow, width = 800, height = 600)
firstFrame.pack_propagate(0)

firstFrame['borderwidth'] = 2
firstFrame['relief'] = 'sunken'
firstFrame.grid(column = 0, row=0, padx=20, pady=5)
#firstFrame.pack(fill=None, expand=False)


secondFrame = Tkinter.Frame(MainWindow, width = wWidth, height = wHeight)
secondFrame['borderwidth'] = 2
secondFrame['relief'] = 'sunken'
secondFrame.grid(column = 0, row=0, padx=20, pady=5)

thirdFrame = Tkinter.Frame(MainWindow, width = wWidth, height = wHeight)
thirdFrame['borderwidth'] = 2
thirdFrame['relief'] = 'sunken'
thirdFrame.grid(column = 0, row=0, padx=20, pady=5)

### Creating widgets for FirstFrame ###
# Create the label for the frame
Label_firstFrame = Tkinter.Label(firstFrame, text='Window 1')
Label_firstFrame.grid(column=0, row=0, pady=10, padx=10)

# Create the Tkinter.Button for the frame
btnQuit_firstFrame = Tkinter.Button(firstFrame, text = "Quit")
btnQuit_firstFrame.grid(column=0, row=1, pady=10)
btnNext_firstFrame = Tkinter.Button(firstFrame, text = "Next")
btnNext_firstFrame.grid(column=1, row=1, pady=10)
btnNext1_firstFrame = Tkinter.Button(firstFrame, text = "Operation")
btnNext1_firstFrame.grid(column=3, row=1, pady=40)


img = ImageTk.PhotoImage(Image.open("C:\\Users\\Imran Ullah\\Desktop\\FYP\\GUI - FYP2\\Images\\6_left-grayscale.png"))
#img.resize(300,400)
#img = cv2.imread('C:\\Users\\Imran Ullah\\Desktop\\FYP\\Images\\17_right.jpeg')
labelImg = Tkinter.Label(firstFrame, image = img)
#labelImg.grid(column=4, row = 1, pady = 10)
#panel.pack(side = "bottom", fill = "both")
labelImg.place( x=30, y =40) 

### Creating widgets secondFrame ###
# Create the label for the frame
Label_secondFrame = Tkinter.Label(secondFrame, text='Window 1')
Label_secondFrame.grid(column=0, row=0, pady=10, padx=10, sticky=(Tkinter.N))

# Create the Tkinter.Button for the frame
btnQuit_secondFrame = Tkinter.Button(secondFrame, text = "Quit")
btnQuit_secondFrame.grid(column=0, row=1, pady=10, sticky=(Tkinter.N))
btnNext_secondFrame = Tkinter.Button(secondFrame, text = "Next")
btnNext_secondFrame.grid(column=1, row=1, pady=10, sticky=(Tkinter.N))

### Creating widgets for ThirdFrame ###
# Create the label for the frame
Label_thirdFrame = Tkinter.Label(thirdFrame, text='Window 1')
Label_thirdFrame.grid(column=0, row=0, pady=10, padx=10, sticky=(Tkinter.N))

# Create the Tkinter.Button for the frame
btnQuit_thirdFrame = Tkinter.Button(thirdFrame, text = "Quit")
btnQuit_thirdFrame.grid(column=0, row=1, pady=10, sticky=(Tkinter.N))
btnNext_thirdFrame = Tkinter.Button(thirdFrame, text = "Next")
btnNext_thirdFrame.grid(column=1, row=1, pady=10, sticky=(Tkinter.N))

# Hide all frames in reverse order, but leave first frame visible (unhidden).
thirdFrame.grid_forget()
secondFrame.grid_forget()

# Start Tkinter event - loop
MainWindow.mainloop()
