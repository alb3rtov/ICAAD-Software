import subprocess
import tkinter as tk
from tkinter import messagebox

import gui
from frames import InitFrame

class MainFrame:
    def __init__(self, master):
        # Create frame and buttons of this frame
        master.geometry("700x400")
        frame = tk.Frame(master, bg='white', width=500, height=300)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.conf_ad_button_border, self.conf_ad_button = gui.create_button(frame, "Active Directory configuration")
        self.conf_ad_button.configure(command = self.ad_configuration, height=2)
        self.conf_ad_button_border.grid(column=0,row=0, pady=10, padx=10)
        self.conf_ad_button.grid(column=0,row=0)

        self.install_ad_button_border, self.install_ad_button = gui.create_button(frame, "Active Directory installation")
        self.install_ad_button.configure(command = self.ad_configuration, height=2)
        self.install_ad_button_border.grid(column=0,row=1, pady=10, padx=10)
        self.install_ad_button.grid(column=0,row=1)

        self.check_ad_button_border, self.check_ad_button = gui.create_button(frame, "Active Directory check")
        self.check_ad_button.configure(command = self.ad_check, height=2)
        self.check_ad_button_border.grid(column=0,row=2, pady=10, padx=10)
        self.check_ad_button.grid(column=0,row=2)

        self.manage_ad_button_border, self.manage_ad_button = gui.create_button(frame, "Active Directory manage")
        self.manage_ad_button.configure(command = self.ad_configuration, height=2)
        self.manage_ad_button_border.grid(column=1,row=0, pady=10, padx=10)
        self.manage_ad_button.grid(column=1,row=0)

        self.conf_dns_button_border, self.conf_dns_button = gui.create_button(frame, "DNS configuration")
        self.conf_dns_button.configure(command = self.ad_configuration, height=2)
        self.conf_dns_button_border.grid(column=1,row=1, pady=10, padx=10)
        self.conf_dns_button.grid(column=1,row=1)

        self.back_button_border, self.back_button = gui.create_button(frame, "Back")
        self.back_button.configure(command = lambda: self.go_back(master), height=2)
        self.back_button_border.grid(column=1,row=2, pady=10, padx=10)
        self.back_button.grid(column=1,row=2)

        self.buttons_list = [self.conf_ad_button,
                            self.install_ad_button,
                            self.check_ad_button,
                            self.manage_ad_button,
                            self.conf_dns_button,
                            self.back_button]

        self.buttons_border_list = [self.conf_ad_button_border,
                                    self.install_ad_button_border,
                                    self.check_ad_button_border,
                                    self.manage_ad_button_border,
                                    self.conf_dns_button_border,
                                    self.back_button_border]

    def ad_check(self):
        p = subprocess.Popen(['powershell.exe', "-ExecutionPolicy", "Bypass", '.\\scripts\\adcheck.ps1'], stdout=subprocess.PIPE, stderr= subprocess.PIPE)
        
        gui.create_progress_bar("Executing command Get-WindowsFeature.",p)
        
        for line in p.stdout:
            decoded_output = line.decode('utf-8', errors='strict').strip()

        if decoded_output == "False":
            messagebox.showinfo("Check Active Directory", "Active Directory services are not installed on this computer")
        else:
            messagebox.showinfo("Check Active Directory", "Active Directory services are installed on this computer")

    def ad_configuration(self):
        print("hola")
    
    # Delete all items of the frame
    def destroy_items(self):
        for index in range(0, len(self.buttons_list)):
            self.buttons_list[index].destroy()
            self.buttons_border_list[index].destroy()

    # Delete items and create previous frame
    def go_back(self, master):
        self.destroy_items()  
        e = InitFrame.InitFrame(master) 