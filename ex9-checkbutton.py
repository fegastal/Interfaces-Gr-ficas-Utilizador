from tkinter import *

raiz = Tk()
raiz.title('Checkbutton')

quadro = Frame(raiz)
quadro.pack()

botao_j = Checkbutton(quadro, text='Jazz')
botao_j.pack()

botao_r = Checkbutton(quadro, text='Rock')
botao_r.pack()

botao_p = Checkbutton(quadro, text='Pop')
botao_p.pack()

raiz.mainloop()