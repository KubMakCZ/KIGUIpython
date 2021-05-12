import tkinter as tk
import os, sys, time, wakeonlan

# ###############
#  Global Metody
# ###############

def osCheck():
    return sys.platform


# ###############
# Třídy
# ###############

class wakeonlan:

class nmapgui:

class pocasiapp:

class texteditorwin:

class readtempcpu:


# ###############
# Hlavní část programu po spuštění
# ###############
if __name__ == '__main__':
    window = tk.Tk() #Vyvolání zaklad okna

    label = tk.Label(text=f"Tvůj OS = {osCheck()}") #vypsaní za pomoci f-stringu
    label.pack()
    window.mainloop()
