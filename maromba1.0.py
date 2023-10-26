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
Tela_Cadastro = False
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
                            treino = Image(centro, "TREINO.png")
                            login.undraw()
                            treino.draw(janela)
                            break
                        else:
                            erro_login = Image(centro, "TELA_LOGIN_ERRO.png")
                            erro_login.draw(janela)
            else:
                erro_login = Image(centro, "TELA_LOGIN_ERRO.png")
                erro_login.draw(janela)
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
            Tela_Cadastro = True


print(dados)
if Tela_Cadastro:
    # tela de cadastro
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

                username = username.getText().lower()

                idade = idade.getText()
                print(idade)
                genero = genero.getText()
                print(genero)
                peso = peso.getText()
                print(peso)
                altura = altura.getText()
                print(altura)
                disponibilidade = disponibilidade.getText()
                print(disponibilidade)
                Tela_Cadastro = False
                cadastro.undraw()
                Tela_Loading = True

# tela de loading
if Tela_Loading:
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
            "messages": [{"role": "user", "content": f"""monte um treino, apenas com agrupamento do dia, exercícios com suas series e repetições.
Ao trocar de dia (treino), crie a próxima linha com apenas o caractere ' ; '
Sem textos supérfluos 
idade:{idade}
sexo: {genero}
peso:{peso}
altura: {altura}
dias da semana disponíveis para treino: {disponibilidade}

-> Por exemplo:
Dia 1 (Segunda-feira) - Treino de Peito e Tríceps:
Supino Reto: 4x10
Supino Inclinado com Halteres: 3x12
Crucifixo na Máquina: 3x12
Tríceps Testa: 4x10
Tríceps Corda no Pulley: 3x12
;
Dia 2 (Terça-feira) - Treino de Pernas:
Agachamento Livre: 4x10
Leg Press: 3x12
Cadeira Extensora: 3x12
Flexora deitado: 4x10
Panturrilha no Leg Press: 4x15
;
..."""}]
        }

        mensagem = json.dumps(mensagem)
        requisicao = requests.post(link, headers=headers, data=mensagem)

        output = requisicao.json()
        output = output["choices"][0]["message"]["content"]
        if output != None or output != "":
            print(output)
            return output
        else:
            requi()

    output = requi()

    #Recebendo output do gpt
    if output != "":
        arq_treino = open("treinos.csv", "a")
        arq_treino.write(f"{username}\n")
        dados_treino_tratados = [] #Lista com todos os dias de treino
        output = output.split(";")
        for dia in output:
            dia = dia.split("\n")
            for exercicio in dia: # Retirando o \n e listas vazias
                if exercicio == "":
                    dia.remove(exercicio)
            if len(dia) != 0:
                dados_treino_tratados.append(dia)
                dia = ";".join(dia)
                dia += ";"
                arq_treino.write(dia)
                arq_treino.write("\n")
        print("-----------------------------------------------------------")
        print(dados_treino_tratados)
        for dia in dados_treino_tratados:
            dia = ";".join(dia) #Vai ter que criar uma lista nova
        print(dados_treino_tratados)
        print("-------------------")
        arq_treino.write("$")
        arq_treino.write("\n")

        Tela_Treino = True
        break


if Tela_Treino:
    treino = Image(centro, "TREINO.png")
    Tela_Loading = False
    Tela_Cadastro = False
    Tela_Login = False
    treino.draw(janela)

def Mostra_Treino(arq, nome):
    treino = open(arq, "r") #Abrindo arquivos com treinos
    treino = treino.read()
    treino = treino.split("$") #Separando os treinos de cada pessoa
    todos_treinos = []
    coluna1 = ""
    coluna2 = ""
    for pessoa in treino:
        pessoa = pessoa.split("\n")
        for exercicio in pessoa:
            if exercicio == "": #Removendo os \n
                pessoa.remove(exercicio)
        if len(pessoa) != 0: #Colocando em uma lista com todas as pessoas
            todos_treinos.append(pessoa)
            #Removendo a lista vazia que sobra
    print(todos_treinos)
    for pessoa in todos_treinos:
        if pessoa[0] == nome:
            treino_escolido = pessoa
            break
        else:
            print("Não tem esse nome")

    print(treino_escolido)
    treino_tratado = []
    for dia in treino_escolido[1:]: #Retirando os ; e colocando \n
        dia_new = dia.replace(";","\n")
        treino_tratado.append(dia_new)
    print(treino_tratado)


    tamanho_coluna_1 = len(treino_tratado) // 2
    for exercicio in range(0,tamanho_coluna_1):
        coluna1 += treino_tratado[exercicio] + "\n"

    for exercicio in range(tamanho_coluna_1, len(treino_tratado)):
        coluna2 += treino_tratado[exercicio] + "\n"

    return coluna1, coluna2



while Tela_Treino:

    Nome_do_Treino = Text(Point(640,101), f"Treino de {username}")
    Nome_do_Treino.setSize(17), Nome_do_Treino.setTextColor(color_rgb(166,166,166)), Nome_do_Treino.setStyle("bold")
    Nome_do_Treino.draw(janela)
    textos = Mostra_Treino("treinos.csv",username.lower())
    coluna1 = Text(Point(426,375), textos[0])
    coluna2 = Text(Point(853,375), textos[1])
    coluna1.draw(janela)
    coluna2.draw(janela)
    tecla = janela.getKey()
    if tecla == "a":
        janela.close()


