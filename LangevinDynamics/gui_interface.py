import tkinter as tk
from tkinter import filedialog

global filename    
def gui(element,show):
    root = tk.Tk()
    elementList  = []
    labelList    = []
    for i in element:
        labelList.append(tk.Label(root, text=i))
        labelList[-1].pack()
        elementList.append(tk.Entry(root))
        elementList[-1].pack()
        
    a = tk.Button(root, text="browse file", width=10, command=lambda: select(elementList))
    a.pack()
    b = tk.Button(root, text="get", width=10, command=lambda:callback(elementList))
    b.pack()
    if show:
        tk.mainloop()
    return elementList,labelList        

def select(fname):
    vname = filedialog.askopenfilename(initialdir = "/",title = "Select file for potential")
    fname[-1].insert(0,vname)

def callback(element):
    val = []
    for i in element:
        val.append(i.get())
    print( val)
    print( filename )

def start():
    element = ["x","p","m","Temperature","lambda","dt","steps","output","filename"]
    gui(element,True)


