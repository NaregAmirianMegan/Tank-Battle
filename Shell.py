class Shell():

	def __init__(self, startX, startY, startAngle):
		self.xPos = startX
		self.yPos = startY
		self.theta = startAngle
		self.moveRate = 1
		self.lifeTime = 5 #decrement every time it bounces off of the wall

	# def calcDeflectionAngle(self, Boundary):

	# def move(self):

	# def render(self, screen):
