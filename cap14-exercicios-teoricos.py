'''
Exercícios Teóricos | Capítulo 14

1) Que diferenças existem entre o modelo convencional de programação e a programação guiada a eventos?

Programação Convencional: programas são decompostos em "passos" de processamento que executam operações complexas.
Rotinas são usadas como unidades de modularização para definir tais "passos" de processamento.
Exemplos: Pascal e C possuem linguagem com esse paradigma.

Programação Guiada a Eventos: É quando você escreve código para responder a eventos.
Na programação orientada a eventos, uma rotina especilizada em monitorar os eventos avisa o código
especilizado em responder a um determinado evento que aquele evento que ele esperava ocorreu; e então o
código recém avisado responde ao evento.

Um uso comum da orientação a eventos é na programação de interfaces gráficas com o usuário.
Nele você escreve código que vai responder por exemplo a um clique do usuário em determinado botão,
e você associa este código ao evento do clique no botão.


2) O que entende por ciclo de gestão de eventos, gestor de eventos e ligação?

Falta aprofundar mais Mas, pelo que entendi, após construída a interface, é chamado o ciclo de gestão de eventos.
A aplicação termina quando é desencadeado um evento que "mata" a janela principal.
No ciclo, podemos observar os eventos, que vão para ele e o output são ações, logo depois o processamento.
Bem como input "inicialização" e output "terminação".


3) O que entende por widgets e que grupos conhece?

Widgets são objetos python eventos que têm uma representação no navegador, geralmente como um controle,
como um controle deslizante, caixa de texto, etc.


4) O que entende por callback e para que servem?

Um retorno de chamada é uma função que é passada como um argumento para outra função. Espera-se que esta
outra função chame esta função de retorno de chamada em sua definição. O ponto em que outra função chama
nossa função de retorno de chamada depende do requisito e da natureza da outra função.

Funções de retorno de chamada geralmente são usadas com funções assíncronas.

Exemplo de função de retorno de chamada: A função de retorno de chamada pode ser passada a uma função para imprimir
o tamanho do arquivo depois que a função ler o arquivo de texto fornecido.


def callbackFunc1(s):
    print('Callback Function 1: Length of the text file is : ', s)

def callbackFunc2(s):
    print('Callback Function 2: Length of the text file is : ', s)

def printFileLength(path, callback):
    f = open(path, "r")
    length = len(f.read())
    f.close()
    callback(length)

if __name__ == '__main__':
    printFileLength("sample.txt", callbackFunc1)
    printFileLength("sample.txt", callbackFunc2)

Output:

Callback Function 1: Length of the text file is :  56
Callback Function 2: Length of the text file is :  56


5) O que são as variáveis em tkinter, que tipos conhece e para que servem?

O Tkinter suporta algumas variáveis que são usadas para manipular os valores dos widgets do Tkinter.
Essas variáveis funcionam como variáveis normais.

set()e get()métodos são usados para definir e recuperar os valores dessas variáveis.

Os valores dessas variáveis podem ser definidos usando o set()método ou usando o construtor dessas variáveis.

BooleanVar()
StringVar()
IntVar()
DoubleVar()

'''
