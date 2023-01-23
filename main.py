from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root=Tk()
root.geometry("394x444")
root.wm_iconbitmap("icon.ico")
root.title("Burger Notes")
#Functions
def myfunc():
    print("It's working")
def newMe():
    global file
    file=None
    root.title("Untitled - Burger Notes")
    text_area.delete(1.0,END)
def openMe():
    global file
    file=askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        f = open(file, "r")
        text_area.insert(1.0, f.read())
        f.close()

def saveMe():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()

    
def exitMe():
    print("The current file is destroyed")
    root.destroy()
#Edit menu
def cutMe():
    text_area.event_generate(("<<Cut>>"))
def copyMe():
    text_area.event_generate(("<<Copy>>"))
def pasteMe():
    text_area.event_generate(("<<Paste>>"))
    
#View Menu function
def aboutMe():
    msg.showinfo("About","This is GUI is created by Beacon Burgers")
def rateMe():
    ask=msg.askquestion("Rate","Is this GUI helpfull?")
    if ask=="yes":
        msg.showinfo("Rate","Thank You for using this GUI")
    else:
        msg.showinfo("Rate","We will Fix it")
#menu bar

Mainmenu=Menu(root)
#File Menu
m1=Menu(Mainmenu,tearoff=0)
m1.add_command(label="New",command=newMe)
m1.add_command(label="Open",command=openMe)
m1.add_command(label="Save",command=saveMe)
m1.add_separator()
m1.add_command(label="Exit",command=exitMe)

Mainmenu.add_cascade(label="File",menu=m1)
#Edit Menu
m2=Menu(Mainmenu,tearoff=0)
m2.add_command(label="Cut",command=cutMe)
m2.add_command(label="Copy",command=copyMe)
m2.add_command(label="Paste",command=pasteMe)

Mainmenu.add_cascade(label="Edit",menu=m2)
#View Menu
m3=Menu(Mainmenu,tearoff=0)
m3.add_command(label="About",command=aboutMe)
m3.add_command(label="Rate",command=rateMe)

Mainmenu.add_cascade(label="View",menu=m3)
root.config(menu=Mainmenu)

#text area
text_area=Text(root,font="lucida 13")
file=None
text_area.pack(expand=True,fill=BOTH)

#scrollbar 
Scroll=Scrollbar(text_area)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=Scroll.set)


root.mainloop()