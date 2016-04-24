import pygame, sys
from math import pi, sin, cos, radians

pygame.init()
clock = pygame.time.Clock()

class car_sprit(pygame.sprite.Sprite):
	def __init__(self, height, length, position_x, position_y, direction):

		pygame.sprite.Sprite.__init__(self)
		self.car = pygame.image.load("car.png").convert()

		self.car_rect = self.car.get_rect(center = (position_x, position_y))
		self.x_position, self.y_position = self.car_rect.x, self.car_rect.y

		self.height = height
		self.length = length
		self.current_direction = (-1) * direction

		rotate = pygame.transform.rotate
		self.display_car = rotate(self.car, direction)


	def display(self, screen):

		screen.blit(self.display_car, self.car_rect)


	def movement(self, left_velocity, right_velocity, position_x, position_y, current_direction):

		#finding the radius of the circle that car turning around
		if right_velocity != left_velocity:
			faster_right_radius = (left_velocity * self.height) / (right_velocity - left_velocity)
			faster_left_radius = (right_velocity * self.height) / (left_velocity - right_velocity)

		elif right_velocity == left_velocity:
			faster_right_radius = 0
			faster_left_radius = 0
			self.x_velocity = (-1) * right_velocity * cos(radians(self.current_direction))
			self.y_velocity = right_velocity * sin(radians(self.current_direction))


		#finding partial velocity according to car_angle
		if right_velocity >= left_velocity and faster_right_radius != 0:
			self.current_direction += (float(left_velocity) / (2.0 * pi * faster_right_radius) * 360)
			self.current_direction = self.current_direction%360

			self.x_velocity = (-1) * faster_right_radius * cos(radians(self.current_direction))
			self.y_velocity = faster_right_radius * sin(radians(self.current_direction))

		elif left_velocity >= right_velocity and faster_left_radius != 0:
			self.current_direction += ((-1) * (float(right_velocity) / (2.0 * pi * faster_left_radius) * 360))
			self.current_direction = self.current_direction%360

			self.x_velocity = (-1) * faster_left_radius * cos(radians(self.current_direction))
			self.y_velocity =  faster_left_radius * sin(radians(self.current_direction))

		elif faster_left_radius != 0 or faster_right_radius != 0:
			self.x_velocity = 0
			self.y_velocity = 0

		self.car_rect = self.car_rect.move(self.x_velocity, self.y_velocity)
		self.x_position, self.y_position = self.car_rect.x, self.car_rect.y

		rotate = pygame.transform.rotate
		self.display_car = rotate(self.car, self.current_direction)




######### Test cases ##########
size = widht , height = 1200, 600
screen = pygame.display.set_mode(size)
car_red = car_sprit(32, 16, 600, 300, 10) #heigh, length, position_x, position_y, first_direction
t = 0

while True:
	screen.fill((255, 255, 255))

	if t < 110:
		car_red.movement(2, 8, car_red.x_position, car_red.y_position, car_red.current_direction)
		car_red.display(screen)
	elif t < 130:
		car_red.movement(8, 8, car_red.x_position, car_red.y_position, car_red.current_direction)
		car_red.display(screen)
	elif 130 < t:
		t = 0


	pygame.display.update()
	t += 1
	clock.tick(60)