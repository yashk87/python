import tkinter as tkr
def donothing():
    filewin = tkr.Toplevel(root)
    button = tkr.Button(filewin, Text="Do nothing button")
    button.pack()
root = tkr.Tk()
menubar = tkr.Menu(root)
filemenu = tkr.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit())
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tkr.Menu(menubar, tearoff=0)
root.config(menu = menubar)
root.mainloop()

