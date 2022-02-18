import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)
		self.image = pygame.Surface((TILE_SIZE // 6 , TILE_SIZE + 20))
		self.image.fill(PLAYER_COLOR)
		self.rect = self.image.get_rect(topleft = pos)

	def update(self):
		pass