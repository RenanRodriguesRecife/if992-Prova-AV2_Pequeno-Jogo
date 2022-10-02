# if992-Prova-AV2_Pequeno-Jogo
Refazendo a prova AV2 de Programação 2

<img src="2VA-Groups3.jpg">

Obs:
O diagrama e a descrição são apenas uma visão geral do sistema. Conforme encontrem aplicação, grupos devem implementar padrões de projeto que se encaixem com as classes trabalhadas.


### 1. Coisa

Toda **Coisa** possui acesso ao **Mapa**.
Os métodos de Coisa deverão ser sobrescritos pelas subclasses que necessitarem. O comportamento padrão dos métodos concretos é não fazer nada.

#### 1.1 Inimigo

O método escolherAcao() escolher uma direção aleatória para mover().

##### 1.1.1. Semialeatorio

Semialeatório se move aleatoriamente 50% das vezes e se move em uma direção se aproximando do Jogador nas demais.

##### 1.1.2 Devagar

Devagar se fica parado um movimento e se move em uma direção se aproximando do Jogador em outro movimento.

##### 1.1.3 Invisivel

Invisível sobrescreve os métodos entrarArea() e sairArea(), nesses o símbolo do objeto é alterado para o mesmo do valor padrão de Coisa (espaços vazios) ao sair e para 'o' ao entrar.

#### 1.2 Jogador

Jogador move em uma das quatro direções de acordo com o evento consumido que é passado para mover()

#### 1.3 Tesouro

reagirMovimento() verifica se existe algum outro **Tesouro** no mapa e caso não exista finaliza o mapa com sucesso, além disso, remove o tesouro do mapa.

#### 1.4 Bomba

Bomba reage ao movimento diminuindo seu contador até 0. Em 0, o contador é resetado e a bomba verifica se existem **Coisas** em uma cruz com distância 2 (2 para cima, 2 para a esquerda, etc.) e chama reagirMovimento() de cada **Coisa** encontrada.

Bomba sobrescreve os métodos entrarArea e sairArea, nesses o símbolo do objeto é alterado para o mesmo do valor padrão de Coisa (espaços vazios) ao sair e para ‘*’ ao entrar.

#### 1.5 Parede

Parede impede o movimento.

### 2. TecladoListener

getEntradaTeclado() recebe um caractere de entrada do usuário e guarda como ‘tecla’. ‘tecla’ é limpa e retornada ao chamar consumirEvento().

### 3. Jogo

Jogo guarda o **Mapa** e informações de execução do jogo, além de ter acesso ao **GeradorMapa** e ao **ArquivoJogo**. pausarJogo() mostra um menu com opções para continuar, salva ou carregar o jogo do arquivo.

laco() realiza o laço principal do jogo, onde o mapa é mostrado de acordo com a câmera (TAMANHO_CAMERA x TAMANHO_CAMERA em volta da posição do Jogador). Lê a entrada utilizando **TecladoListener** e decide a entrada será consumida pelo **Jogador** para realizar movimento, ou pelo **Jogo** para pausar, salvar ou carregar.

O método ainda verifica se o mapa foi finalizado, caso tenha, verifica se todos os **Tesouros** foram coletados e inicia o próximo nível, com tamanho igual ao nível + 9 e quantidade de tesouros igual ao nível. Ou finaliza o jogo, caso ainda existam tesouros. Em ambos os casos, a pontuação do nível é adicionada à pontuação total.

### 4. ArquivoJogo

Salva em um arquivo a pontuação, nível, e mapa (incluindo estado do jogador) em um arquivo e o carrega.

### 5. Mapa

Mantém **Coisas** e controlar suas ações, reações e sinalizadores.

### 6. Camera

Imprime na tela uma seção do **Mapa**.

### 7. GeradorMapa

Cria um **Mapa** com base nas características passadas. É usado no início de cada nível. probX representa a chance de uma **Coisa** do tipo X existir, um número aleatório deve ser gerado e caso seja menor do que probX a **Coisa** é criada e adicionada no mapa.
