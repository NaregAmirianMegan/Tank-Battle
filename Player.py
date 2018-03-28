import pygame, math

def pointDistance(a, b):
		deltaX = b[0] - a[0]
		deltaY = b[1] - a[1]
		return math.sqrt(math.pow(deltaX, 2) + math.pow(deltaY, 2))

class Player():

	def __init__(self, startX, startY, color, startAngle, playerID):
		self.x = startX
		self.y = startY
		self.rotRate = 0.4
		self.moveRate = 0.4
		self.theta = startAngle
		self.height = 35
		self.base = 15
		self.angle = 90 - math.degrees(math.atan(self.height/self.base))
		self.radius = math.sqrt(math.pow(self.base/2, 2) + math.pow(self.height/2, 2))
		self.pointA = (self.x + (self.height/2)*math.cos(math.radians(self.theta)), self.y + (self.height/2)*math.sin(math.radians(self.theta)))
		self.pointB = (self.x + self.radius*(math.cos(math.radians(self.theta + 180 - self.angle))), 
							self.y + self.radius*(math.sin(math.radians(self.theta + 180 - self.angle))))
		self.pointC = (self.x + self.radius*(math.cos(math.radians(self.theta + 180 + self.angle))), 
							self.y + self.radius*(math.sin(math.radians(self.theta + 180 + self.angle))))
		self.color = color
		self.id = playerID
		self.sheildRadius = int(self.radius) + 10
		self.forward = 0
		self.collideWithPlayer = False

	def calcDeltaX(self):
		return self.moveRate*math.cos(math.radians(self.theta))

	def calcDeltaY(self):
		return self.moveRate*math.sin(math.radians(self.theta))

	def checkCollision(self, otherPlayer):
		if(pointDistance((self.x, self.y), (otherPlayer.x, otherPlayer.y)) <= 2*self.sheildRadius):
			self.collideWithPlayer = True
		else:
			self.collideWithPlayer = False

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
				if(self.forward == 1 and self.collideWithPlayer == True):
					self.x = self.x - self.calcDeltaX()
					self.y = self.y - self.calcDeltaY()
				else:
					self.x = self.x + self.calcDeltaX()
					self.y = self.y + self.calcDeltaY()
				self.forward = 1
				self.updatePoints()
			if(keys[pygame.K_s]):
				if(self.forward == -1 and self.collideWithPlayer == True):
					self.x = self.x + self.calcDeltaX()
					self.y = self.y + self.calcDeltaY()
				else:
					self.x = self.x - self.calcDeltaX()
					self.y = self.y - self.calcDeltaY()
				self.forward = -1
				self.updatePoints()
		elif(self.id == 2):
			if(keys[pygame.K_LEFT]):
				self.theta = self.theta - self.rotRate
				self.updatePoints()
			if(keys[pygame.K_RIGHT]):
				self.theta = self.theta + self.rotRate
				self.updatePoints()
			if(keys[pygame.K_UP]):
				if(self.forward == 1 and self.collideWithPlayer == True):
					self.x = self.x - self.calcDeltaX()
					self.y = self.y - self.calcDeltaY()
				else:
					self.x = self.x + self.calcDeltaX()
					self.y = self.y + self.calcDeltaY()
				self.forward = 1
				self.updatePoints()
			if(keys[pygame.K_DOWN]):
				if(self.forward == -1 and self.collideWithPlayer == True):
					self.x = self.x + self.calcDeltaX()
					self.y = self.y + self.calcDeltaY()
				else:
					self.x = self.x - self.calcDeltaX()
					self.y = self.y - self.calcDeltaY()
				self.forward = -1
				self.updatePoints()

	# def shoot(self):

	def render(self, screen):
		pygame.draw.polygon(screen, self.color, (self.pointA, self.pointB, self.pointC))
		pygame.draw.circle(screen, (0, 50, 255), (int(self.x), int(self.y)), self.sheildRadius, 3)