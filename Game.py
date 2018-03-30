import pygame, os

WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)

def explosion_animation(x, y, screen, boundaryArray, playerArray, shellArray):
	run_animation = True
	imgSequence = []
	frameCount = 0

	for img in os.listdir('./images'):
		imgSequence.append(pygame.image.load(os.path.join('./images', img)).convert())

	while(run_animation):
		if(frameCount%30 == 0):
			screen.blit(imgSequence[int(frameCount/30)], (x, y))

		for bound in boundaryArray:
			bound.render(screen)

		for player in playerArray:
			player.render(screen)

		for shell in shellArray:
			shell.render(screen)

		pygame.display.update()

		if(frameCount/30 == len(imgSequence)-1):
			run_animation = False

		frameCount += 1

def end_screen(winner, screen):
	run_game = True

	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS', 29)

	endMatchText = ('PLAYER '+str(winner)+' WINS!!!')
	endMatch = myfont.render(endMatchText, False, RED)

	while(run_game):

		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				quit()

		screen.fill(BLACK)
		screen.blit(endMatch, (300, 300))
		pygame.display.update()


class Game:

	def __init__(self, boundaryArray, playerArray, screen):
		self.boundaries = boundaryArray
		self.shells = []
		self.players = playerArray
		self.screen = screen

	def run(self):
		run_game = True

		self.screen.fill(WHITE)

		while(run_game):
			keys = pygame.key.get_pressed()

			for player in self.players:
				player.move(keys)
				for boundary in self.boundaries:
					player.detectCollision(boundary)
					if(player.collideWithWall):
						break

			for shell in self.shells:
				shell.move()
				if(shell.lifeTime == 0):
					self.shells.remove(shell)
				for player in self.players:
					if(shell.checkHit(player)):
						self.shells.remove(shell)

			self.players[0].checkCollision(self.players[1])
			self.players[1].checkCollision(self.players[0])
				
			for boundary in self.boundaries:
				for shell in self.shells:
					shell.checkBounce(boundary)

			for event in pygame.event.get():
				if(event.type == pygame.QUIT):
					pygame.quit()
					quit()
				elif(event.type == pygame.KEYDOWN):
					for player in self.players:
						if(player.shoot(event) != None): 
							self.shells.append(player.shoot(event))

			self.screen.fill(WHITE)

			for player in self.players:
				if(player.health <= 0):
					if(player.id == 1):
						winner = 2
					else:
						winner = 1
					self.players.remove(player)
					explosion_animation(player.x, player.y, self.screen, self.boundaries, self.players, self.shells)
					pygame.time.wait(500)
					run_game = False

			for boundary in self.boundaries:
				boundary.render(self.screen)

			for player in self.players:
				player.render(self.screen)

			for shell in self.shells:
				shell.render(self.screen)

			pygame.display.update()

		end_screen(winner, self.screen)
