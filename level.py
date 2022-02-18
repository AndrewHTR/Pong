import pygame
from settings import *
from player import Player
from tile import Tile
from enemy import Enemy
from ball import Ball

class Level:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()

		self.visible_sprites   = pygame.sprite.Group()
		self.active_sprites    = pygame.sprite.Group()
		self.collision_sprites = pygame.sprite.Group()

		self.setup_level()


	def setup_level(self):
		for yindex, row in enumerate(LEVEL_MAP):
			for xindex, col in enumerate(row):
				x = xindex * TILE_SIZE
				y = yindex * TILE_SIZE
				if col == 'P':
					Player((x, y), [self.visible_sprites, self.active_sprites, self.collision_sprites])
				if col == 'X':
					Tile((x, y), [self.visible_sprites, self.active_sprites])
				if col == 'E':
					Enemy((x - 40, y), [self.visible_sprites, self.active_sprites, self.collision_sprites])
				if col == 'O':
					Ball(x + 5, y + 40, [self.visible_sprites, self.active_sprites], self.collision_sprites)


	def run(self):
		self.active_sprites.update()
		self.visible_sprites.draw(self.display_surface)
