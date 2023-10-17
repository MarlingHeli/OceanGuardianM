#Manling's version
import pygame
from sys import exit

pygame.init() #starts up pygame components

#create display window
screen = pygame.display.set_mode((1100, 750))
pygame.display.set_caption("Ocean Guardian") #set name of display window
#Set constant frame rate
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("Hello", False, "White")

#keep display window on screen forever
while True:
    #close display window if user quits
    for event in pygame.event.get(): #check for events constantly
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() #exit while loop
            
    screen.blit(text_surface,(500,300))
    
    pygame.display.update() #update elements to show on display window
    clock.tick(60) #limit while true loop to 60fps 

