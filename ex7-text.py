from tkinter import *

raiz = Tk()
raiz.title('Entry')

quadro = Frame(raiz)
quadro.pack()

texto = Text(quadro, width=40, height=5, wrap=WORD)
texto.pack()

raiz.mainloop()