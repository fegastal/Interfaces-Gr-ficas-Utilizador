from tkinter import *

class JogoDoGalo:

    def __init__(self):
        super().__init__()
        joga_o = JogadorO()
        joga_x = JogadorX()
        self._jogo = Jogo(joga_o, joga_x)
        self._ecran = Ecran(self._jogo)
        self._jogador = self._jogo.obtem_jogador()


class Ecran:
    """Classe onde defino a interface."""

    def __init__(self, jogo):
        super().__init__()
        self._jogo = jogo
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Jogo do Galo')

        self.quadro1=Canvas(self, width=450, height=450, bg='light yellow')
        self.quadro1.pack(side=TOP, padx=20, pady=20)
        self.quadro1.create_line(150, 0, 150, 450, fill='red', width=3)
        self.quadro1.create_line(300, 0, 300, 450, fill='red', width=3)
        self.quadro1.create_line(0, 150, 450, 150, fill='red', width=3)
        self.quadro1.create_line(0, 300, 450, 300, fill='red', width=3)

        self.quadro2 = Frame(self)
        self.quadro2.pack(padx=20, pady=20, fill=BOTH)

        self.butao1 = Button(self.quadro2, text='Novo Jogo', command=self._novo_jogo)
        self.butao1.pack(side=LEFT)

        self.butao2 = Button(self.quadro2, text='Sair', command=self._termina)
        self.butao2.pack(side=RIGHT)

        self._jogador = StringVar()
        self._jogador.set('Joga: ' + self._jogo.obtem_jogador())
        self.quadro3 = Label(self, bg='gray', textvariable=self._jogador)
        self.quadro3.pack(padx=20, pady=20, fill=BOTH)

        self.quadro1.bind("<Button-1>", self.jogar)

    def jogar(self, evento):
        self._erro = False
        mensagem = 'Posição já ocupada...'
        posx = evento.x
        posy = evento.y
        x, y = self.quadrante(posx, posy)

        if self._jogo.livre(x, y):
            self._jogo.define_estado(posx, posy)
            self._desenha(x * 150 + 75, y * 150 + 75)

        else:
            print ('Oops!', mensagem)
            self._erro = True

        if not self._erro:

            if self._jogo.vencedor():
                print('Uau!', 'Ganhou %s' % self._jogo.obtem_jogador())
            else:
                self._jogo.muda_jogador()
                self._jogador.set('Joga: ' + self._jogo.obtem_jogador())
        else:
            self._erro = False

    def _desenha(self, x, y):
        if isinstance (self._jogo.obtem_tipo_jogador(), JogadorO):
            self.quadro1.create_oval(x-50, y-50, x+50, y+50, fill='green', width=3)

        else:
            self.quadro1.create_line(x-50, y-50, x+50, y+50, fill='green', width=3)
            self.quadro1.create_line(x-50, y+50, x+50, y-50, fill='green', width=3)


class Jogo:

    def __init__(self, joga_o, joga_x, livre=0):
        self._jogador_o = joga_o
        self._jogador_x = joga_x
        self._jogador = self._jogador_x
        self._livre = livre
        self._grelha = [[self._livre] * 3 for i in range(3)]

    def obtem_tipo_jogador(self):
        return self._jogador

    def obtem_jogador(self):
        return self._jogador.obtem_id()

    def obtem_grelha(self):
        return self._grelha

    def obtem_estado(self, i, j):
        return self._grelha[i][j]

    def define_estado(self, i, j):
        self._grelha[i][j] = self.obtem_jogador()

    def muda_jogador(self):
        if isinstance(self._jogador, JogadorO):
            self._jogador = self._jogador_x
        else:
            self._jogador = self._jogador_o

    def livre(self, i, j):
        return self._grelha[i][j] == self._livre

    def vencedor(self):
        trios = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
        ]

        jogador = self.obtem_jogador()
        resultado = False
        for trio in trios:
            resultado = reduce(and_, [self.obtem_estado(*elem) == jogador
        for elem in trio])
        if resultado:
            return True
        return False

    def novo_jogador(self):
        self._jogador = self._jogador_x
        self._grelha = [[0] * 3 for i in range(3)]