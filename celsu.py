from tkinter import *

root = Tk()




root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)




lb1 = Label(root, fg='black', font='calibri 30')
lb2 = Label(root, fg='black', font='calibri 30')
lb3 = Label(root,  fg='black', font='calibri 30')
in1 = Entry (root, font= 'calibri 30')
in2 = Entry (root, font= 'calibri 305')
lb4 = Label(root, text='Label 1', bg='green', fg='black', font='calibri 30')
lb5 = Button(root, text='Label 1', bg='green', fg='black', font='calibri 30')


lb1.grid(row=0, column=0, sticky=NSEW)
lb2.grid(row=0, column=1, sticky=NSEW)
lb3.grid(row=1, column=0, sticky=NSEW)
lb4.grid(row=1, column=1, sticky=NSEW)
lb5.grid(row=1, column=1, sticky=NSEW)

root.mainloop()
