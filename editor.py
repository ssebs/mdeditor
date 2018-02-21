# pylint: disable=C0103,C0111,W0614,W0401,C0200,C0325,C1001,E1601
from Tkinter import *
import tkFileDialog

##
# mdeditor is a WYSIWYG Markdown editor
##


class Gui:
    def __init__(self, master):
        self.master = master
        self.title = "Markdown Editor"
        master.title(self.title)

        self.textArea = Text(master)
        self.textArea.grid()


    def loadFile(self):
        filename = tkFileDialog.askopenfilename(initialdir=".", title="Select file", filetypes=(
            ("Markdown file", "*.md"), ("all files", "*.*")))
        
    def saveFile(self):
        print("Save here")
        print("Content: " + self.textArea.get("1.0",END))

    def getTitle(self):
        print(self.title)

# End Gui Class


### CODE ENTRY ###
root = Tk()
gui = Gui(root)
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=gui.loadFile)
filemenu.add_command(label="Save", command=gui.saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)


root.config(menu=menubar)
root.mainloop()
