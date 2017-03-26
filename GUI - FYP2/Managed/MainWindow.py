import Tkinter
from WindowFrame import WindowFrame


class MainWindow:

    MainWindow = 0
    listOfWinFrame = list()

        
    def __init__(self):    
        ### MainWindow: Hosts other windows (frames) ###
        global MainWindow
        MainWindow = Tkinter.Tk()
        MainWindow.geometry('800x534')
        MainWindow.resizable(width = False, height = False)
        #MainWindow.overrideredirect(1)


        ### Window "Frames" Dimensions ###
        wHeight = 514
        wWidth = 780

        ### Creating and Instantiating Objects of WindowFrame ###
        firstFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
        secFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
        thirdFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
        fourthFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
        fifthFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
        sixthFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
        seventhFrame = WindowFrame(self, MainWindow, wWidth, wHeight)


        ### Adding All WindowFrames to the List ###
        global listOfWinFrame
        self.listOfWinFrame.append(firstFrame)
        self.listOfWinFrame.append(secFrame)
        self.listOfWinFrame.append(thirdFrame)
        self.listOfWinFrame.append(fourthFrame)
        self.listOfWinFrame.append(fifthFrame)
        self.listOfWinFrame.append(sixthFrame)
        self.listOfWinFrame.append(seventhFrame)

        ### Hide All Except first ###
        
        for i in xrange(len(self.listOfWinFrame)):
            if(i != 0):
                self.listOfWinFrame[i].hide()

            self.listOfWinFrame[0].unhide()

        MainWindow.mainloop()

    def getListOfWinFrame():
        return listOfWinFrame



#######################
### Main() Function ###
#######################

mainObj = MainWindow()
