from tkinter import *

raiz = Tk()
raiz.title('Scale')

escala_1 = Scale(raiz, from_=1, to=50, width=10)
escala_1.pack()

escala_2 = Scale(raiz, from_=1, to=100, sliderlength=15, resolution=5, orient=HORIZONTAL)
escala_2.pack()

raiz.mainloop()