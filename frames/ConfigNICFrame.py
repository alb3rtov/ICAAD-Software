import tkinter as tk
import re
import gui
from frames import InitFrame

class ConfigNICFrame:
    def __init__(self, master):
        self.nc_list = gui.g_dict_osinfo["CsNetworkAdapters"].split(", ")
        
        # Clean NIC name
        for nc in range(len(self.nc_list)):
            self.nc_list[nc] = re.sub('[{}]','',self.nc_list[nc])

        geometry = "500x" + str(300+100*len(self.nc_list))
        master.geometry(geometry)

        frame = tk.Frame(master, bg='white', width=300, height=300)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
        self.buttons_list = []
        self.buttons_border_list = []

        for i in range(len(self.nc_list)):
            self.button_border, self.button = gui.create_button(frame, self.nc_list[nc])
            self.button.configure(command = lambda: self.config_nic(i))
            self.button_border.grid(column=0, row=i, pady=20)
            self.button.grid(column=0, row=i)

            self.buttons_border_list.append(self.button_border)
            self.buttons_list.append(self.button)

        self.back_button_border, self.back_button = gui.create_button(frame, "Back")
        self.back_button.configure(command = lambda: self.go_back(master))
        self.back_button_border.grid(column=0, row=i+1,pady=20)
        self.back_button.grid(column=0, row=i+1)

        self.buttons_border_list.append(self.back_button_border)
        self.buttons_list.append(self.back_button)

    # Display frame for NIC configuration
    def config_nic(self, id):
        print("I'm a NIC " + self.nc_list[id])

    # Delete items and create previous frame
    def go_back(self, master):
        gui.destroy_items(self.buttons_list, self.buttons_border_list)  
        e = InitFrame.InitFrame(master) 