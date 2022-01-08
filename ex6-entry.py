from tkinter import *

raiz = Tk()
raiz.title('Entry')

etiqueta = Label(raiz, text='Nome:')
etiqueta.pack(side=LEFT)

nome_entrada = StringVar()
nome_entrada.set('Nome')

nome = Entry(raiz, textvariable=nome_entrada)
nome.pack(side=LEFT)

raiz.mainloop()