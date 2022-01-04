from tkinter import *


class Dado(Frame):

    def __init__(self):
        super().__init__()
        self.master.title('Lança Dado')
        self.pack(expand=YES, fill=BOTH)

        self._tela = Canvas(self, width=250, height=250)
        self._tela.pack(side=LEFT)

        self._botao = Button(self, text='Joga', command=self.joga)
        self._botao.pack(side=LEFT)

        self._carrega_imagens()
        self._id_imagem = self._tela.create_image(125, 125, image=self._imagens[0])

    def _carrega_imagens(self):
        self._imagens = [None] * 7
        for i in range(0, 7):
            nome_imagem = '~/' + 'dado' + str(i) + '.gif'
            self._imagens[i] = PhotoImage(file=nome_imagem)

    def joga(self):
        from random import randint
        i = randint(1, 6)
        self._id_imagem = self._tela.create_image(125, 125, image=self._imagens[i])


if __name__ == '__main__':
    Dado()
    mainloop()