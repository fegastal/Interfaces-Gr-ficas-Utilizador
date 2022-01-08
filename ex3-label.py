from tkinter import *

raiz = Tk()
raiz.title('Label')
raiz.geometry('200x100')

#Cria e posiciona um frame
quadro = Frame(raiz)
quadro.pack()

etiqueta = Label(quadro, text='Olá Mundo!')
etiqueta.pack()

raiz.mainloop()