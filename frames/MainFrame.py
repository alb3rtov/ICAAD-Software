import tkinter as tk
import tkinter.font as font
import gui
from frames import InitFrame

class MainFrame:
    def __init__(self, master):
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
        self.check_ad_button.configure(command = self.ad_configuration, height=2)
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

    def ad_configuration(self):
        print("hola")

    def go_back(self, master):
        self.conf_ad_button_border.destroy()
        self.conf_ad_button.destroy()
        self.install_ad_button_border.destroy()
        self.install_ad_button.destroy()
        self.check_ad_button_border.destroy()
        self.check_ad_button.destroy()
        self.manage_ad_button_border.destroy()
        self.manage_ad_button.destroy()
        self.conf_dns_button_border.destroy()
        self.conf_dns_button.destroy()
        self.back_button_border.destroy()
        self.back_button.destroy()

        e = InitFrame.InitFrame(master) 