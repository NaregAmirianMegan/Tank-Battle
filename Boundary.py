from pygame.draw import line

class Boundary():
	
	def __init__(self, a, b, color):
		self.a = a
		self.b = b
		self.color = color
		if(a[0] == b[0]):
			self.isHorizontal = False
			self.xVal = a[0]
			if(a[1] > b[1]):
				self.yMin = b[1]
				self.yMax = a[1]
			else:
				self.yMin = a[1]
				self.yMax = b[1]
		else:
			self.isHorizontal = True
			self.yVal = a[1]
			if(a[0] > b[0]):
				self.xMin = b[0]
				self.xMax = a[0]
			else:
				self.xMin = a[0]
				self.xMax = b[0]

	def render(self, screen):
		line(screen, self.color, self.a, self.b, 3)