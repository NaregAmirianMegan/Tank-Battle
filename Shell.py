from pygame.draw import circle
import math

class Shell():

	def __init__(self, startX, startY, startAngle):
		self.xPos = startX
		self.yPos = startY
		self.theta = startAngle
		self.moveRate = 0.3
		self.lifeTime = 5 #decrement every time it bounces off of the wall

	def calcDeltaX(self):
		return self.moveRate*math.cos(math.radians(self.theta))

	def calcDeltaY(self):
		return self.moveRate*math.sin(math.radians(self.theta))

	# def calcDeflectionAngle(self, Boundary):

	def move(self):
		self.xPos += self.calcDeltaX()
		self.yPos += self.calcDeltaY()

	def render(self, screen):
		circle(screen, (0, 0, 0), (int(self.xPos), int(self.yPos)), 5, 0)
