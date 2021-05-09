from tkinter import *
win= Tk()
win.title("Dynamically Resize Buttons")
win.geometry("700x500")

Grid.rowconfigure(win, 0,weight=1)
Grid.columnconfigure(win,0,weight=1)

b1= Button(win, text= "C++", command=lambda: print("AHOJ"))
b2= Button(win, text= "Java", command=lambda: sys.exit(0))

bl= [b1, b2]
row_no=0
#Loop through all the buttons and configure it row-wise
for button in bl:
   Grid.rowconfigure(win,row_no, weight=1)
   row_no+=1


b1.grid(row=0, column=0, sticky= "nsew")
b2.grid(row=1, column=0, stick= "nsew")

win.mainloop()