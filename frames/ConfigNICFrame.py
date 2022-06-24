import tkinter as tk
from PIL import ImageTk,Image
from tkinter import LEFT, ttk
import subprocess
import re

import gui
from frames import InitFrame

class ConfigNICFrame:
    """ Class of NIC configuration frame """
    def __init__(self, master):
        """ Creates the items that contains main frame """
        geometry = "500x600"
        master.geometry(geometry)
        res = geometry.split("x")

        self.list_entries1 = []
        self.list_entries2 = []
        self.list_entries3 = []
        self.list_entries4 = []
        self.list_all_entries = []
        self.address_labels = []
        self.address_dots = []
        self.list_positions_entries = [0,0,0,0]

        self.frame = tk.Frame(master, bg='white', width=300, height=300)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.canvas = tk.Canvas(self.frame, bg='white', bd=0, highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=282, height=400)

        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion= self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

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

    
    def on_mousewheel(self, event):
        """ Event for mousewheel in scrollbar menus """
        try:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        except:
            pass


    def validate(self, num_row, P):
        """ Validate address entry format """
        if len(P) == 0:
            return True
        elif len(P) == 3 and P.isdigit():
            for i in range(4):
                if self.list_positions_entries[int(num_row)] == i and i != 3:
                    self.list_all_entries[int(num_row)][i+1].focus()
                    self.list_positions_entries[int(num_row)] = i+1
                    break
            return True
        elif len(P) >= 1 and len(P) <= 3 and P.isdigit():
            return True
        else:
            return False

    
    def set_address_menu(self, frame, title, num_row, list_entries):
        """ Define field to set addresses """
        vcmd = (frame.register(self.validate), num_row, '%P')
        
        addr_label = tk.Label(frame, bg='white', text=title)
        addr_label.grid(pady=3, padx=30, row=num_row, column=0, sticky=tk.W)

        addr_entry1 = tk.Entry(frame, width= 5, bd=1.5, justify='center', validate="key", validatecommand=vcmd)
        addr_entry1.grid(pady=3, row=num_row, column=1)
        
        dot1_label = tk.Label(frame, bg='white', text=".")
        dot1_label.grid(pady=3, row=num_row, column=2)

        addr_entry2 = tk.Entry(frame, width= 5, bd=1.5, justify='center', validate="key", validatecommand=vcmd)
        addr_entry2.grid(pady=3, row=num_row, column=3)

        dot2_label = tk.Label(frame, bg='white', text=".")
        dot2_label.grid(pady=3, row=num_row, column=4)

        addr_entry3 = tk.Entry(frame, width= 5, bd=1.5, justify='center', validate="key", validatecommand=vcmd)
        addr_entry3.grid(pady=3, row=num_row, column=5)
        
        dot3_label = tk.Label(frame, bg='white', text=".")
        dot3_label.grid(pady=3, row=num_row, column=6)

        addr_entry4 = tk.Entry(frame, width= 5, bd=1.5, justify='center', validate="key", validatecommand=vcmd)
        addr_entry4.grid(pady=3, row=num_row, column=7)
        
        self.address_labels.append(addr_label)
        self.address_dots.extend([dot1_label, dot2_label, dot3_label])
        list_entries.append(addr_entry1)
        list_entries.append(addr_entry2)
        list_entries.append(addr_entry3)
        list_entries.append(addr_entry4)
        list_entries[0].focus()
    
    
    def get_address(self, list_entries):
        """ Get address of corresponding entries """
        return str(list_entries[0].get()) + "." + str(list_entries[1].get()) + "." + str(list_entries[2].get()) + "." + str(list_entries[3].get())

    
    def set_configuration(self, id): 
        """ Configure static address of a given NIC """      
        ip = self.get_address(self.list_entries1)
        mask = self.get_address(self.list_entries2)
        gateway = self.get_address(self.list_entries3)
        dns_server = self.get_address(self.list_entries4)
        
        args = [gui.g_list_nic[id], ip, mask, gateway, dns_server]
        p = subprocess.Popen(['powershell.exe', "-ExecutionPolicy", "Bypass", '.\\scripts\\nic_config.ps1'] + args, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
        gui.create_progress_bar("Executing command X.", p)

        for line in p.stdout:
            decoded_line = line.decode('utf-8', errors='replace').strip()
            clean_line = re.sub('\s+',' ', str(decoded_line))
            #print(clean_line)
        
        if clean_line == "True":
            tk.messagebox.showinfo(gui.g_list_nic[id], gui.g_list_nic[id] + " NIC has been configured successfully")
        else:
            tk.messagebox.showerror(gui.g_list_nic[id], "An error ocurred configuring " + gui.g_list_nic[id] + " NIC")
    
    def clear_all_fields(self):
        """ Clear all entries and restart positions """
        for i in range(len(self.list_all_entries)):
            for e in self.list_all_entries[i]:
                e.delete(0, tk.END)
            self.list_positions_entries[i] = 0
        
        self.list_all_entries[0][0].focus()

    
    def config_nic(self, master, id, res):
        """ Display frame for NIC configuration """
        self.destroy_all_items()

        frame = tk.Frame(master, bg='white', width=300, height=300)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #title_label = tk.Label(frame, bg='white', text= "Configuration of " +  gui.g_list_nic[id] + " NIC")
        #title_label.grid(pady=5, row=0, column=0)

        self.set_address_menu(frame, "IP address:", 0, self.list_entries1)
        self.set_address_menu(frame, "Subnet mask:", 1, self.list_entries2)
        self.set_address_menu(frame, "Default gateway:", 2, self.list_entries3)
        self.set_address_menu(frame, "DNS server:", 3, self.list_entries4)
        self.list_all_entries = [self.list_entries1, self.list_entries2, self.list_entries3, self.list_entries4]

        button1 = tk.Button(frame, text="OK", command = lambda: self.set_configuration(id))
        button1.grid(pady=5, row=5, column=0)

        button2 = tk.Button(frame, text="Clear all", command = lambda: self.clear_all_fields())
        button2.grid(pady=5, row=5, column=1)

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
        """ Destroy all items of this frame """
        gui.destroy_items(self.buttons_list, self.buttons_border_list)
        self.canvas.destroy()
        self.second_frame.destroy()
        self.scrollbar.destroy()
        self.frame.destroy()
        self.icon_label.destroy()

    def delete_config_menu(self):
        """ Delete all items of NIC config menu """
        for i in range(4):
            self.list_entries1[i].destroy()
            self.list_entries2[i].destroy()
            self.list_entries3[i].destroy()
            self.list_entries4[i].destroy()

        for labels in self.address_labels:
            labels.destroy()

        for dots in self.address_dots:
            dots.destroy()


    def go_back_config_nic(self, master):
        """ Back to config nic menu """
        self.delete_config_menu()
        self.destroy_all_items()
        
        e = ConfigNICFrame(master)

    
    def go_back(self, master):
        """ Delete items and create previous frame """
        self.destroy_all_items()
        e = InitFrame.InitFrame(master) 