from tkinter import *


class Contador(Frame):
    def inc_contador(self):
        self._estado.set(self._estado.get() + 1)

    def __init__(self):
        super().__init__()
        self.master.title('Contador')
        self.pack(expand=YES, fill=BOTH)

        self._estado = IntVar()
        self._estado.set(0)

        self._etiqueta = Label(self, textvariable=self._estado)
        self._etiqueta.pack()

        self._botao_1 = Button(self, text='Incrementa', command=self.inc_contador)
        self._botao_1.pack(side=LEFT)

        self._botao_2 = Button(self, text='Terminar', command=self.master.destroy)
        self._botao_2.pack(side=LEFT)


if __name__ == '__main__':
    Contador()
    mainloop()