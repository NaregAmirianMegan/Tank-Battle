# import pygame, os
# from pygame.locals import *

# x = 500
# y = 100
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# WINDOW_HEIGHT = 600
# WINDOW_WIDTH = 800

# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption('Game Window')
# clock = pygame.time.Clock()

# imageSurf = pygame.image.load(os.path.join('images', 'tank.png')).convert()

# def game_loop():
# 	run_game = True

# 	count = 0

# 	while(run_game):
# 		for event in pygame.event.get():
# 			if(event.type == pygame.QUIT):
# 				pygame.quit()
# 				quit()
# 		screen.fill((255, 255, 255))
# 		rotImage = pygame.transform.rotate(imageSurf, count)
# 		screen.blit(rotImage, (100, 100))
# 		pygame.display.update()
# 		clock.tick(1)
# 		count += 10

# game_loop()


import pygame as pg


def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    # Rotate the original image without modifying it.
    new_image = pg.transform.rotate(image, angle)
    # Get a new rect with the center of the old rect.
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect


def main():
    clock = pg.time.Clock()
    screen = pg.display.set_mode((640, 480))
    gray = pg.Color('gray15')
    blue = pg.Color('dodgerblue2')

    image = pg.Surface((320, 200), pg.SRCALPHA)
    pg.draw.polygon(image, blue, ((0, 0), (320, 100), (0, 200)))
    # Keep a reference to the original to preserve the image quality.
    orig_image = image
    rect = image.get_rect(center=(320, 240))
    angle = 0

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        angle += 2
        if(angle == 360):
        	angle = 0
        image, rect = rotate(orig_image, rect, angle)

        screen.fill(gray)
        screen.blit(image, rect)
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()