from tkinter import *

# Creating window,title and size
win = Tk()
win.title("Do you know temperature?")
#win.geometry("400x300")

# Label
L1=Label(win, text= "Fahrenheit:")
L1.grid(row=1, column=0)

L2=Label(win, text= "Celsius:")
L2.grid(row=2, column=0)

# Making the first entry
e1 = Entry(win,bd = 5)
e1.grid(row=1,column=1)


# Making the second entry
e2 = Entry(win,bd = 5)
e2.grid(row = 2,column=1)

# Define function
def action():
    Fah = e1.get()
    Cel = e2.get()
    if len(Fah) == 0:
        Fah = float(e2.get()) * 9/5 + 32
        e1.insert(0,str(Fah))
    if len(Cel) == 0:
        Cel = (float(e1.get()) - 32) * 5/9
        e2.insert(0,str(Cel))

# Adding button to press
b1 = Button(win,text="Calculate!",command= lambda:action())
b1.grid(row=3,ipadx=10,columnspan=2)

win.mainloop()
