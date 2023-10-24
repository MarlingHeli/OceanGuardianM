#Manling's version
import pygame
from sys import exit

pygame.init() #starts up pygame components

#create display window
screen_width = 1100
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ocean Guardian M") #set name of display window
#Set constant frame rate
clock = pygame.time.Clock()
text = pygame.font.Font(None, 50) #pick font for text.

#player class contains the variables and code for the player
class Player:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x, y, 40, 40) #make player a square 40 x 40px
        self.x = int(x)
        self.y = int(y)
        self.color = (250, 120, 60)
        self.velX = 0 #horizontal velocity
        self.velY = 0 #vertical velocity
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
        
        self.rect = pygame.Rect(self.x, self.y, 32, 32) #put player on screen in new position
        
#Initialise player
player = Player(screen_width/2, screen_height/2)
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
    #Draw
    screen.fill((12, 24, 36))
    player.draw(screen) 
    
    #update
    player.update()
    pygame.display.flip()
                
    
    pygame.display.update() #update elements to show on display window
    clock.tick(60) #limit while true loop to 60fps 

