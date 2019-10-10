#! python3
import pyautogui as pg, sys, PIL.ImageGrab, win32gui
from time import sleep

#Botão de procurar partida
xProcurarPartida = 727
yProcurarPartida = 770

#Botão de aceitar partida
xAceitarPartida = 830
yAceitarPartida = 650

#Coordenadas do primeiro campeão na loja
xCampeoes = 577
yCampeoes = 765

#Distancia lateral entre os campeões da loja
distanciaCampeoes = 134

#Botão de upar o level
xSubirNivel = 443
ySubirNivel = 793

#Posição aleatoria no tabuleiro (de preferência fora dos campeões)
xMoverMiniLenda1 = 470
yMoverMiniLenda1 = 380

#Outra posição aleatoria no tabuleiro (de preferência fora dos campeões)
xMoverMiniLenda2 = 610
yMoverMiniLenda2 = 420

#Botão de sair do jogo (fica ao lado de "Continuar Assistindo" quando você morre)
xClicarSair = 680
yClicarSair = 460

#Qualquer pixel que a tela do jogo cubra e que a tela do client não cubra
xPixelDesktop = 400
yPixelDesktop = 815

def clicarProcurarPartida():
	pg.moveTo(xProcurarPartida, yProcurarPartida, 1)
	pg.click()
#

def clicarJogarNovamente():
	clicarProcurarPartida()
#

def clicarAceitarPartida():
	pg.moveTo(xAceitarPartida, yAceitarPartida)
	pg.click()
#

def comprarCampeoes(quantidade=0):
	j = 0
	xInicial = xCampeoes

	while(j < quantidade):
		pg.moveTo(xInicial + (j*distanciaCampeoes), yCampeoes, 0.5)
		pg.mouseDown()
		sleep(0.2)
		pg.mouseUp()

		j = j + 1
	#
#

def subirNivel(quantidadeCliques=0):
	j = 0
	pg.moveTo(xSubirNivel, ySubirNivel, 0.5)

	while(j < quantidadeCliques):
		j = j + 1
		
		pg.mouseDown()
		sleep(0.2)
		pg.mouseUp()
	#
#	

def moverMiniLenda(caminho=0):
	#Posição random 1
	if(caminho == 0):
		pg.moveTo(xMoverMiniLenda1, yMoverMiniLenda1, 0.5)
		pg.mouseDown(button='right')
		sleep(0.5)
		pg.mouseUp(button='right')
		return
	#

	#Posição random 2
	if(caminho==1):
		pg.moveTo(xMoverMiniLenda2, yMoverMiniLenda2, 0.5)
		pg.mouseDown(button='right')
		sleep(0.5)
		pg.mouseUp(button='right')
		return
	#
#

def clicarSairJogo():
	pg.moveTo(xClicarSair, yClicarSair)
	pg.mouseDown()
	sleep(0.2)
	pg.mouseUp()
#

print("Created by Jose Ricardo\n\n")

#Salva instancia do client para que seja trazido para o foreground apos o fim do game
leagueClient = win32gui.FindWindow(0, "League of Legends")

pixelDesktop = PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop]
#print("Desktop: ", pixelDesktop)

sleep(5)

try:
	while True:
		sleep(7)

		#Traz o client para o foreground (topo) após o jogo acabar
		win32gui.SetForegroundWindow(leagueClient)
		win32gui.BringWindowToTop(leagueClient)

		#Entra na fila
		print("Searching game...")
		clicarProcurarPartida()

		#Enquanto a janela do jogo não abrir, continua clicando pra aceitar partida
		while (PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop] == pixelDesktop):
			clicarAceitarPartida()
			sleep(1)
		#

		print("Match found!")

		#Espera 10s antes de começar, pois a tela de load pode ficar bugada no começo
		sleep(10)

		#Grava um pixel da tela de load
		pixelTelaLoad = PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop]

		#Compara o pixel gravado da tela de load com o pixel atual do mesmo lugar, para detectar quando o jogo começar
		while (PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop] == pixelTelaLoad):
			pass
		#

		#Traz o jogo para o foreground (topo) após a partida começar
		leagueGame = win32gui.FindWindow(0, "League of Legends (TM) Client")
		win32gui.SetForegroundWindow(leagueGame)
		win32gui.BringWindowToTop(leagueGame)

		print("Game started, counting:")

		#Nesse ponto, a partida começou, e é iniciado um timer de 15 minutos
		x = 900
		while (x > 0):
			print (x, "s")
			x = x - 1
			sleep(1)

			if(x == 830):
				comprarCampeoes(2)
				moverMiniLenda(0)
				moverMiniLenda(1)
			#

			if(x == 775):
				comprarCampeoes(1)
			#

			if(x == 709):
				moverMiniLenda(1)
				comprarCampeoes(1)
				subirNivel(1)
			#

			if(x == 660):
				comprarCampeoes(1)
				subirNivel(1)
			#

			if(x == 590):
				moverMiniLenda(1)
				comprarCampeoes(1)
				moverMiniLenda(0)
			#

			if(x == 320):
				comprarCampeoes(1)
				subirNivel(1)
			#

			if(x == 260):
				subirNivel(1)
				comprarCampeoes(2)
				moverMiniLenda(1)
			#

			if(x == 60):
				subirNivel(20)
				moverMiniLenda(0)
				moverMiniLenda(1)
			#
		#

		timer = 0

		#Após acabar os 15 minutos, espera pra morrer, clicando no botão de sair até detectar que o jogo fechou
		while (PIL.ImageGrab.grab().load()[xPixelDesktop,yPixelDesktop] != pixelDesktop):
			clicarSairJogo()
			sleep(3)

			#A cada minuto faz algo
			if(timer%60 == 0):
				subirNivel(1)
				comprarCampeoes(1)
			#

			timer = timer + 3
		#

		print("Go next..")

		#Espera alguns segundos até que o jogo feche e maximiza a janela do Client
		sleep(10)
		win32gui.SetForegroundWindow(leagueClient)
		win32gui.BringWindowToTop(leagueClient)
		sleep(5)

		#Clica no botão de jogar novamente
		clicarJogarNovamente()

except KeyboardInterrupt:
	print('\n')
#