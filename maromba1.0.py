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
contlog = 0

dados = dict(Username="", Senha="")

# criando login
lista_logins = []
logins = open("cadastros.csv", "r")
lista_nomes = logins.readlines()
for pessoa in lista_nomes:
    pessoa = pessoa.split(";")
    lista_logins.append(pessoa)
logins.close()
print(lista_logins)

# janela
janela = GraphWin('Maromba.Py', largura, altura)

# Flags das telas
Tela_Login = True
Tela_Cadastro = False
Tela_Treino_Login = False
Tela_Treinador_1 = False
Tela_Treinador_2 = False
Tela_Treinador_3 = False
Tela_Gerar_Novo_Treino = False
Tela_Loading = False
Tela_Treino_no_cadastro = False

# Iniciando programa
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

                # Login do treinador
                if dados["Username"] == "instrutor" and dados["Senha"] == "aed1":
                    username.undraw(), senha.undraw()
                    Tela_Treinador_1 = True
                    Tela_Login = False
                    login.undraw()
                    break
                for pessoa in lista_logins:
                    # login correto
                    if pessoa[0] == dados["Username"] and pessoa[1] == dados["Senha"]:
                        print("Tem login")
                        username.undraw(), senha.undraw()
                        Tela_Treino_Login = True
                        Tela_Login = False
                        login.undraw()
                        break
                    else:
                        contlog = 0
                        for pessoa2 in lista_logins:
                            if dados["Username"].count(pessoa2[0]) == 1 and dados["Senha"].count(pessoa2[1]) == 1:
                                contlog += 1
                        if contlog == 0:
                            erro_login = Image(centro, "TELA_LOGIN_ERRO.png")
                            erro_login.draw(janela)

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


def Mostra_Treino(arq, nome):
    treino = open(arq, "r")  # Abrindo arquivos com treinos
    treino = treino.read()
    treino = treino.split("$")  # Separando os treinos de cada pessoa
    todos_treinos = []
    coluna1 = ""
    coluna2 = ""
    for pessoa in treino:
        pessoa = pessoa.split("\n")
        for exercicio in pessoa:
            if exercicio == "":  # Removendo os \n
                pessoa.remove(exercicio)
        if len(pessoa) != 0:  # Colocando em uma lista com todas as pessoas
            todos_treinos.append(pessoa)
            # Removendo a lista vazia que sobra
    print(todos_treinos)
    for pessoa in todos_treinos:
        if pessoa[0] == nome:
            treino_escolido = pessoa
            break
        else:
            if pessoa == todos_treinos[-1]:
                return "O aluno escolhido não foi cadastrado"

    print(treino_escolido)
    treino_tratado = []
    for dia in treino_escolido[1:]:  # Retirando os ; e colocando \n
        dia_new = dia.replace(";", "\n")
        treino_tratado.append(dia_new)
    print(treino_tratado)

    tamanho_coluna_1 = len(treino_tratado) // 2
    for exercicio in range(0, tamanho_coluna_1):
        coluna1 += treino_tratado[exercicio] + "\n"

    for exercicio in range(tamanho_coluna_1, len(treino_tratado)):
        coluna2 += treino_tratado[exercicio] + "\n"

    return coluna1, coluna2


