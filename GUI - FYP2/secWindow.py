import Tkinter
from Tkinter import *
import tkFileDialog

##class secWindow():
    
top = Tk()

def openFileDialog():
  tkFileDialog.askopenfile(mode='w')
        
def closeFunc():
  top.destroy()

top.geometry('800x500')
top.resizable(0,0)
top.configure(background = "White")

WindowLabel = Label( text = "Detection of Diabetic Retinopathy", height = 1, width = 40)
WindowLabel.place(x=150, y=30)
WindowLabel.configure(background="White", font=("Times New Roman", 16, "bold"))

ExportBtn = Button(height = 1, width = 10, text ="Export", command = openFileDialog)
ExportBtn.place(x = 510, y = 450)

closeBtn = Button( height = 1, width = 10, text="Close", command = closeFunc)
closeBtn.place(x=600, y=450)



""" Group the Widgets by Labels """
""" ##labelframe = LabelFrame(text="This is a Frame")
##labelframe.place(x = 30, y = 30)
"""

ResultsLabel = Label( text = "Results", height = 1, width = 10)
ResultsLabel.place(x=60, y=80)
ResultsLabel.configure(background="White", font=("Times New Roman", 12, "bold"))

subHeadLabel = Label(text = "Classifier", height = 1, width = 10)
subHeadLabel.place(x=120, y=120)
subHeadLabel.configure(background="White", font=("Times New Roman", 10, "bold"))

subHead2Label = Label(text = "DR Level", height = 1, width = 10)
subHead2Label.place(x=400, y=120)
subHead2Label.configure(background="White", font=("Times New Roman", 10, "bold"))

clsfOneLabel = Label(text = "CNN", height = 1, width = 10)
clsfOneLabel.place(x=120, y=150)
clsfOneLabel.configure(background="White", font=("Times New Roman", 10))

clsfTwoLabel = Label(text = "SVM", height = 1, width = 10)
clsfTwoLabel.place(x=120, y=170)
clsfTwoLabel.configure(background="White", font=("Times New Roman", 10))

clsfOneLabel = Label(text = "3 (Severe)", height = 1, width = 10)
clsfOneLabel.place(x=420, y=150)
clsfOneLabel.configure(background="White", font=("Times New Roman", 10))

clsfTwoLabel = Label(text = "3 (Severe)", height = 1, width = 10)
clsfTwoLabel.place(x=420, y=170)
clsfTwoLabel.configure(background="White", font=("Times New Roman", 10))

ResultsLabel = Label( text = "Overall Result:", height = 1, width = 20)
ResultsLabel.place(x=50, y=300)
ResultsLabel.configure(background="White", font=("Times New Roman", 12, "bold"))

ResultsLabel = Label( text = "Severe", height = 1, width = 20)
ResultsLabel.place(x=450, y=300)
ResultsLabel.configure(background="White", font=("Times New Roman", 12, "bold"))    

##    img = ImageTk.PhotoImage(Image.open("C:\\Users\\Imran Ullah\\Desktop\Files\\GUI - FYP2\\Images\\6_left-grayscale.png"))
##    panel = tk.Label(top, image = img)
##    panel.pack(side = "bottom", fill = "both")

top.mainloop()
