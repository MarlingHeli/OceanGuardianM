#Manling's version
import pygame
from sys import exit

pygame.init() #starts up pygame components

#create display window
screen = pygame.display.set_mode((1100, 750))
pygame.display.set_caption("Ocean Guardian") #set name of display window

#keep display window on screen forever
while True:
    #close display window if user quits
    for event in pygame.event.get(): #check for events constantly
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() #exit while loop
    #draw all our elements
    #update everything
    pygame.display.update() #update elements to show on display window

