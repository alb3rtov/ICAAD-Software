import sys
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from PIL import ImageTk,Image

import gui
from frames import MainFrame
from frames import ConfigNICFrame

class InitFrame:
    def __init__(self, master):
        master.geometry("500x600")
        frame = tk.Frame(master, bg='white', width=300, height=300)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.button_border1, self.button1 = gui.create_button(frame, "What is ICAAD Software GUI?")
        self.button1.configure(command = lambda: self.software_info(master))
        self.button_border1.grid(column=0, row=0, pady=20)
        self.button1.grid(column=0, row=0)

        self.button_border2, self.button2 = gui.create_button(frame, "Check operating system")
        self.button2.configure(command = lambda: self.main_menu(master))
        self.button_border2.grid(column=0, row=1,pady=20)
        self.button2.grid(column=0, row=1)

        self.button_border3, self.button3 = gui.create_button(frame, "Configure NICs")
        self.button3.configure(command = lambda: self.configure_nic(master))
        self.button_border3.grid(column=0, row=2,pady=20)
        self.button3.grid(column=0, row=2)

        self.button_border4, self.button4 = gui.create_button(frame, "Exit")
        self.button4.configure(command = lambda: self.exit_program(master))
        self.button_border4.grid(column=0, row=3,pady=20)
        self.button4.grid(column=0, row=3)

        image1 = Image.open("img/cmd.png")
        image1 = image1.resize((30, 30), Image.ANTIALIAS)
        self.cmd_icon = ImageTk.PhotoImage(image1)
        self.cmd_button = tk.Button(master, image=self.cmd_icon, bg='white', relief='groove', borderwidth=0, cursor='hand2', command= lambda: gui.open_cmd(master))
        self.cmd_button.place(x=430,y=530)
        self.cmd_button_border = tk.Frame()

        self.buttons_list = [self.button1,
                            self.button2,
                            self.button3,
                            self.button4,
                            self.cmd_button]
    
        self.buttons_border_list = [self.button_border1,
                                    self.button_border2,
                                    self.button_border3,
                                    self.button_border4,
                                    self.cmd_button_border]

    # Go to main configuration frame   
    def main_menu(self, master):
        if(gui.check_system(master)):
            gui.destroy_items(self.buttons_list, self.buttons_border_list)
            e = MainFrame.MainFrame(master)
    
    # Go to configuration NICs
    def configure_nic(self, master):
        if (gui.check_system(master)):
            gui.get_nics(master)
            gui.destroy_items(self.buttons_list, self.buttons_border_list)
            e = ConfigNICFrame.ConfigNICFrame(master)
    
    # Exit program function
    def exit_program(self, master):
        option = messagebox.askquestion("Exit program","Do you want to exit?")
        if option == "yes":
            sys.exit();

    # Go back of sofware information
    def go_back(self, master):
        self.back_button.destroy()
        self.myLabel.destroy()
        e = InitFrame(master)

    # Show software information 
    def software_info(self, master):
        gui.destroy_items(self.buttons_list, self.buttons_border_list)
        main_font = font.Font(size="14", family="Helvetica")
        self.myLabel = tk.Label(master, 
                        bg='white',
                        text="ICAAD Software is a assistant of instalation, \nconfiguration, administration of Active Directory \n\n http://www.github.com/alb3rtov/ICAAD-Software",
                        font = main_font)
        
        self.myLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        image2 = Image.open("img/back.png")
        image2 = image2.resize((30, 30), Image.ANTIALIAS)
        self.back_icon = ImageTk.PhotoImage(image2)
        self.back_button = tk.Button(master, image=self.back_icon, bg='white', relief='groove', borderwidth=0, cursor='hand2', command= lambda: self.go_back(master))
        self.back_button.place(x=40, y=530)