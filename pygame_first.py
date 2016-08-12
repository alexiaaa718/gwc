# my first pygame file.
import pygame 
# Define some colors
# upper case variables show that they are global
BLACK = (0,0,0)
WHITE = ( 255, 255, 255)
GREEN =(0,255, 0)
RED = (255, 0,0)
BLUE = (0, 0, 255)
# DARK_BLUE = (18, 100, 128)

pygame.init()

#Set thr width and height of the screen [width, height]
screen_size = (700, 700)
my_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("My first game!")

# set the caption of the game
done = False 

 # Used to manage how fast the screen updates
my_clock = pygame.time.Clock()

 # this is the game loop
 # ------- Main Program Loop
while not done:
 	# --- Main Event Loop
	for event in pygame.event.get():
	 	if event.type == pygame.QUIT:
	 		done = True 
 	  # while done:
 # 	 if user quits:
 # 	 	done = True 

 	 	# --- Game logic should go here

 	 	# --- Screen-clearing code goes here

	 # Here. we clear the screen to white. Dont put other drawing commands
	 # above this, or they will be earsed with this command.

	 # If you want a background image, replace this clear with blit'ing the
	 # background image.
	my_screen.fill(RED)

	pygame.draw.line(my_screen, BLUE, (100, 350), (300, 350))

	 # --- Drawing code should go here
	 # redraw based on the new state 

	 # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

 	# --- Limit to 60 frames per second
	my_fancy_clock.tick(60)




# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


# Loop until the user clicks the close button
