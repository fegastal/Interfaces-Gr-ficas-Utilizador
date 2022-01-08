from tkinter import *

raiz = Tk()
raiz.title('Label')
raiz.geometry('200x100')

fonte = ('helvetica', 24, 'underline italic')

etiqueta = Label(quadro, text='Olá Mundo!')

etiqueta.configure(bg='red', fg='green')
etiqueta.configure(font=fonte, height=3, width=15)
etiqueta.configure(bd=10, relief=RAISED)

etiqueta.pack(expand=YES)
raiz.mainloop()