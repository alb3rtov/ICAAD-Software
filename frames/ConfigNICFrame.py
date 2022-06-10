import tkinter as tk
import re
from PIL import ImageTk,Image
from tkinter import VERTICAL, ttk

import gui
from frames import InitFrame

class ConfigNICFrame:
    def __init__(self, master):
        geometry = "500x600"
        master.geometry(geometry)
        res = geometry.split("x")
        
        self.frame = tk.Frame(master, bg='white', width=300, height=300)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.canvas = tk.Canvas(self.frame, bg='white', bd=0, highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=282, height=400)

        self.scrollbar = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion= self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.second_frame = tk.Frame(self.canvas, bg='white')
        x0 = self.second_frame.winfo_screenwidth()/2
        y0 = self.second_frame.winfo_screenheight()/2
        self.canvas.create_window((x0,y0), window=self.second_frame, anchor="center")
        
        self.main_icon = ImageTk.PhotoImage(Image.open("img/icaad.png"))
        self.icon_label = tk.Label(master, image=self.main_icon, bg='white')
        self.icon_label.place(x=13, y=13)

        self.buttons_list = []
        self.buttons_border_list = []
        
        for i in range(len(gui.g_list_nic)):
            self.button_border, self.button = gui.create_button(self.second_frame, gui.g_list_nic[i])
            self.button.configure(command = lambda i=i: self.config_nic(master, i, res))
            self.button_border.grid(column=0, row=i, pady=20)
            self.button.grid(column=0, row=i)
            
            self.buttons_border_list.append(self.button_border)
            self.buttons_list.append(self.button)
        
        image2 = Image.open("img/back.png")
        image2 = image2.resize((30, 30), Image.ANTIALIAS)
        self.back_icon = ImageTk.PhotoImage(image2)
        self.back_button = tk.Button(master, image=self.back_icon, bg='white', relief='groove', borderwidth=0, cursor='hand2', command= lambda: self.go_back(master))
        self.back_button.place(x=40, y=int(res[1])-70)
        self.back_button_border = tk.Frame()

        image1 = Image.open("img/cmd.png")
        image1 = image1.resize((30, 30), Image.ANTIALIAS)
        self.cmd_icon = ImageTk.PhotoImage(image1)
        self.cmd_button = tk.Button(master, image=self.cmd_icon, bg='white', relief='groove', borderwidth=0, cursor='hand2', command= lambda: gui.open_cmd(master))
        self.cmd_button.place(x=430,y=int(res[1])-70)
        self.cmd_button_border = tk.Frame()

        self.buttons_border_list.append(self.back_button_border)
        self.buttons_list.append(self.back_button)
        self.buttons_border_list.append(self.cmd_button_border)
        self.buttons_list.append(self.cmd_button)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    # Display frame for NIC configuration
    def config_nic(self, master, id, res):
        self.destroy_all_items()

        frame = tk.Frame(master, bg='white', width=300, height=300)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        title_label = tk.Label(frame, font=("Helvetica", 15), bg='white', text= "Configuration of " +  gui.g_list_nic[id] + " NIC")
        title_label.pack()

        ip_addr_label = tk.Label(frame, font=("Helvetica", 15), bg='white', text="IP Address")
        ip_addr_label.pack()

        ip_addr_entry = tk.Entry(frame)
        ip_addr_entry.pack()

        button = tk.Button(frame, text="button", command = lambda: print(ip_addr_entry.get()))
        button.pack()

        image2 = Image.open("img/back.png")
        image2 = image2.resize((30, 30), Image.ANTIALIAS)
        self.back_icon = ImageTk.PhotoImage(image2)
        self.back_button = tk.Button(master, image=self.back_icon, bg='white', relief='groove', borderwidth=0, cursor='hand2', command= lambda: self.go_back_config_nic(master))
        self.back_button.place(x=40, y=int(res[1])-70)
        self.back_button_border = tk.Frame()

        image1 = Image.open("img/cmd.png")
        image1 = image1.resize((30, 30), Image.ANTIALIAS)
        self.cmd_icon = ImageTk.PhotoImage(image1)
        self.cmd_button = tk.Button(master, image=self.cmd_icon, bg='white', relief='groove', borderwidth=0, cursor='hand2', command= lambda: gui.open_cmd(master))
        self.cmd_button.place(x=430,y=int(res[1])-70)
        self.cmd_button_border = tk.Frame()

        self.buttons_border_list.append(self.back_button_border)
        self.buttons_list.append(self.back_button)
        self.buttons_border_list.append(self.cmd_button_border)
        self.buttons_list.append(self.cmd_button)

    def destroy_all_items(self):
        gui.destroy_items(self.buttons_list, self.buttons_border_list)
        self.canvas.destroy()
        self.second_frame.destroy()
        self.scrollbar.destroy()
        self.frame.destroy()
        self.icon_label.destroy()

    def go_back_config_nic(self, master):
        self.destroy_all_items()
        e = ConfigNICFrame(master)

    # Delete items and create previous frame
    def go_back(self, master):
        self.destroy_all_items()
        e = InitFrame.InitFrame(master) 