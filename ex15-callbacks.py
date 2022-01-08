from tkinter import *

raiz = Tk()
raiz.title('Contador')

quadro = Frame(raiz)
quadro.pack()

conta = IntVar()
conta.set(0)

def inc_contador():
    conta.set(conta.get() + 1)

etiqueta = Label(quadro, textvariable=conta)
etiqueta.pack()

botao = Button(quadro, text='Contar', command=inc_contador)
botao.pack()

raiz.mainloop()
