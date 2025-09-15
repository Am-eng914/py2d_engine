
import pygame, random, math
from pygame.locals import *
from random import randint, uniform
from math import radians

class py2d:
	def __init__(self, engine_dict, game_ch):
		pygame.init()
		
		self.screen_width = engine_dict['width']
		self.screen_height = engine_dict['height']
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), SCALED|FULLSCREEN)
		self.main_col1, self.main_col2, self.main_col3 = engine_dict['main_col1'], engine_dict['main_col2'], engine_dict['main_col3']
		self.main_col = (self.main_col1, self.main_col2, self.main_col3)
		
		self.font_r, self.font_g, self.font_b = engine_dict['font_r'], engine_dict['font_g'], engine_dict['font_b']
		self.font_other_r, self.font_other_g, self.font_other_b = engine_dict['font_other_r'], engine_dict['font_other_g'], engine_dict['font_other_b']
		self.font_col = (self.font_r, self.font_g, self.font_b)
		self.font_other_col = (self.font_other_r, self.font_other_g, self.font_other_b)
		self.font = pygame.font.SysFont(engine_dict['font_name'], engine_dict['font_size'])
		self.render_msg = self.font.render(engine_dict['msg'], True, self.font_col, self.font_other_col)
		
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
			
			self.screen.blit(self.render_msg, (self.screen_width/3, self.screen_height/2.5))
			
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
		self.radius = game_dict['radius']
		self.x1, self.y1 = game_dict['x1'], game_dict['y1']
		self.x2, self.y2 = game_dict['x2'], game_dict['y2']
		self.thickness = game_dict['thickness']
		self.dir = game_dict['dir']
		self.vel = game_dict['vel']
		self.max_vel = game_dict['max_vel']
		self.acceleration = game_dict['acc']
		self.friction = game_dict['friction']
		self.finished = game_dict['finished']
		self.col1, self.col2, self.col3 = game_dict['col1'], game_dict['col2'], game_dict['col3']
		self.col = (self.col1, self.col2, self.col3)
		self.shape = game_dict['shape']
	
	def draw(self, screen):
		if self.shape == 'rect':
			self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
			pygame.draw.rect(screen, self.col, self.rect)
		
		elif self.shape == 'circle':
			pygame.draw.circle(screen, self.col, (self.x, self.y), self.radius)
		
		elif self.shape == 'line':
			pygame.draw.line(screen, self.col, (self.x1 + self.x, self.y1), (self.x2 + self.x, self.y2), self.thickness)
			
	
	def move(self, screen_width):
		
		dy = round(math.sin(self.dir)) * self.vel
		dx = round(math.cos(self.dir)) * self.vel
		
		self.y += dy
		self.x += dx
		
		if (self.vel < self.max_vel) and (not self.finished):
			self.vel += self.acceleration
		
		if self.finished:
			self.vel -= self.friction/2.5
			if self.vel <= 0:
				self.vel = 0
				self.friction = 0
		
		if self.x >= screen_width:
			self.x = 0
			self.finished = True
		elif self.x <= 0:
			self.x = screen_width


POS = [(1, 50), (1, 150), (1, 250), (1, 350)]
DIR = [0, 45, 90, 135, 180, 225, 270, 315]
FONTS = ['freesansbold.ttf', 'Verdana', 'Courier New', 'comicsansms', 'Times New Roman', 'Arial', 'impact', 'georgia', 'calibri', 'dejavusans']

ENGINE_DICT = {
'width': 540,
'height': 890,
'fps': 60,
'main_col1': 100,
'main_col2': 100,
'main_col3': 130,
'font_name': FONTS[0],
'font_size': 40,
'font_r': 90,
'font_g': 110,
'font_b': 100,
'font_other_r': 150,
'font_other_g': 155,
'font_other_b': 245,
'msg': 'race game'
}

GAME_CH = []
for i in range(len(POS)):
	GAME_CH.append(
	{
	'x': POS[i][0],
	'y': POS[i][1],
	'width': 60,
	'height': 60,
	'radius': 10,
	'x1': POS[i][0],
	'y1': POS[i][1],
	'x2': uniform(POS[i][0] + 10, POS[i][0] + 50),
	'y2': POS[i][1],
	'thickness': randint(1, 20),
	'dir': radians(DIR[0]),
	'vel': 0,
	'max_vel': randint(1, 10),
	'acc': (randint(1, 10)/100),
	'friction': 0.1,
	'finished': False,
	'col1': randint(0, 255),
	'col2': randint(0, 255),
	'col3': randint(0, 255),
	'shape': 'rect'
	}
)

engine = py2d(ENGINE_DICT, GAME_CH)
engine.run_engine()2d(ENGINE_DICT, GAME_CH)
engine.run_engine()
