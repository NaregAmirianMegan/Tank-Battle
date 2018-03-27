import pygame, math

class Player():

	def __init__(self, startX, startY):
		self.x = startX
		self.y = startY
		self.rotRate = 0.01
		self.moveRate = 0.01
		self.theta = 0
		self.height = 1
		self.base = 0.4
		self.angle = 90 - math.degrees(math.atan(self.height/self.base))
		self.radius = math.sqrt(math.pow(self.base/2, 2) + math.pow(self.height/2, 2))
		self.pointA = (self.x + (self.height/2)*math.degrees(math.cos(self.theta)), self.y + (self.height/2)*math.degrees(math.sin(self.theta)))
		self.pointB = (self.x + self.radius*(math.degrees(math.cos(self.theta + (180 - self.angle)))), 
							self.y + self.radius*(math.degrees(math.sin(self.theta + (180 - self.angle)))))
		self.pointC = (self.x + self.radius*(math.degrees(math.cos(self.theta + (180 + 2*self.angle)))), 
							self.y + self.radius*(math.degrees(math.sin(self.theta + (180 + 2*self.angle)))))

		print(self.radius)

	def calcDeltaX(self):
		return self.moveRate*math.degrees(math.cos(self.theta))

	def calcDeltaY(self):
		return self.moveRate*math.degrees(math.sin(self.theta))

	def updatePoints(self):
		self.pointA = (self.x + (self.height/2)*math.degrees(math.cos(self.theta)), self.y + (self.height/2)*math.degrees(math.sin(self.theta)))
		self.pointB = (self.x + self.radius*(math.degrees(math.cos(self.theta + (180 - self.angle)))), 
							self.y + self.radius*(math.degrees(math.sin(self.theta + (180 - self.angle)))))
		self.pointC = (self.x + self.radius*(math.degrees(math.cos(self.theta + (180 + 2*self.angle)))), 
							self.y + self.radius*(math.degrees(math.sin(self.theta + (180 + 2*self.angle)))))

	def move(self, keys, player):
		if(self.theta >= 360 or self.theta <= -360):
				self.theta = 0
		if(player == 1):
			if(keys[pygame.K_a]):
				self.theta = self.theta - self.rotRate
				self.updatePoints()
			if(keys[pygame.K_d]):
				self.theta = self.theta + self.rotRate
				self.updatePoints()
			if(keys[pygame.K_s]):
				self.x = self.x + self.calcDeltaX()
				self.y = self.y + self.calcDeltaY()
				self.updatePoints()
			if(keys[pygame.K_w]):
				self.x = self.x - self.calcDeltaX()
				self.y = self.y - self.calcDeltaY()
				self.updatePoints()
		if(player == 2):
			if(keys[pygame.K_LEFT]):
				self.theta = self.theta - self.rotRate
				self.updatePoints()
			if(keys[pygame.K_RIGHT]):
				self.theta = self.theta + self.rotRate
				self.updatePoints()
			if(keys[pygame.K_DOWN]):
				deltaX = self.calcDeltaX()
				deltaY = self.calcDeltaY()
				self.x = self.x + deltaX
				self.y = self.y + deltaY
				self.pointA[0] + deltaX
				self.pointA[1] + deltaY
				self.pointB[0] + deltaX
				self.pointB[1] + deltaY
				self.pointC[0] + deltaX
				self.pointC[1] + deltaY
			if(keys[pygame.K_UP]):
				deltaX = self.calcDeltaX()
				deltaY = self.calcDeltaY()
				self.x = self.x - deltaX
				self.y = self.y - deltaY
				self.pointA[0] - deltaX
				self.pointA[1] - deltaY
				self.pointB[0] - deltaX
				self.pointB[1] - deltaY
				self.pointC[0] - deltaX
				self.pointC[1] - deltaY
				
	# def shoot(self):

	def render(self, screen):
		pygame.draw.polygon(screen, (0, 255, 0), (self.pointA, self.pointB, self.pointC))
