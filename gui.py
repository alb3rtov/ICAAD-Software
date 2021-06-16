import subprocess
from PIL import ImageTk,Image
from frames.InitFrame import *

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
                        
    button_border.pack(pady=20)
    button.pack()
    button.bind("<Enter>", lambda e: button.config(bg='#f7fcff'))
    button_border.bind("<Enter>", lambda e: button_border.config(highlightbackground="#538de6", highlightcolor="#538de6"))
    button.bind("<Leave>", lambda e: button.config(bg='white'))
    button_border.bind("<Leave>", lambda e: button_border.config(highlightbackground="gray87", highlightcolor="gray87"))

    return button_border, button

def open_cmd():
    option = messagebox.askquestion("CMD Version","Do you want to open ICAAD CMD version?")
    if option == "yes":
        root.destroy()
        subprocess.run(["python.exe","cmd.py"])

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ICAAD Software")
    root.iconbitmap("img/icaad.ico")
    root.geometry("500x510")
    root.wm_minsize(400,450)
    root.configure(bg='white')
    
    main_icon = ImageTk.PhotoImage(Image.open("img/icaad.png"))
    icon_label = tk.Label(root, image=main_icon, bg='white').pack(anchor=tk.NW,padx=10,pady=10)

    image1 = Image.open("img/cmd.png")
    image1 = image1.resize((30, 30), Image.ANTIALIAS)
    cmd_icon = ImageTk.PhotoImage(image1)
    cmd_button = tk.Button(root, image=cmd_icon, bg='white', relief='groove', borderwidth=0, cursor='hand2', command= open_cmd).place(relx=0.85, rely=0.9)

    e = InitFrame(root)
    root.mainloop()