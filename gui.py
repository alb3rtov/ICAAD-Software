import sys
import platform
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from PIL import ImageTk,Image

class MainFrame:
    def __init__(self, master):
        main_font = font.Font(size="12", family="Helvetica")

        self.button_border1 = tk.Frame(master, highlightbackground="gray87", highlightcolor="gray87", highlightthickness=2, bd=0)
        self.my_button1 = tk.Button(self.button_border1, activebackground='#e6f5ff', bg="white", width = 30, height = 3, text="What is ICAAD Software GUI?", relief='groove', borderwidth=0, font = main_font, command=self.software_info)
        self.button_border1.pack(pady=20)
        self.my_button1.pack()
        self.my_button1.bind("<Enter>", lambda e: self.my_button1.config(bg='#f7fcff'))
        self.button_border1.bind("<Enter>", lambda e: self.button_border1.config(highlightbackground="#538de6", highlightcolor="#538de6"))
        self.my_button1.bind("<Leave>", lambda e: self.my_button1.config(bg='white'))
        self.button_border1.bind("<Leave>", lambda e: self.button_border1.config(highlightbackground="gray87", highlightcolor="gray87"))

        self.button_border2 = tk.Frame(master, highlightbackground="gray87", highlightcolor="gray87", highlightthickness=2, bd=0)
        self.my_button2 = tk.Button(self.button_border2, activebackground='#e6f5ff', bg="white", width = 30, height = 3, text="Check operating system", relief='groove', borderwidth=0, font = main_font, command = self.check_system)
        self.button_border2.pack(pady=20)
        self.my_button2.pack()
        self.my_button2.bind("<Enter>", lambda e: self.my_button2.config(bg='#f7fcff'))
        self.button_border2.bind("<Enter>", lambda e: self.button_border2.config(highlightbackground="#538de6", highlightcolor="#538de6"))
        self.my_button2.bind("<Leave>", lambda e: self.my_button2.config(bg='white'))
        self.button_border2.bind("<Leave>", lambda e: self.button_border2.config(highlightbackground="gray87", highlightcolor="gray87"))

        self.button_border3 = tk.Frame(master, highlightbackground="gray87", highlightcolor="gray87", highlightthickness=2, bd=0)
        self.my_button3 = tk.Button(self.button_border3, activebackground='#e6f5ff' ,bg="white", width = 30, height = 3, text="Exit", relief='groove', font = main_font, borderwidth=0, command= lambda: self.exit_program(master))
        self.button_border3.pack(pady=20)
        self.my_button3.pack()
        self.my_button3.bind("<Enter>", lambda e: self.my_button3.config(bg='#f7fcff'))
        self.button_border3.bind("<Enter>", lambda e: self.button_border3.config(highlightbackground="#538de6", highlightcolor="#538de6"))
        self.my_button3.bind("<Leave>", lambda e: self.my_button3.config(bg='white'))
        self.button_border3.bind("<Leave>", lambda e: self.button_border3.config(highlightbackground="gray87", highlightcolor="gray87"))

    def exit_program(self, master):
        option = messagebox.askquestion("Exit program","Do yo want to exit?")
        if option == "yes":
            sys.exit();

    def software_info(self):
        top = tk.Toplevel()
        top.title("Software information")
        top.iconbitmap("img/icaad.ico")
        myLabel = tk.Label(top, text="ICAAD Software is a assistant of instalation, configuration, administration of Active Directory").pack()

    def check_system(self):
        if platform.system() == 'Windows':
            if platform.release() == "10" or platform.release() == "16" or platform.release() == "19":
                messagebox.showinfo("Check operating system","Version " + platform.system() + " " + platform.release() + " is correct")
                #delete items menu
                self.button_border1.destroy()
                self.my_button1.destroy()
                self.button_border2.destroy()
                self.my_button2.destroy()
                self.button_border3.destroy()
                self.my_button3.destroy()
                #create next menu

            else:
                messagebox.showwarning("Check operating system", "Must be a Windows version 2012/2016/2019 " + "\n(You have " + platform.system() + " " + platform.release() + ")")
        else:
            messagebox.showwarning("Check operating system", "Must be a Windows version 2012/2016/2019 " + "\n(You have " + platform.system() + " " + platform.release() + ")")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ICAAD Software")
    root.iconbitmap("img/icaad.ico")
    root.geometry("500x510")
    root.wm_minsize(400,440)
    root.configure(bg='white')
    
    main_icon = ImageTk.PhotoImage(Image.open("img/icaad.png"))
    icon_label = tk.Label(root, image=main_icon, bg='white').pack(anchor=tk.NW,padx=10,pady=10)

    image1 = Image.open("img/cmd.png")
    image1 = image1.resize((30, 30), Image.ANTIALIAS)
    cmd_icon = ImageTk.PhotoImage(image1)
    cmd_label = tk.Label(root, image=cmd_icon, bg='white').place(relx=0.85, rely=0.9)

    

    e = MainFrame(root)
    root.mainloop()
