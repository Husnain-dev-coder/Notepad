from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# Functions
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "."),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "."),
                                           ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))
            root.title(os.path.basename(file) + " - Notepad")
    else:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad", "Welcome to the Notepad application! This lightweight and user-friendly text editor is designed to help you quickly create, edit, and manage plain text files with ease.\n\nDeveloped with dedication by Husnain Raza.")

def wordCount():
    text = TextArea.get(1.0, END)
    words = len(text.split())
    showinfo("Word Count", f"Total Words: {words}")

def findReplace():
    find_window = Toplevel(root)
    find_window.title("Find & Replace")
    find_window.geometry("300x150")

    Label(find_window, text="Find: ").grid(row=0, column=0, padx=10, pady=5)
    Label(find_window, text="Replace: ").grid(row=1, column=0, padx=10, pady=5)

    find_input = Entry(find_window, width=20)
    replace_input = Entry(find_window, width=20)

    find_input.grid(row=0, column=1, padx=10, pady=5)
    replace_input.grid(row=1, column=1, padx=10, pady=5)

    def replaceText():
        text = TextArea.get(1.0, END)
        find_text = find_input.get()
        replace_text = replace_input.get()
        new_text = text.replace(find_text, replace_text)
        TextArea.delete(1.0, END)
        TextArea.insert(1.0, new_text)

    Button(find_window, text="Replace", command=replaceText).grid(row=2, column=1, pady=10)

# Main program
if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")

    # Text Area
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Menu Bar
    MenuBar = Menu(root)

    # File Menu
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    # Edit Menu
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    EditMenu.add_command(label="Find & Replace", command=findReplace)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # Tools Menu
    ToolsMenu = Menu(MenuBar, tearoff=0)
    ToolsMenu.add_command(label="Word Count", command=wordCount)
    MenuBar.add_cascade(label="Tools", menu=ToolsMenu)

    # Help Menu
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    # Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()