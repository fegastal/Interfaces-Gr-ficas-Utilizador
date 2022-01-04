from tkinter import *


class Animacao(Frame):
    
    def __init__(self):
        super().__init__()
        self.master.title('Texto que se move.')

        self._tela = Canvas(self.master, width=300, height=50)
        self._tela.pack()
        self._width = 300

        x = 0
        self._tela.create_text(x, 25, text='Fernanda Gastal', tags='text')
        delta_x = 3
        while True:
            self._tela.move('text', delta_x, 0)
            self._tela.after(100)
            self._tela.update()
            if x < self._width:
                x += delta_x
            else:
                x = 0
                self._tela.delete('text')
                self._tela.create_text(x, 25, text='Fernanda Gastal', tags='text')


if __name__ == '__main__':
    Animacao()
    mainloop()

