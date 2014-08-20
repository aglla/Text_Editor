#Basic Text Editor built with tkinter with some features such as: save, open, clear, copy, paste, word count
#A.G.
#July 14, 2014

from tkinter import *
import tkinter.filedialog as tk
import tkinter.messagebox as tk2

class Application(Frame):
    
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.text1 = Text(width = 20, height = 20)
        self.text1.pack(expand=YES, fill=BOTH)         #to make the textbox fill entire window

        menubar = Menu(self)
        filemenu = Menu(menubar)
        editmenu = Menu(menubar)
        toolsmenu = Menu(menubar)
        filemenu.add_command(label = 'New', command = self.newDoc)
        filemenu.add_command(label = 'Save', command = self.saveDoc)
        filemenu.add_command(label = 'Open', command = self.openDoc)
        editmenu.add_command(label = 'Copy', command = self.copy)
        editmenu.add_command(label = 'Paste', command = self.paste)
        editmenu.add_command(label = 'Clear', command = self.clear)
        toolsmenu.add_command(label = 'Word Count', command = self.wordCount)
        menubar.add_cascade(label = 'File', menu = filemenu)
        menubar.add_cascade(label = 'Edit', menu = editmenu)
        menubar.add_cascade(label = 'Tools', menu = toolsmenu)
        root.config(menu=menubar)

    def newDoc(self):
        if(tk2.askyesno("Message", "Unsaved work will be lost. Continue?")):
            self.text1.delete("1.0", END)        

    def saveDoc(self):
        savefile = tk.asksaveasfile(mode = 'w', defaultextension = ".txt")
        text2save = str(self.text1.get("1.0", END))
        savefile.write(text2save)
        savefile.close()
        
        
    def openDoc(self):
        openfile = tk.askopenfile(mode = 'r')
        text = openfile.read()
        self.text1.insert(END, text)
        openfile.close()

    def copy(self):
        #Copy the selected text into the clipboard
        var = str(self.text1.get(SEL_FIRST,SEL_LAST))
        self.clipboard_clear()
        self.clipboard_append(var)
    

    def paste(self):
        #Insert the clipboard text into the textbox
        result = self.selection_get(selection = "CLIPBOARD")   #get text from clipboard
        self.text1.insert("1.0", result)

    def clear(self):
        self.text1.delete("1.0", END)

    def wordCount(self):
        #Get text from textbox and split it by whitespace characters into a list. Then find length of list
        userText = self.text1.get("1.0", END)
        wordList = userText.split()
        number_of_words = len(wordList)
        tk2.showinfo('Word Count', 'Words:  ' + str(number_of_words))

root = Tk()
root.title('Text Editor')
root.geometry('700x600')
app = Application(root)
app.mainloop()
        
        
