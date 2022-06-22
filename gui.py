import subprocess
import time
import platform
import re
import tkinter.font as font
from tkinter import ttk

from PIL import ImageTk,Image
from frames.InitFrame import *

# Global variables
g_list_nic = []
g_dict_osinfo = {}
g_suitable_os = ["Microsoft Windows Server 2012",
                "Microsoft Windows Server 2016",
                "Microsoft Windows Server 2019",
                "Microsoft Windows Server 2022",
                "Microsoft Windows 10"]

# Main funtions
# Delete all items of the frame
def destroy_items(buttons_list, buttons_border_list):
    for index in range(0, len(buttons_list)):
        buttons_list[index].destroy()
        buttons_border_list[index].destroy()

# Search in suitable OS list
def check_os_list():
    suitable_os = False

    for os in range(len(g_suitable_os)):
        if g_suitable_os[os] in g_dict_osinfo["OsName"]:
            suitable_os = True
            break
    
    return suitable_os

# Create new next frame menu if system is Windows Server
def check_os(master):
    suitable_os = False
    if (check_os_list()):
        messagebox.showinfo("Check operating system","Version " + g_dict_osinfo["OsName"] + " is valid")
        suitable_os = True
    else:
        messagebox.showwarning("Check operating system", "Must be a Windows version 2012/2016/2019/2022 " + "\n(You have " + g_dict_osinfo["OsName"] + ")")

    return suitable_os

# Check if the system is Windows Server
def check_system(master):
    suitable_os = False

    if len(g_dict_osinfo) == 0:
        if platform.system() == 'Windows':
            # Create background subprocess for cmdlet
            p = subprocess.Popen(['powershell.exe', "-ExecutionPolicy", "Bypass", '.\\scripts\\osinfo.ps1'], stdout=subprocess.PIPE, stderr= subprocess.PIPE)
        
            # Create progress bar
            create_progress_bar("Executing command Get-ComputerInfo.", p)

            skip_title = 0
            for line in p.stdout:
                if len(line) > 2:
                    # Decode line format
                    decoded_line = line.decode('utf-8', errors='strict').strip()
                    clean_line = re.sub('\s+',' ', str(decoded_line))
                    
                    key = clean_line.split()[0]
                    g_dict_osinfo[key] = clean_line.partition(' ')[2]

                else:
                    skip_title += 1

            suitable_os = check_os(master)
        else:
            messagebox.showwarning("Check operating system", "Must be a Windows version 2012/2016/2019/2022 " + "\n(You have " + g_dict_osinfo["OsName"] + ")")
    else:
        suitable_os = check_os(master)

    return suitable_os

def get_nics(master):
    if len(g_list_nic) == 0:
        p = subprocess.Popen(['powershell.exe', "-ExecutionPolicy", "Bypass", '.\\scripts\\nics.ps1'], stdout=subprocess.PIPE, stderr= subprocess.PIPE)
        
        # Create progress bar
        create_progress_bar("Executing command Get-NetAdapter.", p)

        skip_title = 0
        for line in p.stdout:
            if len(line) > 2 and skip_title >= 3:
                decoded_line = line.decode('utf-8', errors='replace').strip()
                clean_line = re.sub('\s+',' ', str(decoded_line))

                #print(clean_line)
                g_list_nic.append(clean_line)

            else:
                skip_title += 1

# Create generic progress bar
def create_progress_bar(text, p):
    top = tk.Toplevel()
    top.resizable(False, False)
    top.geometry("400x80")
                
    top.title("Checking OS information")
    top.iconbitmap("img/icaad.ico")
    lbl = tk.Label(top, text= text, bg='white', fg='#707070')
    lbl.pack(pady=10)
    s = ttk.Style()
    s.theme_use("winnative")
    s.configure("blue.Horizontal.TProgressbar",troughcolor='#f2f2f2', foreground='white', background='#0077d1')
    progress_bar = ttk.Progressbar(top, style="blue.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=300, mode="indeterminate")
    progress_bar.pack()
                
    cnt = 0
                
    # Show progress bar while cmdlet is running
    while (p.poll() is None):
                    
        if progress_bar['value'] == 100:
            progress_bar['value'] = 0
        else: 
            progress_bar['value'] += 5%100

            if progress_bar['value']%25 == 0:
                if cnt == 2:
                    lbl['text'] = lbl['text'][:-2]
                    cnt = 0
                else:
                    lbl['text'] += "."
                    cnt += 1

        top.update_idletasks()
        time.sleep(0.125)

    top.destroy()

# Create a generic button
def create_button(master, button_name):
    main_font = font.Font(size="13", family="Helvetica")

    button_border = tk.Frame(master, 
                        highlightbackground="gray87", 
                        highlightcolor="gray87", 
                        highlightthickness=2, 
                        bd=0)
    button = tk.Button(button_border,
                        activebackground='#e6f5ff', 
                        bg="white", width = 30, 
                        height = 3, text=button_name, 
                        relief='groove', 
                        borderwidth=0, 
                        font = main_font)
                        
    button.bind("<Enter>", lambda e: button.config(bg='#f7fcff'))
    button_border.bind("<Enter>", lambda e: button_border.config(highlightbackground="#538de6", highlightcolor="#538de6"))
    button.bind("<Leave>", lambda e: button.config(bg='white'))
    button_border.bind("<Leave>", lambda e: button_border.config(highlightbackground="gray87", highlightcolor="gray87"))

    return button_border, button

# Runs cmd.py and destroy GUI frame
def open_cmd(root):
    option = messagebox.askquestion("CMD Version","Do you want to open ICAAD CMD version?")
    if option == "yes":
        root.destroy()
        subprocess.run(["python.exe","cmd.py"])

# Define and create main frame
def main():
    root = tk.Tk()
    root.title("ICAAD Software")
    root.iconbitmap("img/icaad.ico")
    #root.wm_minsize(435,450)
    root.resizable(False, False)
    root.configure(bg='white')

    main_icon = ImageTk.PhotoImage(Image.open("img/icaad.png"))
    icon_label = tk.Label(root, image=main_icon, bg='white').place(x=13, y=13)

    e = InitFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()