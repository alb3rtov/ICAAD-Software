import subprocess
import tkinter.font as font
from tkinter import ttk

from PIL import ImageTk,Image
from frames.InitFrame import *

# Global variables
g_dict_osinfo = {}

# Main funtions

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
    main_font = font.Font(size="12", family="Helvetica")

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
    root.geometry("500x520")
    #root.wm_minsize(435,450)
    root.resizable(False, False)
    root.configure(bg='white')

    main_icon = ImageTk.PhotoImage(Image.open("img/icaad.png"))
    icon_label = tk.Label(root, image=main_icon, bg='white').place(x=13, y=13)

    image1 = Image.open("img/cmd.png")
    image1 = image1.resize((30, 30), Image.ANTIALIAS)
    cmd_icon = ImageTk.PhotoImage(image1)
    cmd_button = tk.Button(root, image=cmd_icon, bg='white', relief='groove', borderwidth=0, cursor='hand2', command= lambda: open_cmd(root)).place(relx=0.85, rely=0.9)

    e = InitFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()