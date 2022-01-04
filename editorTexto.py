from tkinter import *
import tkinter.filedialog as dialog


def salva(raiz, texto):
    dados = texto.get('0.0', END)
    ficheiro = dialog.asksaveasfilename(parent=raiz, filetypes=[('text files', '.txt')])

    fich_saida = open(ficheiro, 'w')
    fich_saida.write(dados)
    fich_saida.close()


def sair(raiz):
    raiz.destroy()


if __name__ == '__main__':
    janela = Tk()
    texto = Text(janela)
    texto.pack()

    barra_menu = Menu(janela)
    ficheiro_menu = Menu(barra_menu)
    ficheiro_menu.add_command(label='Salvar', command=lambda: salva(janela, texto))
    ficheiro_menu.add_command(label='Terminar', command=lambda: salva(janela))
barra_menu.add_cascade(label='Ficheiro', menu=ficheiro_menu)

janela.configure(menu=barra_menu)
janela.mainloop()
