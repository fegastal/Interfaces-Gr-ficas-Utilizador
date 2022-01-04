from tkinter import *


class Demo(Frame):
    """Clicar com o botão esquerdo do rato na janela."""
    def __init__(self):
        super().__init__()
        self.master.title('Demo')
        self.pack(expand=YES, fill=BOTH)

        self.tela = Canvas(self, width=250, height=150, bg='light yellow')
        self.tela.bind('<Button-1>', self._desenha)
        self.tela.pack(expand=YES, fill=BOTH)

        self.frase = Label(self, bg='gray')
        self.frase.pack(expand=YES, fill=BOTH)

    def _ponteiro(self, evento):
        self.frase.configure(text='Rato pressionado: X = ' + str(evento.x) + ', Y = ' + str(evento.y))


if __name__ == ' main ':
    Demo()
    mainloop()
