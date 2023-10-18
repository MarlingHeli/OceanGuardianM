#Manling's version
import pygame
from sys import exit

pygame.init() #starts up pygame components

#create display window
screen = pygame.display.set_mode((1100, 750))
pygame.display.set_caption("Ocean Guardian M") #set name of display window
#Set constant frame rate
clock = pygame.time.Clock()
text = pygame.font.Font(None, 50) #pick font for text.

#starting co-ords
x = 200
y = 200

#width of player
width = 20
height = 20

#velocity of player
velocity = 10

#keep display window on screen forever
while True:
    pygame.time.delay(10) #delay (optional)
    #close display window if user quits
    for event in pygame.event.get(): #check for events constantly
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() #exit while loop
    
    #stores keys pressed
    keys = pygame.key.get_pressed()
    #if A or left arrow key is pressed
    if keys[pygame.K_LEFT] and x > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += velocity
    if keys[pygame.K_UP] and y > 0:
        y -= velocity
    if keys[pygame.K_DOWN] and y < 500 - height:
        y += velocity
        
    pygame.draw.rect(screen,(0,0,225), (x, y, width, height))
    
    pygame.display.update() #update elements to show on display window
    clock.tick(60) #limit while true loop to 60fps 

