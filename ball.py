import pygame
from settings import *
import random
from debug import *

class Ball(pygame.sprite.Sprite):
	def __init__(self, x, y, group, collision_sprites):
		super().__init__(group)
		self.image = pygame.Surface((25, 25))
		self.image.fill(PLAYER_COLOR)
		self.rect = self.image.get_rect(center = (x, y))

		self.bounce = pygame.mixer.Sound('bounce.wav')

		self.direction = pygame.math.Vector2()
		self.speed = 6

		self.x = random.choice((1,-1))
		self.y = random.choice((1,-1))

		self.x_back = x
		self.y_back = y

		self.pontos = 0

		self.collision_sprites = collision_sprites

	def movement(self):
		#keys = pygame.key.get_pressed()
		#if keys[pygame.K_SPACE]:
			self.direction.y = self.y
			self.direction.x = self.x

	def collision(self):
		# Colisão com borda da tela
		if self.rect.top <= 0:
			if self.direction.x == -1 and self.direction.y == -1:
				self.y = 1
				self.x = -1
				#draw_text("Colidiu ", (255, 255, 255), 20, pygame.display.get_surface(), 60, 40)
			else:
				self.y = 1
				self.x = 1

		if self.rect.bottom >= HEIGHT:
			if self.direction.x == 1 and self.direction.y == 1:
				self.y = -1
			else: 
				self.y = -1
				self.x = -1
			#draw_text("Colidiu ", (255, 255, 255), 20, pygame.display.get_surface(), 60, 40)

		# Checando se existe colisão com algum objeto
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				# Colisão com raquete do player
				if self.direction.x == -1 and self.direction.y == -1:
					self.y = -1
					self.x = 1

				if self.direction.x == -1 and self.direction.y == 1:
					self.y = 1
					self.x = 1

				# Colisão com a raquete inimiga
				if self.direction.x == 1 and self.direction.y == -1:
					self.y = -1
					self.x = -1

				if self.direction.x == 1 and self.direction.y == 1:
					self.y = 1
					self.x = -1

				self.bounce.play()
	def pontuacao(self):
		draw_text(f"Pontuação: {str(f'{self.pontos}')}", (255, 255, 255), 20, pygame.display.get_surface(), 120, 40)
		if self.rect.x <= 0:
			self.pontos -= 1
			self.reiniciar()
			self.direction.y = random.choice((1,-1))
			self.direction.x = random.choice((1,-1))
		if self.rect.x >= WIDTH:
			self.pontos += 1
			self.reiniciar()
			self.direction.y = random.choice((1,-1))
			self.direction.x = random.choice((1,-1))


	def reiniciar(self):
		self.rect.x = self.x_back
		self.rect.y = self.y_back

	def update(self):
		self.collision()
		self.movement()
		self.rect.y += self.direction.y * self.speed
		self.rect.x += self.direction.x * self.speed
		self.pontuacao()