import Tkinter
from Tkinter import *
import tkFileDialog

class MainWindow():

    global top
    top = Tk()

    def openFileDialog():
        tkFileDialog.askopenfile(mode='r')
            
    def closeFunc():
        top.destroy()

    top.geometry('800x500')
    top.resizable(0,0)
    top.configure(background = "White")

    WindowLabel = Label( text = "Detection of Diabetic Retinopathy", height = 1, width = 40)
    WindowLabel.place(x=150, y=30)
    WindowLabel.configure(background="White", font=("Times New Roman", 16, "bold"))

    browseBtn = Button(height = 1, width = 10, text ="Browse", command = openFileDialog)
    browseBtn.place(x = 420, y = 450)

    closeBtn = Button( height = 1, width = 10, text="Close", command = closeFunc)
    closeBtn.place(x=600, y=450)

    ClsfiersLabel = Label( text = "Classifiers", height = 1, width = 10)
    ClsfiersLabel.place(x=60, y=80)
    ClsfiersLabel.configure(background="White", font=("Times New Roman", 12, "bold"))

    global CNNcbVar
    CNNcbVar = IntVar
    global CNNchckBox
    CNNchckBox = Checkbutton(text = "CNN", variable = CNNcbVar, height = 1, width = 10)
    CNNchckBox.place(x=50, y=100)
    CNNchckBox.configure(background="White")
                         
    global SVMcbVar
    SVMcbVar = IntVar()
    global SVMchckBox
    SVMchckBox = Checkbutton(text = "SVM", variable = SVMcbVar, height = 1, width = 10)
    SVMchckBox.place(x=50, y=120)
    SVMchckBox.configure(background="White")
    
    operationBtn = Button( height = 1, width = 10, text="Operation")
    operationBtn.place(x=510, y=450)
    top.mainloop()
""" Problem Here!!
    Can't change state based on CheckBox Selection """
##    def checkForClassifiers():
##        print (CNNcbVar.get)
##        if CNNcbVar.get():
##            clsfWarnLabel = Label(text = "*Select a Classifier")
##            clsfWarnLabel.place(x=65,y=140)
##            clsfWarnLabel.configure(background="White", foreground = "Red", font=("Times New Roman", 6, "bold"))
            



##    img = ImageTk.PhotoImage(Image.open("C:\\Users\\Imran Ullah\\Desktop\Files\\GUI - FYP2\\Images\\6_left-grayscale.png"))
##    panel = tk.Label(top, image = img)
##    panel.pack(side = "bottom", fill = "both")
