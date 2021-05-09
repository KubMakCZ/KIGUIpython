from tkinter import *

root = Tk()

topleft = Frame(root)
topright = Frame(root)
bottomleft = Frame(root)
bottomright = Frame(root)

lbl1 = Label(topleft, text="topleft")
lbl2 = Label(topright, text="topright")
lbl3 = Label(bottomleft, text="bottomleft")
lbl4 = Label(bottomright, text="bottomright")

topleft.grid(row = 0, column = 0)
topright.grid(row = 0, column = 1)
bottomleft.grid(row = 1, column = 0)
bottomright.grid(row = 1, column = 1)

lbl1.grid(row = 0, column = 0)
lbl2.grid(row = 0, column = 0)
lbl3.grid(row = 0, column = 0)
lbl4.grid(row = 0, column = 0)

root.mainloop()