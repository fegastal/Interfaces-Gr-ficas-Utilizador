from tkinter import *

raiz = Tk()
raiz.title('Canvas')

tela = Canvas(raiz, width=200, height=200)
tela.pack()
tela.master.title('As de Espadas')

imagem = PhotoImage(file='~/1s.gif')

id_imagem = tela.create_image(100, 100, image = imagem)

raiz.mainloop()