def Altera_exercicio(arq, nome, exercicio_escolhido, alteracao):
    arq = open(arq, "r")  # Abrindo arquivos com treinos
    treino = arq.read()
    arq.close()
    treino = treino.split("$")  # Separando os treinos de cada pessoa
    todos_os_treino = []

    # colocando todos os treinos splitados em uma so lista
    for pessoa in treino:
        pessoa = pessoa.split("\n")
        # retirando elementos vazios
        for exercicio in pessoa:
            if exercicio == "":
                pessoa.remove(exercicio)
        todos_os_treino.append(pessoa)

    # procurando a pessoa
    for pessoa in todos_os_treino:
        if pessoa[0] == nome:
            treino_esolhido = pessoa
            posicao_aluno = todos_os_treino.index(pessoa)

    # lista para realizar o replace
    novo_treino = []

    # splitando entradas
    exercicio_escolhido = exercicio_escolhido.split("-")
    alteracao = alteracao.split("-")
    print(exercicio_escolhido)
    print(alteracao)
    print(treino_esolhido)

    # procurando o exercicio para fazer a alteração

    for dia in treino_esolhido:

        # Vendo se o exercicio está naquele dia de treino
        if exercicio_escolhido[0] in dia:
            novo_dia = ""
            dia = dia.split(";")
            novo_dia += dia[0] + ";"  # colocando a parte inicial do treino (dia tal treino tal)

            # Procurando o exercicio a partir disso
            for exercicio in dia[1:]:

                exercicio_splitado = exercicio.split(
                    ":")  # Splito nos ':' para procurar pelo exercicio e se achar mudar tbm a serie

                if exercicio_splitado[0] == exercicio_escolhido[0]:  # Exercicio encontrado
                    novo_dia += alteracao[0] + ":" + " "
                    novo_dia += alteracao[1] + ";"
                else:
                    if len(exercicio_splitado) > 1:  # Colocando os outros exercicio na string
                        novo_dia += exercicio_splitado[0] + ":"
                        novo_dia += exercicio_splitado[1] + ";"
                    if exercicio == dia[-1]:
                        novo_dia += exercicio_splitado[0]

            novo_treino.append(novo_dia)  # colocando na lista principal apos a alteração

        else:
            novo_treino.append(dia)
    print(novo_treino)
    print("------------------------")
    todos_os_treino[posicao_aluno] = novo_treino
    # print(todos_os_treino[posicao_aluno])
    # print(todos_os_treino)

    treino_pro_arquivo = ""

    for aluno in todos_os_treino:
        if len(aluno) > 1:
            for exercicio in aluno:
                treino_pro_arquivo += exercicio + "\n"
            treino_pro_arquivo += "$" + "\n"
    print(treino_pro_arquivo)

    arq = open("treinos_teste.csv", "w")
    arq.write(treino_pro_arquivo)
    arq.close()

api_key = "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"

