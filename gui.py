import platform
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from PIL import ImageTk,Image

class MainFrame:
    def __init__(self, master):
        myFrame = tk.Frame(master)
        myFrame.pack()

        myFont = font.Font(size="10", family="Helvetica")

        self.myButton1 = tk.Button(master, bg="white", width = 30, height = 3, text="What is ICAAD Software GUI?", relief='groove', font = myFont, command=self.softwareInfo)
        self.myButton1.pack(pady=20)
        self.myButton1.bind("<Enter>", lambda e: self.myButton1.config(bg='gray87'))
        self.myButton1.bind("<Leave>", lambda e: self.myButton1.config(bg='white'))

        self.myButton2 = tk.Button(master,  bg="white", width = 30, height = 3, text="Check operating system", relief='groove', font = myFont, command = self.checkSystem)
        self.myButton2.pack(pady=20)
        self.myButton2.bind("<Enter>", lambda e: self.myButton2.config(bg='gray87'))
        self.myButton2.bind("<Leave>", lambda e: self.myButton2.config(bg='white'))

        self.myButton3 = tk.Button(master,  bg="white", width = 30, height = 3, text="Exit", relief='groove', font = myFont, command=master.quit)
        self.myButton3.pack(pady=20)
        self.myButton3.bind("<Enter>", lambda e: self.myButton3.config(bg='gray87'))
        self.myButton3.bind("<Leave>", lambda e: self.myButton3.config(bg='white'))

    def softwareInfo(self):
        top = tk.Toplevel()
        top.title("Software information")
        top.iconbitmap("img/icaad.ico")
        myLabel = tk.Label(top, text="ICAAD Software is a assistant of instalation, configuration, administration of Active Directory").pack()

    def checkSystem(self):
        if platform.system() == 'Windows':
            if platform.release() == "12" or platform.release() == "16" or platform.release() == "19":
                messagebox.showinfo("Check operating system","Version " + platform.system() + " " + platform.release() + " is correct")
            else:
                messagebox.showwarning("Check operating system", "Must be a Windows version 2012/2016/2019 " + "\n(You have " + platform.system() + " " + platform.release() + ")")
        else:
            messagebox.showwarning("Check operating system", "Must be a Windows version 2012/2016/2019 " + "\n(You have " + platform.system() + " " + platform.release() + ")")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ICAAD Software")
    root.iconbitmap("img/icaad.ico")
    root.geometry("400x400")

    e = MainFrame(root)
    root.mainloop()
