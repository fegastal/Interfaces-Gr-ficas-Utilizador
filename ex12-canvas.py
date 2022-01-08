from tkinter import *

raiz = Tk()

tela = Canvas(raiz, width=100, height=50)
tela.pack()

tela.create_rectangle(30, 30, 50, 50, fill='green')

raiz.mainloop()
