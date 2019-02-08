import pygame,sys,os
from pygame.locals import *         # Imports a bunch of stuffs
import time

pygame.init()

fps = pygame.time.Clock()

# Bunch of variables

wide =  800
height = 500

red = (255,0,0)
grey = (20,20,20)

bx = 100
by = 250

bw = 100
bh = 50

show = pygame.display.set_mode((wide,height))
pygame.display.set_caption("Incredibly complex visual novel made by Yours Truly")

# Loads image from directory file then resizes image to fit screen
img = pygame.image.load(os.path.join('E:', '596610.jpg'))

img = pygame.transform.scale(img, (wide,height))


# Imports font
font = pygame.font.SysFont(None, 50)

# Function to display a message
def message (msg,colour):
    text = font.render(msg, True, colour)
    show.blit(text, [100, height/2])

# Function to display image
def image (x,y):
    show.blit(img,(x,y))
    

# Main loop
while True:
    mousex, mousey = pygame.mouse.get_pos()     # gets mouse position
   
    image(0,0) # the image
    pygame.draw.rect(show,grey,(bx,by,bw,bh), 0) # a box
    
    message("Hello",  red) # The message
    
    for event in pygame.event.get():   # event handler
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
           
        if mousex > bx and mousex < bx + bw: # if you click on the button 
                                # something magical will happen
            if event.type == MOUSEBUTTONUP:
             bx = 400
            
     

    

    pygame.display.update()     
    fps.tick(60)        #Sets FPS


