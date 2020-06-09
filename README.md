# joseBot
**TFT αυτο cλιcκεr para farm de Tokens**

Esta ferramenta foi criada para auxiliar no farm de Tokens nos eventos da Riot. Anteriormente, ao jogar o mono de jogo "TFT", bastava ficar AFK (away from keyboard) por 10 minutos e logo em seguidar se render (FF) para que os tokens fossem adicionados à conta. Ao saber disso, nossa amiga Riot resolveu implementar mecanismos para detecção de AFK's, de forma a impedir que estes ganhassem tokens. Pensando nisso, lhes apresento o José Bot, que é capaz de farmar tokens automaticamente, sem possibilidade de ban (não altera arquivos do jogo), e que também é capaz de burlar o sistema de detecção de AFK's da Riot. O bot foi desenvolvido por mim, José Ricardo, juntamente com meu amigo José Ricardo (sim), ao qual devo grande agradecimento pelas ideias.


## Instalação

Primeiramente, você vai precisar baixar e instalar o Python, que é uma linguagem de programação. Baixe a última versão pelo [link]( https://www.python.org/downloads/). No processo de instalação, tenha certeza de marcar a opção "Add Python to PATH".

Em seguida, baixe os dois arquivos que estão nesse repositório, Tokens.py e mouse.py, crie uma pasta na área de trabalho e coloque eles lá.

Agora, instalaremos as bibliotecas necessárias para rodar o bot. Abra o CMD (Windows + R -> cmd -> Enter) e execute os comandos abaixo:

```
pip install pyautogui
pip install pillow
pip install pywin32
```

Em seguida, abra uma partida custom no LoL (pode ser Summoners Rift) e coloque o jogo em modo janela, com uma resolução menor que fullscreen, e depois saia da partida. Agora, iremos configurar as coordenadas para que o bot aprenda os locais onde deve clicar. Vá até a pasta na área de trabalho onde salvou os arquivos, segure Shift + Botão direito e clique em "Abrir PowerShell" ou algo parecido. Na tela que aparecer, digite:

```
python mouse.py
```

Este programa irá mostrar as coordenadas atuais do mouse, para que possamos configurar o bot. Deixe ele aberto e, voltando na pasta onde salvou os arquivos, abra o arquivo Tokens.py com algum editor de texto e configure as coordenadas que estão na primeira parte do arquivo, que vão de "xProcurarPartida" até "yPixelDesktop". Basta você colocar o mouse em cima do local indicado e atualizar as coordenadas do arquivo Tokens.py, de acordo com seu computador.

Para um tutorial detalhado de configuração das coordenadas, clique [aqui](https://drive.google.com/open?id=1UxBu7yyjDNyZfpL77O1f-sIZAqIoho8L2Jsh1lrr3TY).

## Execução

Com as coordenadas definidas, você deverá fechar todos os programas que não sejam o bot e o LoL, abrir o power shell na pasta dos arquivos (Shift + Botão direito), mover essa tela azul de preferência para cima na esquerda (deixe ela menor para não interferir) e, estando no lobby do TFT normal game, digite no PowerShell:

```
python Tokens.py
```

O bot deverá começar a fazer suas ações. Quando quiser parar, basta fechar a janela do PowerShell ou apertar Ctrl + C nela.

## Importante

*O cliente e o jogo não podem ser movidos durante a operação do bot, e nem o mouse, de preferência.*
