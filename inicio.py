import pygame, sys
from pygame.locals import *
from debug import draw_text
from settings import *
def fechar():
	pygame.quit()
	sys.exit()
def inicio(main):
	screen = pygame.display.get_surface()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				fechar()
			if event.type == KEYDOWN:
				if event.key == K_q:
					fechar()
					main.main()

			screen.fill((0, 0, 0))
			draw_text("DODGER GAME!", (255, 50, 30), 50, screen, WIDTH//3 - 130, HEIGHT//3 - 90)
			draw_text("BEM VINDO", (255, 255, 255), 36, screen, WIDTH//3 - 36, HEIGHT//3 - 10)
			draw_text("Aperte qualquer tecla para começar.", (255, 255, 255), 24, screen, WIDTH//3 - 125, HEIGHT//3 + 80)
			draw_text("Aperte Q para sair", (240, 240, 240), 20, screen, WIDTH//3 - 20, HEIGHT//3 + 150)
		pygame.display.update()
		return