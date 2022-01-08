from tkinter import *

raiz = Tk()
raiz.title('Contador')

quadro = Frame(raiz)
quadro.pack()

conta = IntVar()
conta.set(0)

def inc_contador():
    conta.set(conta.get() + 1)

def dec_contador():
    conta.set(conta.get() -1)

def limpa_contador():
    conta.set(0)

etiqueta = Label(quadro, textvariable=conta)
etiqueta.pack()

botao_inc = Button(quadro, text='Incrementa', command=inc_contador)
botao_inc.pack(side=LEFT)

botao_dec = Button(quadro, text='Decrementa', command=dec_contador)
botao_dec.pack(side=LEFT)

botao_limpa = Button(quadro, text='Limpa', command=limpa_contador)
botao_limpa.pack(side=LEFT)

raiz.mainloop()
