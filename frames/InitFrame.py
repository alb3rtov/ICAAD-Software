import sys
import platform
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

import gui
from frames import MainFrame

class InitFrame:
    def __init__(self, master):
        self.button_border1, self.button1 = gui.create_button(master, "What is ICAAD Software GUI?")
        self.button1.configure(command = self.software_info)
        
        self.button_border2, self.button2 = gui.create_button(master, "Check operating system")
        self.button2.configure(command = lambda: self.check_system(master))
        
        self.button_border3, self.button3 = gui.create_button(master, "Exit")
        self.button3.configure(command = lambda: self.exit_program(master))
  
    def exit_program(self, master):
        option = messagebox.askquestion("Exit program","Do yo want to exit?")
        if option == "yes":
            sys.exit();

    def software_info(self):
        top = tk.Toplevel()
        top.title("Software information")
        top.iconbitmap("img/icaad.ico")
        myLabel = tk.Label(top, text="ICAAD Software is a assistant of instalation, configuration, administration of Active Directory").pack()

    def check_system(self, master):
        if platform.system() == 'Windows':
            if platform.release() == "10" or platform.release() == "16" or platform.release() == "19":
                messagebox.showinfo("Check operating system","Version " + platform.system() + " " + platform.release() + " is correct")
               
                # Delete current widgets
                self.button_border1.destroy()
                self.button1.destroy()
                self.button_border2.destroy()
                self.button2.destroy()
                self.button_border3.destroy()
                self.button3.destroy()
                
                # Create next frame menu
                e = MainFrame.MainFrame(master)

            else:
                messagebox.showwarning("Check operating system", "Must be a Windows version 2012/2016/2019 " + "\n(You have " + platform.system() + " " + platform.release() + ")")
        else:
            messagebox.showwarning("Check operating system", "Must be a Windows version 2012/2016/2019 " + "\n(You have " + platform.system() + " " + platform.release() + ")")