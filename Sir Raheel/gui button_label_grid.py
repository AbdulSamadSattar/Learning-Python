from tkinter import *

gui = Tk()

gui.title('GUI ')
gui.geometry("400x400")

lb = Label(gui,text="First Python Label 1")
lb.grid(row=0,column=0, sticky = N, padx = 0, pady=100)

lb = Label(gui,text="First Python Label 2")
lb.grid(row=1,column=0, sticky = N, padx = 10, pady=50)

gui.mainloop()