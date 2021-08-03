from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    Textfile.delete(1.0, END)
def openfile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes = [("All files", "*.*"), ("Text documents", "*.txt")])
    if file == "":
         file = None
    else:
        root.title(os.path.basename(file)+ " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt',defaultextension = ".txt", filetypes = [("All files", "*.*"), ("Text documents", "*.txt")])
        if file == "":
            None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)* " - Notepad")
            print("File saved")
    else:
        # save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END ))
        f.close()
    pass
    
    
def quitapp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
    
def copy():
    TextArea.event_generate(("<<Copy>>"))
    
def paste():
    TextArea.event_generate(("<<Paste>>"))
    pass
    
def about():
    showinfo("Notepad"," Notepad created by Amit Kumar Ram")

if __name__ == '__main__':
    root = Tk()
    root.title("Notepad")
    root.wm_iconbitmap("notes.icon.ico")
    root.geometry("644x788")
# add text area
    TextArea = Text(root, font = "lucida 13")
    file = None
    TextArea.pack(fill = BOTH, expand = True)
# lets create menubar
    Menubar = Menu(root)
    FileMenu = Menu(Menubar , tearoff = 0)

# to open new a menubar
    FileMenu.add_command(label = "New",command = newfile)
# to open already existing file
FileMenu.add_command(label = "Open", command = openfile)
# to save the current file

FileMenu.add_command(label = "Save", command = savefile)
FileMenu.add_separator()
FileMenu.add_command(label = "Exit", command = quitapp)
Menubar.add_cascade(label = "File", menu = FileMenu)
# File menu ends

# Edit menu starts
EditMenu = Menu(Menubar, tearoff = 0)
# to give a feaure of cut copy paste
EditMenu.add_command(label = "Cut", command = cut)
EditMenu.add_command(label = "Copy", command = copy)
EditMenu.add_command(label = "Paste", command = paste)
Menubar.add_cascade(label = "Edit", menu= EditMenu)
# EditMenu.add_cascade(label = "Exit", menu= quitapp)
root.config(menu = Menubar)
# Edit menu ends

# Help menu starts
Helpmenu = Menu(Menubar, tearoff = 0)
Helpmenu.add_command(label = "About Notepad", command = about)

Menubar.add_cascade(label = "Help", menu = Helpmenu)
root.config(menu = Menubar)
Scroll = Scrollbar(TextArea)
Scroll.pack(side = RIGHT, fill = Y)
Scroll.config(command = TextArea.yview)
TextArea.config(yscrollcommand = Scroll.set)


# Help menu ends
root.mainloop()