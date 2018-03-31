import pygame, os

WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

def mouse_on_box(xPos, yPos, width, height, mousePosition):
	if(mousePosition[0] > xPos and mousePosition[0] < xPos+width):
		if(mousePosition[1] > yPos and mousePosition[1] < yPos+height):
			return True
	return False

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

def end_screen(currentScore, screen):
	run_game = True

	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS', 29)
	clock = pygame.time.Clock()

	endMatchTextP1 = ('PLAYER ONE: '+str(currentScore[0]))
	endMatchP1 = myfont.render(endMatchTextP1, False, RED)
	endMatchTextP2 = ('PLAYER TWO: '+str(currentScore[1]))
	endMatchP2 = myfont.render(endMatchTextP2, False, RED)
	quitLabel = myfont.render('QUIT', False, WHITE)
	startLabel = myfont.render('START?', False, WHITE)

	while(run_game):

		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				quit()

				#TODO: fix rectangle
		if(pygame.mouse.get_pressed()[0] == True):
			if(mouse_on_box(WINDOW_WIDTH/4, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50, pygame.mouse.get_pos())):
				pygame.draw.rect(screen, RED, (WINDOW_WIDTH/4, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
				pygame.draw.rect(screen, GREY, (WINDOW_WIDTH-WINDOW_WIDTH/3, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
				pygame.display.update()
				pygame.time.wait(50)
				pygame.quit()
				quit()
			if(mouse_on_box(WINDOW_WIDTH-WINDOW_WIDTH/3, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50, pygame.mouse.get_pos())):
				pygame.draw.rect(screen, GREY, (WINDOW_WIDTH/4, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
				pygame.draw.rect(screen, GREEN, (WINDOW_WIDTH-WINDOW_WIDTH/3, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
				pygame.display.update()
				pygame.time.wait(50)
				break
		else:
			pygame.draw.rect(screen, 
				GREY, (WINDOW_WIDTH/4, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
			pygame.draw.rect(screen, 
				GREY, (WINDOW_WIDTH-WINDOW_WIDTH/3, 
					WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))

		screen.fill(BLACK)
		screen.blit(endMatchP1, (100, 300))
		screen.blit(endMatchP2, (500, 300))
		screen.blit(quitLabel, (WINDOW_WIDTH/4, WINDOW_HEIGHT-WINDOW_HEIGHT/3))
		screen.blit(startLabel, (WINDOW_WIDTH-WINDOW_WIDTH/3, WINDOW_HEIGHT-WINDOW_HEIGHT/3))

		pygame.display.update()
		clock.tick(15)

class Game:

	def __init__(self, boundaryArray, playerArray, screen, currentScore):
		self.boundaries = boundaryArray
		self.shells = []
		self.players = playerArray
		self.screen = screen
		self.currentScore = currentScore

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
						if(player.shoot(event) != None and player.shotDelay <= 0): 
							self.shells.append(player.shoot(event))
							player.shotDelay = 500

			self.screen.fill(WHITE)

			for player in self.players:
				if(player.health <= 0):
					if(player.id == 1):
						winner = 2
						self.currentScore[1] = self.currentScore[1] + 1
					else:
						winner = 1
						self.currentScore[0] = self.currentScore[0] + 1
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

		end_screen(self.currentScore, self.screen)
		return self.currentScore
