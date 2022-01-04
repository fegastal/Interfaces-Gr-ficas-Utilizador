from tkinter import *
from math import *


class Calculadora(Frame):

    def __init__(self):
        super().__init__()
        self.master.title('Calculadora')
        self.pack()
        self._entrada = Entry(self, width=25, bg='yellow')
        self._entrada.bind("<Return>", (lambda evento: self._calcula()))
        self._entrada.pack(fill=BOTH)

        self._resultado = Label(self)
        self._resultado.pack()

        self._botao = Button(self, text='Limpa', command=self._limpa)
        self._botao.pack()

    def _calcula(self):
        valor = eval(self._entrada.get())
        self._resultado.configure(text='Resultado = ' + str(valor))

    def _limpa(self):
        self._entrada.delete(0, END)
        self._resultado.configure(text="")


if __name__ == '__main__':
    Calculadora()
    mainloop()
