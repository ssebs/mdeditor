# pylint: disable=C0103,C0111,W0614,W0401,C0200,C0325,C1001
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
        

    def loadFile(self):
        filename = tkFileDialog.askopenfilename(initialdir=".", title="Select file", filetypes=(
            ("markdown files", "*.md"), ("all files", "*.*")))

    def saveFile(self):
        print "Save here"

    def getTitle(self):
        print self.title


### CODE ENTRY ###
root = Tk()
gui = Gui(root)
menubar = Menu(root)
text = Text(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=gui.loadFile)
filemenu.add_command(label="Save", command=gui.loadFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)


text.grid()

root.config(menu=menubar)
root.mainloop()



