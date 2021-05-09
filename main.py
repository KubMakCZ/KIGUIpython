import tkinter as tk
import os, sys

# ###############
#  Global Metody
# ###############

def osCheck():
    return sys.platform


# ###############
# Třídy
# ###############



# ###############
# Hlavní část programu po spuštění
# ###############
if __name__ == '__main__':
    SystemName = osCheck() #uložení názvu systému pro vypsání
    window = tk.Tk() #Vyvolání zaklad okna
    label = tk.Label(text=f"Tvůj OS = {SystemName}") #vypsaní za pomoci f-stringu
    label.pack()
    window.mainloop()
