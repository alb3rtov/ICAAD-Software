import tkinter as tk
import tkinter.font as font
from frames import InitFrame

class MainFrame:
    def __init__(self, master):
        main_font = font.Font(size="12", family="Helvetica")
        self.back_button = tk.Button(master, text="Back", command = lambda: self.go_back(master))
        self.back_button.pack()
    
    def go_back(self, master):
        self.back_button.destroy()
        e = InitFrame.InitFrame(master) 