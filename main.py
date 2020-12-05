from tkinter import *
from app import checkPrice

root = Tk()
root.title('MÖ Fiyat Takibi')
root.geometry('500x250')

status= False
timeloop = 1000
def scaning():
    if status:
        print('Çalıştı')
        url = urlEntry.get()
        target = float(targetEntry.get())
        check = checkPrice(url,target)
        if check:
            stopApp()
        root.after(timeloop,scaning)


def startApp():
    global status
    status=True
    exeButton.config(text="DURDUR", command=stopApp)
    scaning()

def stopApp():
    global status
    status=False
    exeButton.config(text="BAŞLA", command=startApp)


global urlLabel
urlLabel = Label(root, text='Hedef:')
urlLabel.pack()

global urlEntry
urlEntry = Entry(root, width=40)
urlEntry.pack()


global targetLabel
targetLabel = Label(root, text='Fiyat:')
targetLabel.pack()

global targetEntry
targetEntry = Entry(root, width=40)
targetEntry.pack()

global exeButton
exeButton = Button(root,text='BAŞLA', command=startApp, width=20, height=2)
exeButton.pack(pady=10)

root.mainloop()
