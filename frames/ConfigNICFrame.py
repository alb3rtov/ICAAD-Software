import tkinter as tk
import re
from PIL import ImageTk,Image

import gui
from frames import InitFrame

class ConfigNICFrame:
    def __init__(self, master):
        self.nc_list = gui.g_dict_osinfo["CsNetworkAdapters"].split(", ")
        
        # Clean NIC name
        for nc in range(len(self.nc_list)):
            self.nc_list[nc] = re.sub('[{}]','',self.nc_list[nc])

        geometry = "500x" + str(200+100*len(self.nc_list))
        master.geometry(geometry)
        res = geometry.split("x")

        frame = tk.Frame(master, bg='white', width=300, height=300)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
        self.buttons_list = []
        self.buttons_border_list = []
    
        for i in range(len(self.nc_list)):
            self.button_border, self.button = gui.create_button(frame, self.nc_list[i])
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

    # Display frame for NIC configuration
    def config_nic(self, master, id, res):
        gui.destroy_items(self.buttons_list, self.buttons_border_list)
        
        frame = tk.Frame(master, bg='white', width=300, height=300)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        title_label = tk.Label(frame, font=("Helvetica", 15), bg='white', text= "Configuration of " +  self.nc_list[id] + " NIC")
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

    def go_back_config_nic(self, master):
        gui.destroy_items(self.buttons_list, self.buttons_border_list)  
        e = ConfigNICFrame(master)

    # Delete items and create previous frame
    def go_back(self, master):
        gui.destroy_items(self.buttons_list, self.buttons_border_list)  
        e = InitFrame.InitFrame(master) 