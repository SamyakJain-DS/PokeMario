import pygame as pg
from assets import *
from settings import *

class Platform(pg.sprite.Sprite):

    plt_list = []

    def __init__(self,x,y,img,w,h,speed = 0,direction = ''):
        self.width = w
        self.height = h

        self.img = pg.transform.scale(img,(self.width,self.height))  # rescaling the platform
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.active = False  # active variable tells us if the platform is printed or not

        self.speed = speed     # platform movement speed
        self.initial_x = self.rect.x   
        self.initial_y = self.rect.y   # marking the initial coordinates to facilitate movement
        self.direction = direction    # directiop of the movement

        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

        if  self.direction.lower() == "right":
            self.move_right = True
        elif self.direction.lower() == "left":
            self.move_left = True
        elif self.direction.lower() == "up":
            self.move_up = True
        elif self.direction.lower() == "down":
            self.move_down = True
        
        Platform.plt_list.append(self)  # to append each object into a list

    def draw(self,screen):    # print the platform on the screen
        screen.blit(self.img,(self.rect.x,self.rect.y))
        self.active = True
    
    def move(self,x_pixels,y_pixels):  # platform movement function

        if self.move_left:    # to move the platform left
            self.rect.x -= self.speed
            if self.rect.x <= (self.initial_x - x_pixels) or self.rect.x <= 0:
                self.move_left = False
                self.move_right = True

        if self.move_right:    # to move the platform right
            self.rect.x += self.speed
            if self.rect.x >= (self.initial_x + x_pixels) or (self.rect.x + self.width) >= win_x:
                self.move_right = False
                self.move_left = True

        if self.move_up:       # to move the platform up
            self.rect.y -= self.speed
            if self.rect.y <= (self.initial_y - y_pixels) or self.rect.y <= 0:
                self.move_up = False
                self.move_down = True

        if self.move_down:      # to move the platform down
            self.rect.y += self.speed
            if self.rect.y >= (self.initial_y + y_pixels) or (self.rect.y + self.height) >= win_y:
                self.move_down = False
                self.move_up = True

    def getDimensions(self):          # to get dimensions of each object 
        return (self.rect.x , self.rect.y , self.width , self.height)

# creating platforms

horz_plat_1 = Platform(150,100,platform,100,100,5,'LEFT')
vert_plat_1 = Platform(100,150,platform,100,100,5,'up')
horz_plat_2 = Platform(1050,100,platform,100,100,5,'right')
vert_plat_2 = Platform(100,650,platform,100,100,5,'down')
stat_plat_1 = Platform(200,550,platform,400,100)
stat_plat_2 = Platform(0,764,platform,1000,100)


# creating a list of collidable platforms

collidable_plt_list = []
plt_objs = []

for obj in Platform.plt_list:
    plt_objs.append(obj)     # this list contains all the objects of the class Platform

# this list contains dimensions of each object of Platform class
for dims in plt_objs:
    collidable_plt_list.append(dims.getDimensions()) 

# function to reset the active state of each platform whenever the screen changes
def reset_active():
    
    for obj in plt_objs:
        obj.active = False