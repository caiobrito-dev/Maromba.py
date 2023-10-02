from graphics import *


def cria_input(x, y, width, size):
    entrada = Entry(Point(x, y), width)
    entrada.setFill(color_rgb(166, 166, 166))
    entrada.setTextColor('White'), entrada.setSize(size)
    entrada.draw(janela)
    return entrada


# variaveis
largura, altura = 1280, 720
centro = Point(largura/2, altura/2)
username_flag = False
senha_flag = False
email_flag = False
genero_flag = False
idade_flag = False
peso_flag = False
altura_flag = False
disponibilidade_flag = False
objetivo_flag = False

dados = dict(Username="", Senha="")
cadastros = [
    dict(Username="adm2023", Senha="aed1")
]

# janela
janela = GraphWin('Maromba.Py', largura, altura)

# tela de login
Tela_Login = True
login = Image(centro, 'MENU.png')
login.draw(janela)
while Tela_Login:

    # checando mouse
    pos_mouse = janela.checkMouse()
    if pos_mouse is not None:
        pos_mouseX = pos_mouse.getX()
        pos_mouseY = pos_mouse.getY()

        # clicando na caixa de usuario
        if 528 <= pos_mouseX <= 782 and 296 <= pos_mouseY <= 344:
            username = cria_input(655, 320, 21, 16)
            username_flag = True

        # clicando na caixa de senha
        if 528 <= pos_mouseX <= 782 and 360 <= pos_mouseY <= 408:
            senha = cria_input(655, 385, 21, 16)
            senha_flag = True

        # clicando no botão de login
        if 560 <= pos_mouseX <= 720 and 424 <= pos_mouseY <= 470:

            # checando se senha e username foram preenchidos
            if senha_flag and senha.getText() != "" and username_flag and username.getText() != "":
                dados["Username"] = username.getText().lower()
                dados["Senha"] = senha.getText().lower()

                # checando login
                for pessoa in cadastros:
                    if pessoa == dados:
                        print("Tem login")
                    else:
                        print("Não tem")
                print(cadastros)
            else:
                print("Caio")  # erro de não digitar nada

        # clicando no botão de cadastro
        if 599 <= pos_mouseX <= 681 and 488 <= pos_mouseY <= 512:
            if senha_flag:
                senha.undraw()
                senha_flag = False
            if username_flag:
                username.undraw()
                username_flag = False
            Tela_Login = False
            login.undraw()

print(dados)

# tela de cadastro
Tela_Cadastro = True
cadastro = Image(centro, 'CADASTRO.png')
cadastro.draw(janela)
while Tela_Cadastro:

    # checando mouse
    pos_mouse = janela.checkMouse()
    if pos_mouse is not None:
        pos_mouseX = pos_mouse.getX()
        pos_mouseY = pos_mouse.getY()

        # clicando na caixa de username
        if 344 <= pos_mouseX <= 668 and 168 <= pos_mouseY <= 200:
            username = cria_input(504, 184, 33, 12)
            username_flag = True

        # clicando na caixa de e-mail
        if 344 <= pos_mouseX <= 668 and 241 <= pos_mouseY <= 273:
            email = cria_input(504, 257, 33, 12)
            email_flag = True

        # clicando na caixa de senha
        if 700 <= pos_mouseX <= 900 and 241 <= pos_mouseY <= 273:
            senha = cria_input(800, 257, 19, 12)
            senha_flag = True

        # clicando na caixa de gênero
        if 344 <= pos_mouseX <= 504 and 342 <= pos_mouseY <= 374:
            genero = cria_input(424, 358, 15, 12)
            genero_flag = True

        # clicando na caixa de idade
        if 536 <= pos_mouseX <= 636 and 342 <= pos_mouseY <= 374:
            idade = cria_input(586, 358, 8, 12)
            idade_flag = True

        # clicando na caixa de peso
        if 668 <= pos_mouseX <= 768 and 342 <= pos_mouseY <= 374:
            peso = cria_input(718, 358, 8, 12)
            peso_flag = True

        # clicando na caixa de altura
        if 800 <= pos_mouseX <= 900 and 342 <= pos_mouseY <= 374:
            altura = cria_input(850, 358, 8, 12)
            altura_flag = True

        # clicando na caixa de disponibilidade
        if 344 <= pos_mouseX <= 900 and 415 <= pos_mouseY <= 447:
            disponibilidade = cria_input(622, 431, 59, 12)
            disponibilidade_flag = True

        # clicando na caixa de objetivo
        if 344 <= pos_mouseX <= 900 and 488 <= pos_mouseY <= 520:
            objetivo = cria_input(622, 504, 59, 12)
            objetivo_flag = True

        # clicando no botão de cadastro
        if 560 < pos_mouseX < 720 and 536 < pos_mouseY < 584:
            if username_flag and username.getText() != "" and senha_flag and senha.getText() != "" and email_flag and email.getText() != "" and genero_flag and genero.getText() != "" and idade_flag and idade.getText() != "" and peso_flag and peso.getText() != "" and altura_flag and altura.getText() != "" and disponibilidade_flag and disponibilidade.getText() != "" and objetivo_flag and objetivo.getText() != "":
                username.undraw(), senha.undraw(), email.undraw(), genero.undraw(), idade.undraw(), peso.undraw(), altura.undraw(), disponibilidade.undraw(), objetivo.undraw()
                Tela_Cadastro = False
                cadastro.undraw()

# tela de loading
Tela_Loading = True
loading = Image(centro, 'LOADING.png')
loading.draw(janela)
while Tela_Loading:

    # checando mouse
    pos_mouse = janela.checkMouse()
    if pos_mouse is not None:
        pos_mouseX = pos_mouse.getX()
        pos_mouseY = pos_mouse.getY()

janela.close()
