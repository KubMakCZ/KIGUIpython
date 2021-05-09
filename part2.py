import tkinter as tk

win = tk.Tk()
win.title("Dynamically Resize Buttons")
win.geometry("700x500")

tk.Grid.rowconfigure(win, 0,weight=1)
tk.Grid.columnconfigure(win,0,weight=1)


win.mainloop()
