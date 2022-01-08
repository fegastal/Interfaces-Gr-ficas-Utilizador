from tkinter import *

raiz = Tk()
raiz.title('Label')
raiz.geometry('200x100')

fonte = ('helvetica', 24, 'bold')

etiqueta = Label(quadro, text='Olá Mundo!')

etiqueta.configure(font=fonte, height=3, width=15)
etiqueta.configure(font=fonte, height=3, width=15)
etiqueta.pack()

raiz.mainloop()