import Tkinter
import cv2
import PIL
from PIL import ImageTk
from PIL import Image

### MainWindow: Hosts other windows (frames) ###
MainWindow = Tkinter.Tk()
MainWindow.geometry('800x534')
MainWindow.resizable(width = False, height = False)
#MainWindow.overrideredirect(1)


### Window "Frames" Dimensions ###
wHeight = 514
wWidth = 780


### Functions ###

    ### Global Function ###

def quitProgram():
    MainWindow.destroy()

    ### Welcome Frame Functions ###
def NextWindow(self):
    if self == welFrame:
        print("Olambaiiiii")
    secFrame.place(x=10,y=1)



### Window Frames ###
    ### Welcome Frame ###
welFrame = Tkinter.Frame(MainWindow, width = wWidth, height = wHeight)
welFrame['borderwidth'] = 2
welFrame['relief'] = 'sunken'
welFrame.place(x=10,y=10)

welLabel = Tkinter.Label(welFrame, text="Welcome to Automated DR Identifier System", font=("Helvetica", 16))
welLabel.place(x=200,y=170)
descrpLabel = Tkinter.Label(welFrame, text="Click \"Next\" to get started!!")
descrpLabel.place(x=200,y=210)

btnQuit_welFrame = Tkinter.Button(welFrame, text = "Close", width=8, command=quitProgram)
btnQuit_welFrame.place(x=650, y=450) 
btnNext_welFrame = Tkinter.Button(welFrame, text = "Next", width=8, command= lambda: NextWindow(welFrame))
btnNext_welFrame.place(x=575, y=450)                                   

    ### Second Frame ###
secFrame = Tkinter.Frame(MainWindow, width = wWidth, height = wHeight)
secFrame['borderwidth'] = 2
secFrame['relief'] = 'sunken'
secFrame.place(x=10,y=10)

##secLabel = Tkinter.Label(secFrame, text="Welcome to Automated DR Identifier System", font=("Helvetica", 16))
##secLabel.place(x=200,y=170)
##secDesLabel = Tkinter.Label(secFrame, text="Click \"Next\" to get started!!")
##secDesLabel.place(x=200,y=210)

btnQuit_secFrame = Tkinter.Button(secFrame, text = "Close", width=8)
btnQuit_secFrame.place(x=650, y=450) 
btnNext_secFrame = Tkinter.Button(secFrame, text = "Next", width=8)
btnNext_secFrame.place(x=575, y=450) 




img = Image.open("C:\\Users\\Imran Ullah\\Desktop\\FYP\\GUI - FYP2\\Images\\6_left-grayscale.png")
h,w = img.size
#print (500 , " " , w+100)
imgRes = img.resize((int(h*2),int(w*2)), Image.ANTIALIAS)
imgTk = ImageTk.PhotoImage(image=imgRes)

#img = cv2.imread('C:\\Users\\Imran Ullah\\Desktop\\FYP\\Images\\17_right.jpeg')
#labelImg = Tkinter.Label(MainWindow, image = imgTk)
#labelImg.grid(column=4, row = 1, pady = 10)
#panel.pack(side = "bottom", fill = "both")
#labelImg.place(x=3,.30, y =100)


### Hiding all Frames except Welcome Frame ###
secFrame.place_forget()

# Start Tkinter event - loop
MainWindow.mainloop()
