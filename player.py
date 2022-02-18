import pygame
from settings import *
from debug import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)
		self.image = pygame.Surface((TILE_SIZE // 3 + 5, TILE_SIZE + 60))
		self.image.fill(PLAYER_COLOR)
		self.rect = self.image.get_rect(topleft = pos)

		self.direction = pygame.math.Vector2()
		self.speed = 8

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
			if self.rect.y == 0:
				self.direction.y = 0
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

	def collision(self):
		if self.rect.top <= 0:
			#if self.direction == -1:
			self.rect.y = 0 
			#draw_text("Colidiu ",(255, 255, 255), 20, pygame.display.get_surface(), 60, 40)
		if self.rect.bottom >= HEIGHT:
			self.rect.y = HEIGHT - (TILE_SIZE + 61)


	def update(self):
		self.input()
		self.collision()
		self.rect.y += self.direction.y * self.speed
