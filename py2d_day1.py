
import pygame, random
from pygame.locals import *
from random import randint

class py2d:
	def __init__(self, engine_dict, game_ch):
		pygame.init()
		
		self.screen_width = engine_dict['width']
		self.screen_height = engine_dict['height']
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), SCALED|FULLSCREEN)
		self.main_col1, self.main_col2, self.main_col3 = engine_dict['main_col1'], engine_dict['main_col2'], engine_dict['main_col3']
		self.main_col = (self.main_col1, self.main_col2, self.main_col3)
		
		self.clock = pygame.time.Clock()
		self.fps = engine_dict['fps']
		
		self.characters = []
		for ch in game_ch:
			self.characters.append(character(ch))
		
		self.running = True
		
	
	def run_engine(self):
		while self.running:
			self.screen.fill(self.main_col)
			
			for ch in self.characters:
				ch.draw(self.screen)
				ch.move(self.screen_width)
			
			self.update()
	
	def update(self):
		self.clock.tick(self.fps)
		pygame.display.update()


class character:
	def __init__(self, game_dict):
		self.x = game_dict['x']
		self.y = game_dict['y']
		self.width = game_dict['width']
		self.height = game_dict['height']
		self.vel = game_dict['vel']
		self.max_vel = game_dict['max_vel']
		self.acceleration = game_dict['acc']
		self.col1, self.col2, self.col3 = game_dict['col1'], game_dict['col2'], game_dict['col3']
		self.col = (self.col1, self.col2, self.col3)
		self.shape = 'rect'
	
	def draw(self, screen):
		if self.shape == 'rect':
			self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
			pygame.draw.rect(screen, self.col, self.rect)
	
	def move(self, screen_width):
		self.x -= self.vel
		
		if self.vel < self.max_vel:
			self.vel += self.acceleration
		
		if self.x >= screen_width:
			self.x = 1
		if self.x <= 0:
			self.x = screen_width


POS = [(1, 50), (1, 150), (1, 250), (1, 350)]

ENGINE_DICT = {
'width': 540,
'height': 890,
'fps': 60,
'main_col1': 100,
'main_col2': 100,
'main_col3': 130
}

GAME_CH = []
for i in range(len(POS)):
	GAME_CH.append(
	{
	'x': POS[i][0],
	'y': POS[i][1],
	'width': 60,
	'height': 60,
	'vel': 0,
	'max_vel': randint(1, 10),
	'acc': (randint(1, 10)/100),
	'col1': randint(0, 255),
	'col2': randint(0, 255),
	'col3': randint(0, 255),
	'shape': 'rect'
	}
)

engine = py2d(ENGINE_DICT, GAME_CH)
engine.run_engine()
