import Tkinter
import PIL
from PIL import ImageTk
from PIL import Image

class WindowFrame:

    xAxis = 0
    yAxis = 0
    MainWindow = 0
    MainObj = 0
    winFrame = object()
    btnQuit = object()
    btnNext = object()
    
    def __init__(self, mainObj, MainWin, wWidth, wHeight, xAxis = 10, yAxis = 10):
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.MainWindow = MainWin
        self.MainObj = mainObj
        
        global winFrame
        self.winFrame = Tkinter.Frame(self.MainWindow, width = wWidth, height = wHeight)
        self.winFrame['borderwidth'] = 2
        self.winFrame['relief'] = 'sunken'
        self.winFrame.place(x=xAxis,y=yAxis)

        self.btnQuit= Tkinter.Button(self.winFrame, text = "Close", width=8, command= lambda: self.quitProgram(self.MainWindow))
        self.btnQuit.place(x=650, y=450)
        self.btnNext = Tkinter.Button(self.winFrame, text = "Next", width=8, command= self.NextWindow)
        self.btnNext.place(x=575, y=450)

##        samplelabel = Tkinter.Label(self.winFrame, text="Yeahhh")
##        samplelabel.place(x=120,y=40)

        img = Image.open("C:\\Users\\Imran Ullah\\Desktop\\FYP\\GUI - FYP2\\Images\\6_left-grayscale.png")
        h,w = img.size
        print ( h , " " , w)
        imgRes = img.resize((300,300), Image.ANTIALIAS)
        imgTk = ImageTk.PhotoImage(image=imgRes)
        labelImg = Tkinter.Label(self.winFrame, image = imgTk)
        labelImg.place(x=100, y=40)


    def quitProgram(self, window):
        global MainWindow
        self.MainWindow.destroy()
        
    def getWindowFrame():
        global winFrame
        return winFrame

    def unhide(self):
        self.winFrame.place(x=self.xAxis,y=self.yAxis)

    def hide(self):
        self.winFrame.place_forget()

    def NextWindow(self):
        global MainObj
        listWF = list(self.MainObj.listOfWinFrame)
        print("Size: ", len(listWF))
        current = 0
        for i in xrange(len(listWF)):
            listWF[i].hide()
            if (listWF[i] == self):
                current = i
                print (current)
                

        if (current == (len(listWF)-1)):
            ## Button Disable
            print ("Last")
            listWF[current].unhide()
            self.btnNext['state'] = 'disable'
        else:
            listWF[current+1].unhide()
