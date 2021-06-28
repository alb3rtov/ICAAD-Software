import sys
import time
import platform
import subprocess
import tkinter as tk
import re
from tkinter import messagebox


import gui
from frames import MainFrame

class InitFrame:
    def __init__(self, master):
        master.geometry("500x520")
        frame = tk.Frame(master, bg='white', width=300, height=300)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.button_border1, self.button1 = gui.create_button(frame, "What is ICAAD Software GUI?")
        self.button1.configure(command = self.software_info)
        self.button_border1.grid(column=0, row=0, pady=20)
        self.button1.grid(column=0, row=0)

        self.button_border2, self.button2 = gui.create_button(frame, "Check operating system")
        self.button2.configure(command = lambda: self.check_system(master))
        self.button_border2.grid(column=0, row=1,pady=20)
        self.button2.grid(column=0, row=1)

        self.button_border3, self.button3 = gui.create_button(frame, "Exit")
        self.button3.configure(command = lambda: self.exit_program(master))
        self.button_border3.grid(column=0, row=2,pady=20)
        self.button3.grid(column=0, row=2)

        self.buttons_list = [self.button1,
                            self.button2,
                            self.button3]
    
        self.buttons_border_list = [self.button_border1,
                                    self.button_border2,
                                    self.button_border3]
        
    # Exit program function
    def exit_program(self, master):
        option = messagebox.askquestion("Exit program","Do you want to exit?")
        if option == "yes":
            sys.exit();

    # Show software information 
    def software_info(self):
        top = tk.Toplevel()
        top.title("Software information")
        top.iconbitmap("img/icaad.ico")
        myLabel = tk.Label(top, text="ICAAD Software is a assistant of instalation, configuration, administration of Active Directory").pack()

    # Delete all items of the frame
    def destroy_items(self):
        for index in range(0, len(self.buttons_list)):
            self.buttons_list[index].destroy()
            self.buttons_border_list[index].destroy()

    # Create new next frame menu if system is Windows Server
    def check_os(self, master):
        if ("Microsoft Windows Server 2012" in gui.g_dict_osinfo["OsName"] or 
            "Microsoft Windows Server 2016" in gui.g_dict_osinfo["OsName"] or 
            "Microsoft Windows Server 2019" in gui.g_dict_osinfo["OsName"]):

            messagebox.showinfo("Check operating system","Version " + gui.g_dict_osinfo["OsName"] + " is valid")
            # Delete current widgets
            self.destroy_items()
            # Create next frame menu
            e = MainFrame.MainFrame(master)

        else:
            messagebox.showwarning("Check operating system", "Must be a Windows version 2012/2016/2019 " + "\n(You have " + gui.g_dict_osinfo["OsName"] + ")")
   
    # Check if the system is Windows Server
    def check_system(self, master):
        if len(gui.g_dict_osinfo) == 0:
            if platform.system() == 'Windows':
                # Create background subprocess for cmdlet
                p = subprocess.Popen(['powershell.exe', "-ExecutionPolicy", "Bypass", '.\\scripts\\hashtable.ps1'], stdout=subprocess.PIPE, stderr= subprocess.PIPE)
        
                # Create progress bar
                gui.create_progress_bar("Executing command Get-ComputerInfo.", p)

                skip_title = 0
                for line in p.stdout:
                    if skip_title == 3 and len(line) > 2:
                        # Decode line format
                        decoded_line = line.decode('utf-8', errors='strict').strip()
                        clean_line = re.sub('\s+',' ', str(decoded_line))
                        
                        key = clean_line.split()[0]
                        gui.g_dict_osinfo[key] = clean_line.partition(' ')[2]

                    else:
                        skip_title += 1

                self.check_os(master)

            else:
                messagebox.showwarning("Check operating system", "Must be a Windows version 2012/2016/2019 " + "\n(You have " + gui.g_dict_osinfo["OsName"] + ")")
        else:
            self.check_os(master)