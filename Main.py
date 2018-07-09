#import external files
from Player import Player
from Boundary import Boundary
from Shell import Shell
from Game import Game

#import pygame and system
import pygame, os
from pygame.locals import *
from random import randint
import math

print("Game loading...")

#set window position
x = 500
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#setup pygame
pygame.init()
#setup text font
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 29)

#set game constants
#set window size
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

#colors
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)

#create pygame display and frame clock
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Game Window')
clock = pygame.time.Clock()

#setup global variables for the program
boundaryArray = []
playerArray = []
title = myfont.render('Tank Battle', False, BLACK)
quitLabel = myfont.render('QUIT', False, WHITE)
startLabel = myfont.render('START', False, WHITE)

def mouse_on_box(xPos, yPos, width, height, mousePosition):
	if(mousePosition[0] > xPos and mousePosition[0] < xPos+width):
		if(mousePosition[1] > yPos and mousePosition[1] < yPos+height):
			return True
	return False

def game_menu():
	run_menu = True

	while(run_menu):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				quit()

		screen.fill(GREY)
		if(pygame.mouse.get_pressed()[0] == True):
			if(mouse_on_box(WINDOW_WIDTH/4, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50, pygame.mouse.get_pos())):
				pygame.draw.rect(screen, RED, (WINDOW_WIDTH/4, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
				pygame.draw.rect(screen, BLACK, (WINDOW_WIDTH-WINDOW_WIDTH/3, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
				pygame.display.update()
				pygame.time.wait(50)
				pygame.quit()
				quit()
			if(mouse_on_box(WINDOW_WIDTH-WINDOW_WIDTH/3, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50, pygame.mouse.get_pos())):
				pygame.draw.rect(screen, BLACK, (WINDOW_WIDTH/4, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
				pygame.draw.rect(screen, GREEN, (WINDOW_WIDTH-WINDOW_WIDTH/3, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
				pygame.display.update()
				pygame.time.wait(50)
				break
		else:
			pygame.draw.rect(screen, 
				BLACK, (WINDOW_WIDTH/4, WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
			pygame.draw.rect(screen, 
				BLACK, (WINDOW_WIDTH-WINDOW_WIDTH/3, 
					WINDOW_HEIGHT-WINDOW_HEIGHT/3, 100, 50))
		screen.blit(title, (WINDOW_WIDTH/3+55, WINDOW_HEIGHT/3))
		screen.blit(quitLabel, (WINDOW_WIDTH/4, WINDOW_HEIGHT-WINDOW_HEIGHT/3))
		screen.blit(startLabel, (WINDOW_WIDTH-WINDOW_WIDTH/3, WINDOW_HEIGHT-WINDOW_HEIGHT/3))	
		pygame.display.update()
		clock.tick(15)

#options to quit or play again
def final_screen(score):
	run = True

	header = myfont.render('WINNER: ', False, WHITE)
	if(score[0] > score[1]):
		winnerText = 'Player One'
	else:
		winnerText = 'Player Two'
	winningPlayer = myfont.render(winnerText, False, WHITE)

	while(run):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				quit()

		screen.fill(BLACK)

		screen.blit(header, (350, 100))
		screen.blit(winningPlayer, (350, 300))
		pygame.display.update()



boundaryArray.append( Boundary((0, 0), (0, WINDOW_HEIGHT), BLACK) )
boundaryArray.append( Boundary((0, 0), (WINDOW_WIDTH, 0), BLACK) )
boundaryArray.append( Boundary((0, WINDOW_HEIGHT), (WINDOW_WIDTH, WINDOW_HEIGHT), BLACK) )
boundaryArray.append( Boundary((WINDOW_WIDTH, 0), (WINDOW_WIDTH, WINDOW_HEIGHT), BLACK) )
boundaryArray.append( Boundary((WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT/2), BLACK) )

playerArray.append( Player(100, 100, GREEN, 45, 1) )
playerArray.append( Player(700, 100, RED, 135, 2) )

game1 = Game(boundaryArray, playerArray, screen, [0, 0])

game_menu()
print("Game loaded.")


nextScore = game1.run()


boundaryArray.append( Boundary((0, 500), (300, 500), BLACK) )
boundaryArray.append( Boundary((500, 500), (800, 500), BLACK) )

playerArray = []
playerArray.append( Player(100, 100, GREEN, 45, 1) )
playerArray.append( Player(700, 100, RED, 135, 2) )

game2 = Game(boundaryArray, playerArray, screen, nextScore)

nextScore = game2.run()


boundaryArray.append( Boundary((0, 200), (200, 200), BLACK) )
boundaryArray.append( Boundary((600, 200), (800, 200), BLACK) )

playerArray = []
playerArray.append( Player(100, 100, GREEN, 45, 1) )
playerArray.append( Player(700, 100, RED, 135, 2) )

game3 = Game(boundaryArray, playerArray, screen, nextScore)

nextScore = game3.run()


final_screen(nextScore)