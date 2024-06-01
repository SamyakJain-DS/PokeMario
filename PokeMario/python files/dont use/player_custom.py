import pygame as pg
from assets import *
from settings import *
from platform_class import *

pika_dims = 64

class Player():

    def __init__(self,x,y,img):

        self.img = pg.transform.scale(img,(pika_dims,pika_dims))
        
        self.height = self.img.get_height()
        self.width = self.img.get_width()

        self.rect = self.img.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.x_change = 0       # change in player's x coordinate by a keypress
        self.movement_speed = 5    # player movement speed

        self.y_velocity = 50     # speed with which the player jumps
        self.jump_height = 50    # max jump height
        self.y_gravity = 5       # speed with which the player falls

        # if buttons are pressed or not

        self.right_pressed = False
        self.left_pressed = False
        self.jump = False


    def draw(self,surface):
        surface.blit(self.img,(self.rect.x,self.rect.y))
    
    def move(self):

        if self.right_pressed and not self.left_pressed:
            if self.rect.x >= (win_x-self.width):      # limits player's movements to within the screen
                pass
            else:
                self.rect.x += self.movement_speed

        if self.left_pressed and not self.right_pressed:
            if self.rect.x <= 0:                       # limits player's movements to within the screen
                pass
            else: 
                self.rect.x -= self.movement_speed

        if self.jump:
            
            print(self.y_gravity,self.y_velocity)
            # y coordinate decreases (or the player jumps) with the given velocity
            self.rect.y -= self.y_velocity
            # speed with which player jumps decreases and gradually becomes negative
            self.y_velocity -= self.y_gravity

            if self.y_velocity < 0:

                #checking collision with platform objects, only while the player is falling
                for platform in plt_objs:     

                    # platform.getDimensions()[1] is the platform's Y coordinate
                    if platform.active and self.rect.colliderect(platform.getDimensions()) and self.rect.y <= platform.getDimensions()[1] - pika_dims: 
                        #self.jump = False
                        # sets new player Y coordinate
                        if self.rect.y == platform.getDimensions()[1] - self.height:
                            self.y_velocity = self.jump_height   # resets velocity for the next jump

            # if player has returned to the original location after the jump
                        
            if self.y_velocity < -self.jump_height:
                self.jump = False
                self.y_velocity = self.jump_height   # resets velocity for the next jump
    
    def onPlatform(self):

        for obj in plt_objs:
            if obj.active == True and self.rect.colliderect(obj.getDimensions()): #and self.rect.y <= obj.getDimensions()[1] - pika_dims:
                print(self.rect.y,obj.getDimensions()[1],self.height)
                self.rect.y = obj.getDimensions()[1] - self.height
            else:
                self.rect.y += 1
                if self.rect.y > win_y:
                    self.rect.topleft = (0,700)

# creating players

player = Player(0,700,pikachu)