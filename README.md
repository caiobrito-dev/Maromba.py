OBSERVAÇÕES A RESPEITO DO PROGRAMA!:

- É possivel que o ChatGPT envie algumas coisas a mais que não deveriam ser enviadas, como: ';' a mais, mensagens
de recomendações, observações para o treino antes e no final do output, '\n' a mais entre outros problemas.
Nesses outputs errados do ChatGPT é possivel que na hora de printar o treino fique com uma linha gigante, então
para garantir uma boa experiencia com o programa recomendamos que fique de olho no banco de dados para ver como ele 
está respondendo as requisições e se necessário retire outputs indesejados, a seguir daremos algumas instruções a
respeito do banco de dados!

- No arquivo 'cadastros.csv' estão registrados todos os logins do programa, estes que são salvos na 'TELA_CADASTRO.png'
no arquivo os dados são separados da seguinte forma: 'username;senha\n', nos nossos testes esse padrão foi mantido a 
todo tempo pois não está dependente de meios externos mas sim somente da logica desenvolvida no programa!

- No arquivo 'treinos.csv' estão registrados todos os treinos recebidos pelo ChatGPT, estes são salvos na
'TELA_LOADING.png' no arquivo os dados são separados da seguinte forma, primeiro é colocado o nome do usuario,
depois quebramos a linha e colocamos o primeiro dia com cada exercicio separado por ';' e ao final de cada dia colocamos
um ';' e quebramos a linha novamente. Ao final do treino de cada pessoa colocamos o caracter '$' e quebramos a linha, 
após isso vem o proximo usuario, como é um processo que ocupa muitas linhas ficaria dificil mostrar aqui então para
melhor noção de como funciona recomendamos que olhe o arquivo 'treinos.csv'. Organizamos o banco de dados dessa 
forma pois foi o melhor jeito que encontramos para trabalhar com os dados e suas alterações. Certas vezes o 
ChatGPT manda ';' a mais ou a menos quando ele manda esse caracter a menos o programa resolve e a mais
tambem (pelo menos nos nossos testes kkkk), entretanto no banco de dados essa mudança fica aparente, por isso
se ocorrer pedimos que seja feita a retirada manualmente de possiveis outputs não desejados do ChatGPT.

- Existe um bug raro que acontece nos inputs do programa, as unicas vezes que vimos ele acontecer foi na 
'TELA_CADASTRO' e na 'TELA_GERAR_NOVO_TREINO'. O bug é o seguinte, após o usuario enviar seus dados clicando
no botão algum dos inputs presentes na tela não é removido como os outros, ele fica lá até o encerramento
do programa, fizemos de tudo para descobrir o porque, e porque só acontece as vezes mas infelizmente 
não descobrimos o motivo

- Na tela de alterar o treino para escolher o exercício que deseja alterar basta somente digitar o nome do 
exercício não é necessário digitar a quantidade de repetições, entretanto quando for enviar o
novo exercício pedimos que siga o seguinte padrão: 'supino reto-4x12' foi nesse unico padrão que
conseguimos alterar o exercício e sua serie. O login para o treinador é, username: istrutor senha: aed1 

- É possivel que o ChatGPT não responda a requisição, adicionamos a recursividade na função: requi()
mas aparentemente não é possivel fazer requisições seguidas, quando ocorre dele não responder a requisição
o programa fica preso na 'TELA_LOADING' portanto é necessário fecha-lo, se a requisição estiver sendo feita 
com o objetivo de gerar um novo treino e ocorrer esse erro é possivel que o usuario perca seu treino, e se
esse erro ocorrer após o cadastro o usuario fica salvo no banco de dados entretanto não possui um treino
fizemos de tudo para evitar isso também entretanto não obtivemos sucesso.

Aparentemente esses são os pontos mais importantes para serem lembrados! Desejamos uma ótima experiencia com 
o programa, foi feito com muito esforço e carinho!

Ass.: Caio Barcelos e Tiago Pinheiro
