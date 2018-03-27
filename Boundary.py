from pygame.draw import line

class Boundary():
	
	def __init__(self, x1, x2, y1, y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

	def render(self, screen):
		line(screen, (255, 255, 255), (self.x1, self,y1), (self.x2, self.y2), 2)