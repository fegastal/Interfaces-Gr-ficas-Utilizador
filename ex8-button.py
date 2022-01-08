from tkinter import *

raiz = Tk()
raiz.title('Dados')

quadro = Frame(raiz)
quadro.pack()

botao = Button(quadro, text='Lança Dado')
botao.pack()

raiz.mainloop()