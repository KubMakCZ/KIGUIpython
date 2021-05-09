import tkinter as tk
import os

# jednoduchy program pro zjistění OS
if __name__ == '__main__': #pokud je program spustěný
    SystemName = os.name #uložení názvu systému pro vypsání
    window = tk.Tk()
    label = tk.Label(text=f"System je = {SystemName}") #vypsaní za pomoci f-stringu
    label.pack()
    window.mainloop()
