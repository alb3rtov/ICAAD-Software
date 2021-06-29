import tkinter as tk

import gui
from frames import InitFrame

class ConfigNCFrame:
    def __init__(self, master):
        master.geometry("500x520")
        frame = tk.Frame(master, bg='white', width=300, height=300)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
        self.button_border1, self.button1 = gui.create_button(frame, "NC 1")
        self.button1.configure(command = self.prueba)
        self.button_border1.grid(column=0, row=0, pady=20)
        self.button1.grid(column=0, row=0)

        self.button_border2, self.button2 = gui.create_button(frame, "NC 2")
        self.button2.configure(command = self.prueba)
        self.button_border2.grid(column=0, row=1,pady=20)
        self.button2.grid(column=0, row=1)

        self.button_border3, self.button3 = gui.create_button(frame, "NC 3")
        self.button3.configure(command = self.prueba)
        self.button_border3.grid(column=0, row=2,pady=20)
        self.button3.grid(column=0, row=1)

        self.button_border4, self.button4 = gui.create_button(frame, "Back")
        self.button4.configure(command = lambda: self.go_back(master))
        self.button_border4.grid(column=0, row=3,pady=20)
        self.button4.grid(column=0, row=2)

        self.buttons_list = [self.button1,
                            self.button2,
                            self.button3,
                            self.button4]
    
        self.buttons_border_list = [self.button_border1,
                                    self.button_border2,
                                    self.button_border3,
                                    self.button_border4]
    def prueba(self):
        return
    # Delete items and create previous frame
    def go_back(self, master):
        gui.destroy_items(self.buttons_list, self.buttons_border_list)  
        e = InitFrame.InitFrame(master) 