from pygame.draw import circle
import math

def pointDistance(a, b):
		deltaX = b[0] - a[0]
		deltaY = b[1] - a[1]
		return math.sqrt(math.pow(deltaX, 2) + math.pow(deltaY, 2))


class Shell():

	def __init__(self, startX, startY, startAngle):
		self.xPos = startX
		self.yPos = startY
		self.theta = startAngle
		self.moveRate = 0.3
		self.lifeTime = 5 #decrement every time it bounces off of the wall
		self.delay = 15

	def calcDeltaX(self):
		return self.moveRate*math.cos(math.radians(self.theta))

	def calcDeltaY(self):
		return self.moveRate*math.sin(math.radians(self.theta))

	def calcVerticalDeflectionAngle(self):
		if(self.theta < 0):
			posTheta = self.theta + 360
		else:
			posTheta = self.theta

		if(posTheta == 270):
			self.theta = 90
		elif(posTheta == 90):
			self.theta = 270
		elif(180 >= posTheta >= 0):
			self.theta = 180 - posTheta
		elif(360 >= posTheta > 180):
			self.theta = 540 - posTheta
			
	def calcHorizontalDeflectionAngle(self):
		if(self.theta == 0):
			self.theta = 180
		elif(self.theta == 180 or self.theta == -180):
			self.theta = 0
		elif(self.theta > 0):
			self.theta = self.theta * -1
		else:
			self.theta = abs(self.theta)


	def onPlayer(self, player):
		x = self.xPos
		y = self.yPos
		x1 = player.pointA[0]
		x2 = player.pointB[0]
		x3 = player.pointC[0]
		y1 = player.pointA[1]
		y2 = player.pointB[1]
		y3 = player.pointC[1]

		a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
		b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
		c = 1 - a - b

		if(0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1):
			return True
		else:
			return False

	def onPlayerShield(self, player):
		if(pointDistance((self.xPos, self.yPos), (player.x, player.y)) <= player.shieldRadius):
			return True
		else:
			return False

	def checkHit(self, player):
		if(player.shieldHealth <= 0):
			if(self.onPlayer(player) and self.delay <= 0):
				player.health -= 25
				return True
			else:
				return False
		else:
			if(self.onPlayerShield(player) and self.delay <= 0):
				player.shieldHealth -= 25
				player.health -= 25
				return True
			else:
				return False

	def checkBounce(self, boundary):
		if(not boundary.isHorizontal): 
			if(int(self.xPos) == boundary.xVal and boundary.yMax >= self.yPos >= boundary.yMin):
				self.lifeTime -= 1
				self.calcVerticalDeflectionAngle()
		else: 
			if(int(self.yPos) == boundary.yVal and boundary.xMax >= self.xPos >= boundary.xMin):
				self.lifeTime -= 1
				self.calcHorizontalDeflectionAngle()

	def move(self):
		self.delay -= 0.1
		self.xPos += self.calcDeltaX()
		self.yPos += self.calcDeltaY()

	def render(self, screen):
		circle(screen, (255, 0, 0), (int(self.xPos), int(self.yPos)), 3, 0)
