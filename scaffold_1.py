import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)



pygame.init()

# Setting the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Candy Game")

# Looping until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

X = 200
Y = 60
speed=5

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# ------- Background ------            
	screen.fill(GREY)

	# --- Drawing code should go here
	pygame.draw.circle(screen, RED, (X,Y),30)
	X += speed
	Y += speed

	# --- Update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(120)

# Close the window and quit.
pygame.quit()

exit() # Needed when using IDLE




