from tkinter import *

raiz = Tk()
raiz.title('Contador')

quadro = Frame(raiz)
quadro.pack()

conta = IntVar()
conta.set(0)

def contador():
    conta.set(valor)

etiqueta = Label(quadro, textvariable=conta)
etiqueta.pack()

botao_inc = Button(quadro, text='Incrementa', command=(lambda:contador(conta.get() +1)))
botao_inc.pack(side=LEFT)

botao_dec = Button(quadro, text='Decrementa', command=(lambda:contador(conta.get() -1)))
botao_dec.pack(side=LEFT)

botao_limpa = Button(quadro, text='Limpa', command=(lambda:contador(0)))
botao_limpa.pack(side=LEFT)

raiz.mainloop()
