from tkinter import *

gui = Tk()

gui.title('GUI ')

# we create button successfully but button will not show because we haven't call button
btn = Label(gui,text="this is First Python Button") 
btn.pack(side=BOTTOM,pady=50)
btn.mainloop()