import sys
import time
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import HORIZONTAL

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
        option = messagebox.askquestion("Exit program","Do you want to exit?")
        if option == "yes":
            sys.exit();

    def software_info(self):
        top = tk.Toplevel()
        top.title("Software information")
        top.iconbitmap("img/icaad.ico")
        myLabel = tk.Label(top, text="ICAAD Software is a assistant of instalation, configuration, administration of Active Directory").pack()


    def check_system(self, master):
        if platform.system() == 'Windows':

            #Create background subprocess for cmdlet
            p = subprocess.Popen(['powershell.exe', 'Get-ComputerInfo OsName'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
           
            top = tk.Toplevel()
            top.resizable(False, False)
            top.geometry("400x80")
            
            top.title("Checking OS information")
            top.iconbitmap("img/icaad.ico")
            lbl = tk.Label(top, text= "Executing command Get-ComputerInfo", bg='white', fg='#707070').pack(pady=10)
            s = ttk.Style()
            s.theme_use("winnative")
            s.configure("blue.Horizontal.TProgressbar",troughcolor='#f2f2f2', foreground='white', background='#0077d1')
            progress_bar = ttk.Progressbar(top, style="blue.Horizontal.TProgressbar", orient=HORIZONTAL, length=300, mode="indeterminate")
            progress_bar.pack()
            
            while (p.poll() is None):
                if progress_bar['value'] == 100:
                    progress_bar['value'] = 0
                else: 
                    progress_bar['value'] += 5%100

                top.update_idletasks()
                time.sleep(0.125)
            
            top.destroy()
            for line in p.stdout:
                if "Microsoft Windows" in str(line):
                    win_ver = str(line)

            if "Microsoft Windows Server 2012" in win_ver or "Microsoft Windows Server 2016" in win_ver or "Microsoft Windows Server 2019" in win_ver:
                messagebox.showinfo("Check operating system","Version " + win_ver + " is valid")
               
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