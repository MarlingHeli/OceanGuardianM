#Manling's version
import pygame
from sys import exit
import random

pygame.init() #starts up pygame components

#create display window
screen_width = 1100
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ocean Guardian M's version") #set name of display window
#Set constant frame rate
clock = pygame.time.Clock()
text = pygame.font.Font(None, 50) #pick font for text.

#player class contains the variables and code for the player
class Player:
    global player_width, player_height
    player_width = 50 
    player_height = 50

    def __init__(self,x,y):
        self.rect = pygame.Rect(x, y, player_width, player_height) #make player a rectangle
        self.x = int(x)
        self.y = int(y)
        self.color = (250, 120, 60)
        self.velX = 0 
        self.velY = 0 
        self.left_pressed = False #Set movement keys to false upon initialisation
        self.right_pressed = False 
        self.up_pressed = False 
        self.down_pressed = False 
        self.speed = 5 #player speed
        
    def draw(self, screen): #display player on screen
        pygame.draw.rect(screen, self.color, self.rect)
        
    def update(self): #refresh player to update to new positions (account for movement)
        self.velX = 0
        self.velY = 0   
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed 
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed 
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
            
        self.x += self.velX #update to new position
        self.y += self.velY
        
        self.rect = pygame.Rect(self.x, self.y, player_width, player_height) #put player on screen in new position
        
#Initialise player
player = Player(screen_width/2, screen_height/2)

class Rubbish:
    global rubbish_width, rubbish_height, rubbish_colour
    rubbish_width = 35
    rubbish_height = 35
    rubbish_colour = (255, 0, 0)
    
    def __init__(self):
        self.x = screen_width #start from right side of the screen
        self.y = random.randrange(0, screen_height - rubbish_height) #spawn randomly on y axis. min value of 0, max of screen_height-rubbish_height
        self.color = rubbish_colour
        self.speed = random.uniform(3.5, 5) #speed of rubbish will range from 3 to 4.5
        
    def move(self):
        self.x -= self.speed
        
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, rubbish_width, rubbish_height))
        
rubbish_list = []


#keep display window on screen forever
while True:
    #pygame.time.delay(10) #delay (optional)
    #close display window if user quits
    for event in pygame.event.get(): #check for events constantly
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() #exit while loop
            
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
                
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
                
        if len(rubbish_list) < 3:
            rubbish_list.append(Rubbish())


    #Draw
    screen.fill((12, 24, 36)) #colour of display screen
    player.draw(screen) 
    
    for rubbish in rubbish_list:
        rubbish.move()
        rubbish.draw()
        
        rubbish_list = [rubbish for rubbish in rubbish_list if rubbish.x > -rubbish_width]
    
    #update
    player.update()
    pygame.display.flip()
    
                
    
    pygame.display.update() #update elements to show on display window
    clock.tick(60) #limit while true loop to 60fps 

