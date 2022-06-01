from tkinter import *

#back-end
def soma():
    lb3['text']=(int(varX.get()) + int(varY.get()))

def subtrair():
   lb3['text']=(int(varX.get()) - int(varY.get()))   

def dividir():
   lb3['text']=(int(varX.get()) / int(varY.get()))  

def multiplicar():
   lb3['text']=(int(varX.get()) * int(varY.get()))   


#front
#window
janela = Tk()

#geometry
janela.geometry('400x300+500+500')
janela.minsize(width=900, height=500)

#widgets
lb0 = Label(janela, text='Calculadora', font='Arial 25')
lb1 = Label(janela, text='Valor Um', font='Arial 15')
varX = Entry(janela, font='Arial 10')
lb2 = Label(janela, text='Valor Dois', font='Arial 15')
varY = Entry(janela,  font='Arial 10')
lb3 = Label(janela, text='Resultado', font='Arial 20')
bt1 = Button(janela, text='Somar', font='Arial 15', command=soma)
bt2 = Button(janela, text='Subtrair', font='Arial 15', command=subtrair)
bt3 = Button(janela, text='Multiplicar', font='Arial 15', command=multiplicar)
bt4 = Button(janela, text='Dividir', font='Arial 15', command=dividir)

#layout
lb0.pack()
lb1.pack()
varX.pack()
lb2.pack()
varY.pack()
lb3.pack()
bt1.pack(side=LEFT)
bt2.pack(side=LEFT)
bt3.pack(side=LEFT)
bt4.pack(side=LEFT)

#RUN
janela.mainloop()