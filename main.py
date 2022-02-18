import pygame, sys
from pygame.locals import *
from settings import *
from level import Level
from debug import *


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

level = Level()

def fechar():
	pygame.quit()
	sys.exit()

def inicio():
	screen = pygame.display.get_surface()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				fechar()
			if event.type == KEYDOWN:
				if event.key == K_q:
					fechar()
				main()

			screen.fill((0, 0, 0))
			draw_text("PONG!", (20, 50, 255), 500, screen, WIDTH//2 , 0 + 200)
			draw_text("BEM VINDO", (255, 255, 255), 36, screen, WIDTH//2, HEIGHT//3 + 20)
			draw_text("Aperte qualquer tecla para começar.", (255, 255, 255), 24, screen, WIDTH//2, HEIGHT//3 + 80)
			draw_text("Aperte Q para sair", (240, 240, 240), 15, screen, WIDTH//2, HEIGHT//3 + 200)
		pygame.display.update()

def main():
	while True:
		screen.fill(BG_COLOR)

		for event in pygame.event.get():
			if event.type == QUIT:
				fechar()
			if event.type == KEYDOWN:
				if event.key == K_q:
					fechar()

		level.run()
		#display_fps(clock)
		pygame.display.update()
		clock.tick(60)
inicio()