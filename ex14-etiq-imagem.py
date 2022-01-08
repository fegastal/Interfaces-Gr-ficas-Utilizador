from tkinter import *

raiz = Tk()
raiz.title('As de Espadas')
imagem = PhotoImage(file='~/1s.gif')

etiq_imagem = Label(raiz, image = imagem)
etiq_imagem.pack()

raiz.mainloop()
