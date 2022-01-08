from tkinter import *

raiz = Tk()
raiz.title('Radiobutton')

quadro = Frame(raiz)
quadro.pack()

var = InterVar()

botao_m = Radiobutton(quadro, text='Masculino', variable=var, value=1)
botao_m.pack()

botao_f = Radiobutton(quadro, text='Feminino', variable=var, value=2)
botao_f.pack()

raiz.mainloop()