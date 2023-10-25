from graphics import *
import requests
import json


def cria_input(x, y, width, size):
    entrada = Entry(Point(x, y), width)
    entrada.setFill(color_rgb(166, 166, 166))
    entrada.setTextColor('White'), entrada.setSize(size)
    entrada.draw(janela)
    return entrada


# variaveis
largura, altura = 1280, 720
centro = Point(largura / 2, altura / 2)
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
lista_logins = []

logins = open("cadastros.csv", "r")
lista_nomes = logins.readlines()
for pessoa in lista_nomes:
    pessoa = pessoa.split(";")
    lista_logins.append(pessoa)
logins.close()

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
                for pessoa in lista_logins:
                    if dados["Username"] == "instrutor" and dados["Senha"] == "aed1":
                        username.undraw()
                        senha.undraw()
                        loading = Image(centro, "LOADING.png")
                        login.undraw()
                        loading.draw(janela)
                        break
                    else:
                        if pessoa[0] == dados["Username"] and pessoa[1] == dados["Senha"]:
                            print("Tem login")
                            username.undraw()
                            senha.undraw()
                            loading = Image(centro, "LOADING.png")
                            login.undraw()
                            loading.draw(janela)
                            break
                        else:
                            print("Não tem")
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

logins = open("cadastros.csv", "a")

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
                logins.write(username.getText()), logins.write(";")
                logins.write(senha.getText()), logins.write(";"), logins.write("\n")

                idade = idade.getText()
                peso = peso.getText()
                disponibilidade = disponibilidade.getText()
                objetivo = objetivo.getText()
                Tela_Cadastro = False
                cadastro.undraw()

# tela de loading
Tela_Loading = True
loading = Image(centro, 'LOADING.png')
loading.draw(janela)

api_key = "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"

while Tela_Loading:
    def requi():
        link = "https://api.openai.com/v1/chat/completions"
        id = "gpt-3.5-turbo"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

        mensagem = {
            "model": id,
            "messages": [{"role": "user", "content": """Monte um treino, apenas com agrupamento do dia, exercícios com suas series e repetições, sem dias de descanso nos dias  disponiveis de treino. Separe os dias e cada exercicio com o caracter ";"
    Ao trocar de dia (treino), crie a próxima linha apenas com o caractere '\n'. So coloque o caracter "\n" no final de cada dia.
    Preciso que você mande sem  a mensagem "claro aqui está..." e sem a mensagem "lembrando que os exercicios..."
    So quebre a linha no final de cada dia!
    No lugar de cada exercicio escreva o seu nome como supino, agachamento, triceps corda...
    segue minhas informações:
    idade:24
    sexo: masculino
    peso: 77
    altura:1.64
    dias da semana disponíveis para treino: 7

    Aqui está um exemplo de como fazer entretanto não copie ele:
    Dia 1 (Segunda-feira) ;Treino de X e Y: ; Exercicio 1: 4x10; Exercicio 2: 3x12;Exercicio 3: 3x12;Exercicio 4: 4x10;Exercicio 5: 3x12\nDia 2 (Terça-feira) ;Treino de Z:;Exercicio 1: 4x10;Exercicio 2: 3x12;Exercicio 3: 3x12;Exercicio 4: 4x10;Exercicio 5: 4x15\n"""
                          }]
        }

        mensagem = json.dumps(mensagem)
        requisicao = requests.post(link, headers=headers, data=mensagem)

        output = requisicao.json()
        output = output["choices"][0]["message"]["content"]
        if output != None or output != "":
            if output.count('\n') > 6:
                print("errou")
                requi()
            else:
                return output
        else:
            requi()


    output = requi()

    if output != "":
        dados_treino_tratados = ""
        print(output)
        print(output.count("\n"))
        print(type(output))
        output = output.split("\n")
        print(output)
        for dia in output:
            if dia != "" and dia != "\n":
                dia = dia.split(";")
                print(dia)
                dados_treino_tratados += dia[0] + " - " + dia[1] + "\n" + "->"
            for exercicio in dia[2:]:
                if dia.index(exercicio) == len(dia) - 1:
                    dados_treino_tratados += exercicio + "\n"
                else:
                    dados_treino_tratados += exercicio + "\n" + "->"
        print(dados_treino_tratados)

    janela.close()
    break

'''# checando mouse
    pos_mouse = janela.checkMouse()
    if pos_mouse is not None:
        pos_mouseX = pos_mouse.getX()
        pos_mouseY = pos_mouse.getY()
'''

