from graphics import *


def cria_input(x, y, width, red, green, blue):
    entrada = Entry(Point(x, y), width)
    entrada.setFill(color_rgb(red, green, blue))
    entrada.draw(janela)
    return entrada


# variaveis
largura, altura = 1280, 720
centro = Point(640, 360)
Tela_Login = True
Tela_Cadastro = False
Tela_Loading = False
senha_flag = False
senha_text = False
username_flag = False
username_text = False

dados = dict(Username="", Senha="")
cadastros = [
    dict(Username="adm2023", Senha="aed1")
]

# janela
janela = GraphWin('Maromba.Py', largura, altura)

# login
login = Image(centro, 'MENU.png')
login.draw(janela)

while Tela_Login:

    pos_mouse = janela.checkMouse()

    if pos_mouse is not None:
        pos_mouseX = pos_mouse.getX()
        pos_mouseY = pos_mouse.getY()

        # Clicando na caixa do usuario
        if 528 <= pos_mouseX <= 780 and 296 <= pos_mouseY <= 344:
            username = cria_input(651, 320, 20, 166, 166, 166)
            username.setTextColor('White'), username.setSize(16)
            username_flag = True

        # Verificando se há texto
        if username_flag and username.getText() != "":
            username_text = True

        # Clicando na tela da senha
        if 528 <= pos_mouseX <= 780 and 360 <= pos_mouseY <= 408:
            senha = cria_input(651, 385, 20, 166, 166, 166)
            senha.setTextColor('White'), senha.setSize(16)
            senha_flag = True

        # Verificando se há texto
        if senha_flag and senha.getText() != "":
            senha_text = True

        # Clicando no botão de login
        if 570 <= pos_mouseX <= 710 and 424 <= pos_mouseY <= 472:

            if senha_text and username_text:
                dados["Username"] = username.getText().lower()
                dados["Senha"] = senha.getText().lower()

                for pessoa in cadastros:
                    if pessoa == dados:
                        print("Tem login")
                    else:
                        print("Não tem")
                print(senha_text)
                print(username_text)
                print(cadastros)
            else:
                print("Caio")
                # Erro de não digitar nada

        # Clicando para criar cadastro
        if 599 <= pos_mouseX <= 661 and 488 <= pos_mouseY <= 512:
            Tela_Login = False
            if senha_flag:
                senha.undraw()
                senha_flag = False
            if username_flag:
                username.undraw()
                username_flag = False
            login.undraw()
            Tela_Cadastro = True
            cadastro = Image(centro, 'CADASTRO.png')
            cadastro.draw(janela)
    else:
        pass
print(dados)

senha_flag = False
senha_text = False
username_flag = False
username_text = False
email_flag = False
email_text = False
genero_flag = False
genero_text = False
idade_flag = False
idade_text = False
peso_flag = False
peso_text = False
altura_flag = False
altura_text = False
disponibilidade_flag = False
disponibilidade_text = False
objetivo_flag = False
objetivo_text = False

while Tela_Cadastro:
    pos_mouse = janela.checkMouse()

    if pos_mouse is not None:
        pos_mouseX = pos_mouse.getX()
        pos_mouseY = pos_mouse.getY()

        # Caixa do Username
        if 344 <= pos_mouseX <= 584 and 168 <= pos_mouseY <= 200:
            username = cria_input(464, 184, 23, 166, 166, 166)
            username.setTextColor('White'), username.setSize(12)
            username_flag = True

        # Verificando texto no username
        if username_flag and username.getText() != "":
            username_text = True
        else:
            username_text = False

        # Caixa de e-mail
        if 348 <= pos_mouseX <= 668 and 241 <= pos_mouseY <= 273:
            email = cria_input(504, 257, 32, 166, 166, 166)
            email.setTextColor("white"), email.setSize(12)
            email_flag = True

        # Verificando se há texto no email
        if email_flag and email.getText() != "":
            email_text = True
        else:
            email_text = False

        # Senha
        if 712 <= pos_mouseX <= 872 and 241 <= pos_mouseY <= 273:
            senha = cria_input(792, 257, 14, 166, 166, 166)
            senha.setTextColor("white"), senha.setSize(12)
            senha_flag = True

        # Verificando se há texto na senha
        if senha_flag and senha.getText() != "":
            senha_text = True
        else:
            senha_text = False

        # Gênero
        if 344 <= pos_mouseX <= 504 and 342 <= pos_mouseY <= 374:
            genero = cria_input(424, 358, 14, 166, 166, 166)
            genero.setTextColor('white'), genero.setSize(12)
            genero_flag = True

        # Verificando se há texto em genero
        if genero_flag and genero.getText() != "":
            genero_text = True

        # Idade
        if 536 <= pos_mouseX <= 636 and 342 <= pos_mouseY <= 374:
            idade = cria_input(586, 358, 8, 166, 166, 166)
            idade.setTextColor('white'), idade.setSize(12)
            idade_flag = True

        # Verificando se há texto em idade
        if idade_flag and idade.getText() != "":
            idade_text = True

        # Peso
        if 668 <= pos_mouseX <= 768 and 342 <= pos_mouseY <= 374:
            peso = cria_input(718, 358, 8, 166, 166, 166)
            peso.setTextColor('white'), peso.setSize(12)
            peso_flag = True

        # Verificando se há texto em peso
        if peso_flag and peso.getText() != "":
            peso_text = True

        # Altura
        if 800 <= pos_mouseX <= 900 and 342 <= pos_mouseY <= 374:
            altura = cria_input(850, 358, 8, 166, 166, 166)
            altura.setTextColor('white'), altura.setSize(12)
            altura_flag = True

        # Verificando se há texto em altura
        if altura_flag and altura.getText() != "":
            altura_text = True

        # Disponibilidade
        if 344 <= pos_mouseX <= 764 and 415 <= pos_mouseY <= 447:
            disponibilidade = cria_input(554, 431, 43, 166, 166, 166)
            disponibilidade.setTextColor('white'), disponibilidade.setSize(12)
            disponibilidade_flag = True

        # Verificando se há texto em disponibilidade
        if disponibilidade_flag and disponibilidade.getText() != "":
            disponibilidade_text = True

        # Objetivo
        if 344 <= pos_mouseX <= 900 and 488 <= pos_mouseY <= 520:
            objetivo = cria_input(622, 504, 58, 166, 166, 166)
            objetivo.setTextColor('white'), objetivo.setSize(12)
            objetivo_flag = True

        # Verificando se há texto em objetivo
        if objetivo_flag and objetivo.getText() != "":
            objetivo_text = True

            # Clicando no botão de cadastro
            if 560 < pos_mouseX < 720 and 536 < pos_mouseY < 584:
                if senha_text and username_text and email_text and genero_text and idade_text and peso_text and altura_text and disponibilidade_text and objetivo_text:
                    if senha_flag:
                        senha.undraw()
                        senha_flag = False
                    if username_flag:
                        username.undraw()
                        username_flag = False
                    if email_flag:
                        email.undraw()
                        email_flag = False

                    Tela_Cadastro = False
                    cadastro.undraw()
                    Tela_Loading = True
                    loading = Image(centro, 'LOADING.png')
                    loading.draw(janela)
janela.close()
