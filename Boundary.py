from pygame.draw import line

class Boundary():
	
	def __init__(self, a, b, color):
		self.a = a
		self.b = b
		self.color = color

	def render(self, screen):
		line(screen, self.color, self.a, self.b, 2)