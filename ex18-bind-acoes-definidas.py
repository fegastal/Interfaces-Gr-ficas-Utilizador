from tkinter import *

def ola(evento):
    print('Carpe diem...')

def termina(evento):
    print('E acabou...')
    import sys
    sys.exit()

def muda_linha(evento):
    print('E mudo de linha...')

raiz = Tk()

botao = Button(raiz, text='Testa Ligação')
botao.pack(expand=YES, fill=BOTH)
botao.bind('<Button-1>', ola)
botao.bind('<Double-1>', termina)

texto = Text(raiz)
texto.pack()

texto.bind('<Return>', muda_linha)
raiz.mainloop()
