import pygame, math
from Shell import Shell

def pointDistance(a, b):
		deltaX = b[0] - a[0]
		deltaY = b[1] - a[1]
		return math.sqrt(math.pow(deltaX, 2) + math.pow(deltaY, 2))

class Player():

	def __init__(self, startX, startY, color, startAngle, playerID):
		self.x = startX
		self.y = startY
		self.rotRate = 0.3
		self.moveRate = 0.2
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
		self.shieldRadius = int(self.radius) + 10
		self.direction = 0
		self.collideWithPlayer = False
		self.collideWithWall = False
		self.shieldHealth = 250
		self.shieldWidth = 3
		self.health = self.shieldHealth + 50

	def calcDeltaX(self):
		return self.moveRate*math.cos(math.radians(self.theta))

	def calcDeltaY(self):
		return self.moveRate*math.sin(math.radians(self.theta))

	def checkCollision(self, otherPlayer):
		if(pointDistance((self.x, self.y), (otherPlayer.x, otherPlayer.y)) <= 2*self.shieldRadius):
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
				if(not self.collideWithWall):
					self.theta -= self.rotRate
				else:
					self.theta += self.theta/10
				self.updatePoints()
			if(keys[pygame.K_d]):
				if(not self.collideWithWall):
					self.theta += self.rotRate
				else:
					self.theta -= self.theta/10
				self.updatePoints()
			if(keys[pygame.K_w]):
				if(self.direction == 1 and self.collideWithWall == True):
					self.x = self.x - self.calcDeltaX()
					self.y = self.y - self.calcDeltaY()
				if(self.direction == 1 and self.collideWithPlayer == True):
					if(self.shieldHealth != 0):
						self.shieldHealth -= 1
						self.health -= 1
					self.x = self.x - self.calcDeltaX()
					self.y = self.y - self.calcDeltaY()
				else:
					self.x = self.x + self.calcDeltaX()
					self.y = self.y + self.calcDeltaY()
				self.direction = 1
				self.updatePoints()
			if(keys[pygame.K_s]):
				if(self.direction == -1 and self.collideWithWall == True):
					self.x = self.x + self.calcDeltaX()
					self.y = self.y + self.calcDeltaY()
				if(self.direction == -1 and self.collideWithPlayer == True):
					if(self.shieldHealth != 0):
						self.shieldHealth -= 1
						self.health -= 1
					self.x = self.x + self.calcDeltaX()
					self.y = self.y + self.calcDeltaY()
				else:
					self.x = self.x - self.calcDeltaX()
					self.y = self.y - self.calcDeltaY()
				self.direction = -1
				self.updatePoints()
		elif(self.id == 2):
			if(keys[pygame.K_LEFT]):
				if(not self.collideWithWall):
					self.theta -= self.rotRate
				else:
					self.theta += self.theta/10
				self.updatePoints()
			if(keys[pygame.K_RIGHT]):
				if(not self.collideWithWall):
					self.theta += self.rotRate
				else:
					self.theta -= self.theta/10
				self.updatePoints()
			if(keys[pygame.K_UP]):
				if(self.direction == 1 and self.collideWithWall == True):
					self.x = self.x - self.calcDeltaX()
					self.y = self.y - self.calcDeltaY()
				if(self.direction == 1 and self.collideWithPlayer == True):
					if(self.shieldHealth != 0):
						self.shieldHealth -= 1
						self.health -= 1
					self.x = self.x - self.calcDeltaX()
					self.y = self.y - self.calcDeltaY()
				else:
					self.x = self.x + self.calcDeltaX()
					self.y = self.y + self.calcDeltaY()
				self.direction = 1
				self.updatePoints()
			if(keys[pygame.K_DOWN]):
				if(self.direction == -1 and self.collideWithWall == True):
					self.x = self.x + self.calcDeltaX()
					self.y = self.y + self.calcDeltaY()
				if(self.direction == -1 and self.collideWithPlayer == True):
					if(self.shieldHealth != 0):
						self.shieldHealth -= 1
						self.health -= 1
					self.x = self.x + self.calcDeltaX()
					self.y = self.y + self.calcDeltaY()
				else:
					self.x = self.x - self.calcDeltaX()
					self.y = self.y - self.calcDeltaY()
				self.direction = -1
				self.updatePoints()

	def getHighestPoint(self):
		y1 = self.pointA[1]
		y2 = self.pointB[1]
		y3 = self.pointC[1]
		pointList = []
		pointList.append(y1)
		pointList.append(y2)
		pointList.append(y3)
		return max(pointList)

	def getLowestPoint(self):
		y1 = self.pointA[1]
		y2 = self.pointB[1]
		y3 = self.pointC[1]
		pointList = []
		pointList.append(y1)
		pointList.append(y2)
		pointList.append(y3)
		return min(pointList)

	def getLeftmostPoint(self):
		x1 = self.pointA[0]
		x2 = self.pointB[0]
		x3 = self.pointC[0]
		pointList = []
		pointList.append(x1)
		pointList.append(x2)
		pointList.append(x3)
		return max(pointList)

	def getRightmostPoint(self):
		x1 = self.pointA[0]
		x2 = self.pointB[0]
		x3 = self.pointC[0]
		pointList = []
		pointList.append(x1)
		pointList.append(x2)
		pointList.append(x3)
		return min(pointList)

	def detectCollision(self, boundary):
		rightmostBound = self.getRightmostPoint()
		leftmostBound = self.getLeftmostPoint()
		upperBound = self.getHighestPoint()
		lowerBound = self.getLowestPoint()

		if(boundary.a[0] == boundary.b[0]): 
			if(boundary.a[1] > boundary.b[1]):
				greaterY = boundary.a[1]
				lesserY = boundary.b[1]
			else:
				lesserY = boundary.a[1]
				greaterY = boundary.b[1]
			if(rightmostBound >= boundary.a[0] >= leftmostBound and (lowerBound < greaterY or upperBound > lesserY)):
				self.collideWithWall = True
			else:
				self.collideWithWall = False
		elif(boundary.a[1] == boundary.b[1]): 
			if(boundary.a[0] > boundary.b[0]):
				greaterX = boundary.a[0]
				lesserX = boundary.b[0] 
			else:
				lesserX = boundary.a[0]
				greaterX = boundary.b[0]
			if(upperBound >= boundary.a[1] >= lowerBound and (leftmostBound < greaterX or rightmostBound > lesserX)):
				self.collideWithWall = True
			else:
				self.collideWithWall = False

	def shoot(self, event):
		if(self.id == 1):
			if(event.key == pygame.K_SPACE):
				return Shell(self.pointA[0], self.pointA[1], self.theta)
		elif(self.id == 2):
			if(event.key == pygame.K_KP_ENTER):
				return Shell(self.pointA[0], self.pointA[1], self.theta)

	def render(self, screen):
		pygame.draw.polygon(screen, self.color, (self.pointA, self.pointB, self.pointC))
		if(self.shieldHealth != 0):
			self.renderShield(screen)
		
	def renderShield(self, screen):
		pygame.draw.circle(screen, (0, (250 - self.shieldHealth), 255), (int(self.x), int(self.y)), self.shieldRadius, self.shieldWidth)