def requi(idade, genero, peso, altura, disponibilidade):
        link = "https://api.openai.com/v1/chat/completions"
        idgpt = "gpt-3.5-turbo"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

        mensagem = {
            "model": idgpt,
            "messages": [{"role": "user", "content": f"""monte um treino, apenas com agrupamento do dia, exercícios com suas series e repetições.
Ao trocar de dia (treino), crie a próxima linha com apenas o caractere ' ; '
Sem textos supérfluos 
idade:{idade}
sexo: {genero}
peso: {peso}
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
        if output is not None or output != "":
            print(output)
            return output.lower()
        else:
            requi(idade, genero, peso, altura, disponibilidade)


if Tela_Treinador_1:
    tela_treinador = Image(centro, "TELA_TREINADOR_1.png")
    tela_treinador.draw(janela)

    coluna1_txt = ""
    coluna2_txt = ""
    tamanho = len(lista_logins) // 2

    # Printando os alunos disponiveis na tela
    for aluno in range(1, tamanho):
        coluna1_txt += lista_logins[aluno][0].capitalize() + "\n"

    for aluno in range(tamanho, len(lista_logins)):
        coluna2_txt += lista_logins[aluno][0].capitalize() + "\n"
    coluna1 = Text(Point(426, 375), coluna1_txt)
    coluna2 = Text(Point(853, 375), coluna2_txt)
    coluna1.setTextColor(color_rgb(166, 166, 166)), coluna1.setStyle('bold')
    coluna2.setTextColor(color_rgb(166, 166, 166)), coluna2.setStyle('bold')
    coluna1.draw(janela), coluna2.draw(janela)

    # Aluno escolhido
    aluno_escolhido = cria_input(690, 563, 15, 16)
    aviso_flag = False

while Tela_Treinador_1:

    pos_mouse = janela.checkMouse()
    if pos_mouse is not None:

        pos_mouseX = pos_mouse.getX()
        pos_mouseY = pos_mouse.getY()

        # Clicando na escolha do aluno
        if 532 <= pos_mouseX <= 745 and 591 <= pos_mouseY <= 647:
            # Verificando texto
            if aluno_escolhido.getText() != "":
                aluno = aluno_escolhido.getText().strip().lower()

                coluna1.undraw()
                coluna2.undraw()
                aluno_escolhido.undraw()
                tela_treinador.undraw()
                Tela_Treinador_2 = True
                Tela_Treinador_1 = False

                if aviso_flag:
                    aviso.undraw()

            # Caixa de texto vazia
            else:
                aviso = Text(Point(640, 530), "Preencha o campo")
                aviso.setTextColor(color_rgb(166, 166, 166)), aviso.setStyle("bold")
                aviso_flag = True
                aviso.draw(janela)

if Tela_Treinador_2:

    tela_treinador = Image(centro, "TELA_TREINADOR_2.png")
    tela_treinador.draw(janela)
    # inputs de exercicios
    exercicio_escolhido = cria_input(535, 590, 20, 13)
    alteracao_do_exercicio = cria_input(900, 590, 20, 13)

    # Mostrando treino do aluno desejado
    textos = Mostra_Treino("treinos.csv", aluno)

    if len(textos) == 2:
        coluna1 = Text(Point(426, 360), textos[0].title())
        coluna2 = Text(Point(853, 360), textos[1].title())
        coluna1.setSize(10), coluna1.setTextColor(color_rgb(166, 166, 166)), coluna1.setStyle('bold')
        coluna2.setSize(10), coluna2.setTextColor(color_rgb(166, 166, 166)), coluna2.setStyle('bold')
        coluna1.draw(janela)
        coluna2.draw(janela)
    else:
        aluno_nao_encontrado = Text(Point(640, 360), textos)
        aluno_nao_encontrado.setStyle("bold"), aluno_nao_encontrado.setTextColor(color_rgb(166, 166, 166))
        aluno_nao_encontrado.draw(janela)

while Tela_Treinador_2:
    pos_mouse = janela.checkMouse()
    if pos_mouse is not None:

        pos_mouseX = pos_mouse.getX()
        pos_mouseY = pos_mouse.getY()

        if 560 <= pos_mouseX <= 759 and 605 <= pos_mouseY <= 647:
            # Verificando texto
            if exercicio_escolhido.getText() != "" and alteracao_do_exercicio.getText() != "":
                exercicio = exercicio_escolhido.getText().strip().lower()
                alteracao = alteracao_do_exercicio.getText().strip().lower()

                Altera_exercicio("treinos.csv", aluno, exercicio, alteracao)

                exercicio_escolhido.undraw()
                alteracao_do_exercicio.undraw()
                tela_treinador.undraw()
                Tela_Treinador_3 = True
                Tela_Treinador_2 = False

                if aviso_flag:
                    aviso.undraw()

            # Caixa de texto vazia
            else:
                aviso = Text(Point(640, 560), "Preencha o campo")
                aviso.setTextColor(color_rgb(166, 166, 166)), aviso.setStyle("bold")
                aviso_flag = True
                aviso.draw(janela)

if Tela_Treinador_3:
    tela_treinador = Image(centro, "TELA_TREINADOR_3.png")
    tela_treinador.draw(janela)
    textos = Mostra_Treino("treinos_teste.csv", aluno)
    coluna1 = Text(Point(426, 395), textos[0].title())
    coluna2 = Text(Point(853, 395), textos[1].title())
    coluna1.setSize(10), coluna1.setTextColor(color_rgb(166, 166, 166)), coluna1.setStyle('bold')
    coluna2.setSize(10), coluna2.setTextColor(color_rgb(166, 166, 166)), coluna2.setStyle('bold')
    coluna1.draw(janela)
    coluna2.draw(janela)

while Tela_Treinador_3:
    tecla = janela.getKey()
    if tecla == "a":
        janela.close()
        break

if Tela_Treino_Login:
    tela_treino = Image(centro, "TELA_TREINO_NO_LOGIN.png")
    tela_treino.draw(janela)

    #Printando treino
    Nome_do_Treino = Text(Point(640, 101), f"Treino de {dados['Username'].capitalize()}")
    Nome_do_Treino.setSize(17), Nome_do_Treino.setTextColor(color_rgb(166, 166, 166)), Nome_do_Treino.setStyle("bold")
    Nome_do_Treino.draw(janela)

    texto = Mostra_Treino("treinos.csv", dados['Username'])
    coluna1 = Text(Point(426, 375), texto[0].title())
    coluna2 = Text(Point(853, 375), texto[1].title())
    coluna1.setSize(11), coluna1.setTextColor(color_rgb(166, 166, 166)), coluna1.setStyle('bold')
    coluna2.setSize(11), coluna2.setTextColor(color_rgb(166, 166, 166)), coluna2.setStyle('bold')
    coluna1.draw(janela), coluna2.draw(janela)

while Tela_Treino_Login:

    #Checando mouse
    pos_mouse = janela.checkMouse()
    if pos_mouse is not None:
        pos_mouseX = pos_mouse.getX()
        pos_mouseY = pos_mouse.getY()

        if 525 <= pos_mouseX <= 655 and 606 <= pos_mouseY <= 648:
            coluna1.undraw()
            coluna2.undraw()
            Nome_do_Treino.undraw()
            tela_treino.undraw()
            Tela_Treino_Login = False
            Tela_Gerar_Novo_Treino = True


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
                logins.write(username.getText().strip().lower()), logins.write(";")
                logins.write(senha.getText().strip().lower()), logins.write(";"), logins.write("\n")
                logins.close()

                username = username.getText().strip().lower()

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

            else:
                erro_cadastro = Image(centro, "TELA_CADASTRO_ERRO.png")
                erro_cadastro.draw(janela)
                print("nao digitou")

if Tela_Gerar_Novo_Treino:
    tela_gerar = Image(centro, "TELA_GERAR_NOVO_TREINO.png")
    tela_gerar.draw(janela)

while Tela_Gerar_Novo_Treino:

    pos_mouse = janela.checkMouse()
    if pos_mouse is not None:
        pos_mouseX = pos_mouse.getX()
        pos_mouseY = pos_mouse.getY()

        # clicando na caixa de gênero
        if 347 <= pos_mouseX <= 507 and 287 <= pos_mouseY <= 319:
            genero = cria_input(427, 303, 15, 12)
            genero_flag = True

        # clicando na caixa de idade
        if 539 <= pos_mouseX <= 639 and 287 <= pos_mouseY <= 319:
            idade = cria_input(589, 303, 8, 12)
            idade_flag = True

        # clicando na caixa de peso
        if 671 <= pos_mouseX <= 771  and 287 <= pos_mouseY <= 319:
            peso = cria_input(721, 303, 8, 12)
            peso_flag = True

        # clicando na caixa de altura
        if 803 <= pos_mouseX <= 903 and 287 <= pos_mouseY <= 319:
            altura = cria_input(853, 303, 8, 12)
            altura_flag = True

        # clicando na caixa de disponibilidade
        if 347 <= pos_mouseX <= 903 and 360 <= pos_mouseY <= 392:
            disponibilidade = cria_input(625, 376, 59, 12)
            disponibilidade_flag = True

        # clicando na caixa de objetivo
        if 347 <= pos_mouseX <= 903 and 432 <= pos_mouseY <= 464:
            objetivo = cria_input(625, 448, 59, 12)
            objetivo_flag = True

        if 563 <= pos_mouseX <= 723 and 480 <= pos_mouseY <= 528:
            if genero_flag and genero.getText() != "" and idade_flag and idade.getText() != "" and peso_flag and peso.getText() != "" and altura_flag and altura.getText() != "" and disponibilidade_flag and disponibilidade.getText() != "" and objetivo_flag and objetivo.getText() != "":
                genero.undraw(), idade.undraw(), peso.undraw(), altura.undraw(), disponibilidade.undraw(), objetivo.undraw()

                idade = idade.getText().strip()
                genero = genero.getText().strip()
                peso = peso.getText().strip()
                altura = altura.getText().strip()
                disponibilidade = disponibilidade.getText().strip()
                Tela_Gerar_Novo_Treino = False
                tela_gerar.undraw()
                Tela_Loading = True


# tela de loading
if Tela_Loading:
    loading = Image(centro, 'LOADING.png')
    loading.draw(janela)

while Tela_Loading:

    output = requi(idade, genero, peso, altura, disponibilidade)

    # Recebendo output do gpt
    if output != "":
        arq_treino = open("treinos.csv", "a")
        arq_treino.write(f"{username}\n")
        todos_os_treino = []  # Lista com todos os dias de treino

        output_sem_carac_proibidos = (output.replace("ç", "c").replace("í", "i").replace("ô", "o").replace("ã", "a")
                                      .replace("á", "a").replace("õ", "o").replace("ú", "u"))
        output = output_sem_carac_proibidos.split(";")

        for dia in output:
            dia = dia.split("\n")
            for exercicio in dia:  # Retirando o \n e listas vazias
                if exercicio == "":
                    dia.remove(exercicio)
            if len(dia) != 0:
                todos_os_treino.append(dia)
                dia = ";".join(dia)
                dia += ";"
                arq_treino.write(dia)
                arq_treino.write("\n")
        arq_treino.write("$")
        arq_treino.write("\n")

        print("-----------------------------------------------------------")
        print(todos_os_treino)
        tratando_treino = []  # Lista para conseguir da join

        for dia in todos_os_treino:
            dia = ";".join(dia)  # Colocando cada dia em uma string
            tratando_treino.append(dia)

        print(tratando_treino)
        treino_com_quebralinha = []  # Lista para conseguir colocar a quebra de linha

        for dia in tratando_treino:  # Colocando um ; no final de cada dia para quebrar a linha
            dia += ";" + "" + ";"
            treino_com_quebralinha.append(dia)

        print(treino_com_quebralinha)

        for dia in treino_com_quebralinha:  # Removendo textos superfluos do gpt
            if "profissional" in dia.lower() or "consulte" in dia.lower() or "claro" in dia.lower() or "ajustar" in dia.lower() or "obs" in dia.lower():
                treino_com_quebralinha.remove(dia)
        print("-----------------------------------------------------------")

        Tela_Treino_no_cadastro = True
        break

if Tela_Treino_no_cadastro:
    treino = Image(centro, "TELA_TREINO_NO_CADASTRO.png")
    Tela_Loading = False
    Tela_Cadastro = False
    Tela_Login = False
    treino.draw(janela)

while Tela_Treino_no_cadastro:

    if contlog == 1:
        Nome_do_Treino = Text(Point(640, 101), f"Treino de {dados['Username'].capitalize()}")
        Nome_do_Treino.setSize(15), Nome_do_Treino.setTextColor(color_rgb(166, 166, 166)), Nome_do_Treino.setStyle("bold")
        Nome_do_Treino.draw(janela)
    else:
        Nome_do_Treino = Text(Point(640, 101), f"Treino de {username.capitalize()}")
        Nome_do_Treino.setSize(15), Nome_do_Treino.setTextColor(color_rgb(166, 166, 166)), Nome_do_Treino.setStyle("bold")
        Nome_do_Treino.draw(janela)
    mostra_treino = []

    for exercicio in treino_com_quebralinha:
        exercicio_tratado = exercicio.replace(";", "\n")
        exercicio_tratado += ";"
        exercicio_tratado = exercicio.replace(";", "\n")
        mostra_treino.append(exercicio_tratado)

    tam = len(mostra_treino) // 2
    coluna1_txt = ""
    coluna2_txt = ""
    for cont in range(tam):
        coluna1_txt += mostra_treino[cont]

    for cont in range(tam, len(mostra_treino)):
        coluna2_txt += mostra_treino[cont]

    coluna1 = Text(Point(426, 375), coluna1_txt.title())
    coluna2 = Text(Point(853, 375), coluna2_txt.title())
    coluna1.setSize(11), coluna1.setTextColor(color_rgb(166, 166, 166)), coluna1.setStyle('bold')
    coluna2.setSize(11), coluna2.setTextColor(color_rgb(166, 166, 166)), coluna2.setStyle('bold')
    coluna1.draw(janela), coluna2.draw(janela)
    tecla = janela.getKey()
    if tecla == "a":
        janela.close()
        break
