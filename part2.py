import tkinter as tk
import sys

#vytvoreni TK
win = tk.Tk()
win.title("Part 2 - Dashboard")
win.geometry("700x500")

#configurace grid systemu
tk.Grid.rowconfigure(win, 0,weight=1)
tk.Grid.columnconfigure(win,0,weight=1)

b1= tk.Button(win, text= "1", command=lambda: print("1"))
b2= tk.Button(win, text= "2", command=lambda: sys.exit(0))
b3= tk.Button(win, text= "3", command=lambda: print("4"))
b4= tk.Button(win, text= "4", command=lambda: print("4"))
b5= tk.Button(win, text= "5", command=lambda: print("5"))
b6= tk.Button(win, text= "6", command=lambda: print("6"))


#priprava na vytvoreni Mrizky pro dynamicke transformovani
bl= [b1, b2, b3]
row_no=0

bl2= [b3, b4]
row2_no=0
#Loop through all the buttons and configure it row-wise
for button in bl:
   tk.Grid.rowconfigure(win,row_no, weight=1)
   row_no+=1

for button in bl2:
   tk.Grid.columnconfigure(win,row2_no,weight=1)
   row2_no+=1

#Vypsani vsechn tlacitek
b1.grid(row=0, column=0, sticky= "NSEW")
b2.grid(row=0, column=1, sticky= "NSEW")
b3.grid(row=1, column=0, sticky= "NSEW")
b4.grid(row=1, column=1, sticky= "NSEW")
b5.grid(row=2, column=0, sticky= "NSEW")
b6.grid(row=2, column=1, sticky= "NSEW")



win.mainloop()
