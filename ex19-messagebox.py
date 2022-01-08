from tkinter import *
from tkinter.messagebox import *

raiz = Tk()
raiz.title('Messagebox')

quadro = Frame(raiz)
quadro.pack()

conta = IntVar()
conta.set(0)

mensagem = 'Impossível decrementar!'

def contador(valor):
    conta.set(valor)

etiqueta = Label(quadro, textvariable=conta)
etiqueta.pack()

botao_inc = Button(quadro, text='Incrementa', command=(lambda:contador(conta.get() +1)))
botao_inc.pack(side=LEFT)

botao_dec = Button(quadro, text='Decrementa', command=(lambda:contador(conta.get() -1) if (conta.get() > 0 ) else showerror('Decrementa', mensagem)))
botao_dec.pack(side=LEFT)

botao_limpa = Button(quadro, text='Limpa', command=(lambda:contador(0)))
botao_limpa.pack(side=LEFT)

raiz.mainloop()
