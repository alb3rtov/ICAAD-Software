import sys
import tkinter as tk
from tkinter import messagebox

import gui
from frames import MainFrame
from frames import ConfigNCFrame

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
        self.button2.configure(command = lambda: self.main_menu(master))
        self.button_border2.grid(column=0, row=1,pady=20)
        self.button2.grid(column=0, row=1)

        self.button_border3, self.button3 = gui.create_button(frame, "Configure network cards")
        self.button3.configure(command = lambda: self.configure_nc_cards(master))
        self.button_border3.grid(column=0, row=2,pady=20)
        self.button3.grid(column=0, row=1)

        self.button_border4, self.button4 = gui.create_button(frame, "Exit")
        self.button4.configure(command = lambda: self.exit_program(master))
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

    # Go to main configuration frame   
    def main_menu(self, master):
        gui.check_system(master)
        gui.destroy_items(self.buttons_list, self.buttons_border_list)
        e = MainFrame.MainFrame(master)
    
    # Go to configuration NC cards frame
    def configure_nc_cards(self, master):
        gui.check_system(master)
        gui.destroy_items(self.buttons_list, self.buttons_border_list)
        e = ConfigNCFrame.ConfigNCFrame(master)
    
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