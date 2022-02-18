import pygame

def draw_text(texto, color, tamanho, surface, x, y):
	font = pygame.font.SysFont("Arial", 32)
	textobj = font.render(texto, True, color)
	textrect = textobj.get_rect()
	textrect.center = (x, y)
	surface.blit(textobj, textrect)

def display_fps(clock):
	screen = pygame.display.get_surface()

	draw_text(str(int(clock.get_fps())),'#ffffff', screen, 20, 20)