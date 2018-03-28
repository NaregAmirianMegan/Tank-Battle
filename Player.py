import pygame, math

class Player():

	def __init__(self, startX, startY, color, startAngle, playerID):
		self.x = startX
		self.y = startY
		self.rotRate = 1
		self.moveRate = 1
		self.theta = startAngle
		self.height = 100
		self.base = 50
		self.angle = 90 - math.degrees(math.atan(self.height/self.base))
		self.radius = math.sqrt(math.pow(self.base/2, 2) + math.pow(self.height/2, 2))
		self.pointA = (self.x + (self.height/2)*math.cos(math.radians(self.theta)), self.y + (self.height/2)*math.sin(math.radians(self.theta)))
		self.pointB = (self.x + self.radius*(math.cos(math.radians(self.theta + 180 - self.angle))), 
							self.y + self.radius*(math.sin(math.radians(self.theta + 180 - self.angle))))
		self.pointC = (self.x + self.radius*(math.cos(math.radians(self.theta + 180 + self.angle))), 
							self.y + self.radius*(math.sin(math.radians(self.theta + 180 + self.angle))))
		self.color = color
		self.id = playerID

	def calcDeltaX(self):
		return self.moveRate*math.cos(math.radians(self.theta))

	def calcDeltaY(self):
		return self.moveRate*math.sin(math.radians(self.theta))

	def updatePoints(self):
		self.pointA = (self.x + (self.height/2)*math.cos(math.radians(self.theta)), self.y + (self.height/2)*math.sin(math.radians(self.theta)))
		self.pointB = (self.x + self.radius*(math.cos(math.radians(self.theta + 180 - self.angle))), 
							self.y + self.radius*(math.sin(math.radians(self.theta + 180 - self.angle))))
		self.pointC = (self.x + self.radius*(math.cos(math.radians(self.theta + 180 + self.angle))), 
							self.y + self.radius*(math.sin(math.radians(self.theta + 180 + self.angle))))

	def move(self, keys):
		if(self.theta >= 360 or self.theta <= -360):
				self.theta = 0
		if(self.id == 1):
			if(keys[pygame.K_a]):
				self.theta = self.theta - self.rotRate
				self.updatePoints()
			if(keys[pygame.K_d]):
				self.theta = self.theta + self.rotRate
				self.updatePoints()
			if(keys[pygame.K_w]):
				self.x = self.x + self.calcDeltaX()
				self.y = self.y + self.calcDeltaY()
				self.updatePoints()
			if(keys[pygame.K_s]):
				self.x = self.x - self.calcDeltaX()
				self.y = self.y - self.calcDeltaY()
				self.updatePoints()
		elif(self.id == 2):
			if(keys[pygame.K_LEFT]):
				self.theta = self.theta - self.rotRate
				self.updatePoints()
			if(keys[pygame.K_RIGHT]):
				self.theta = self.theta + self.rotRate
				self.updatePoints()
			if(keys[pygame.K_UP]):
				deltaX = self.calcDeltaX()
				deltaY = self.calcDeltaY()
				self.x += deltaX
				self.y += deltaY
				self.updatePoints()
			if(keys[pygame.K_DOWN]):
				deltaX = self.calcDeltaX()
				deltaY = self.calcDeltaY()
				self.x -= deltaX
				self.y -= deltaY
				self.updatePoints()

	# def shoot(self):

	def render(self, screen):
		pygame.draw.polygon(screen, self.color, (self.pointA, self.pointB, self.pointC))