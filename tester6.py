from tkinter import *
import nmap, time

window = Tk()
window.title("Skenovani site Dashboard")
window.geometry('860x400')

Grid.rowconfigure(window, 1,weight=1)
Grid.columnconfigure(window,1,weight=1)

lbl = Label(window, text="Zadej IP")
lbl.grid(column=0, row=0, sticky= "NSEW")
txt = Entry(window,width=10)
txt.grid(column=1, row=0, sticky= "NSEW")
txt_edit = Label(window, text="Zadejte IP a klikněte na start")
txt_edit.grid(column=0, row=1,columnspan=3, sticky= "NSEW")
def clicked():
    res = "Začinam skenovat sit: " + txt.get()
    txt_edit.configure(text= res)
    time.sleep(0.1)
    nm = nmap.PortScanner()
    nm.scan(hosts=txt.get(), arguments='-sS -O -A')
    res2= nm.csv()
    txt_edit.configure(text=res2)


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()