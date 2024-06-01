import pygame as pg
from assets import *
from settings import *


class Button: 
    def __init__(self,x,y,image,scale = 1):

        self.width = image.get_width()
        self.height = image.get_height()
        # rescaling the button to the desired size
        self.image = pg.transform.scale(image, (int(self.width * scale),int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.clicked = False   # is the button clicked?

    def draw(self,surface):
        
        action = False      # is there a need to do the action?
        pos = pg.mouse.get_pos()   # getting mouse position

        if self.rect.collidepoint(pos):     # collides with mouse pointer
            # left mouse button pressed while the button wasn't already pressed
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked == True     # the button is pressed
                action = True        # perform the action

        if pg.mouse.get_pressed()[0] == 0:   # if the left mouse button gets unpressed
                self.clicked == False   # button no longer pressed
        
        surface.blit(self.image,(self.rect.x,self.rect.y))
        
        return action    # performs action if button clicked else does nothing

# creating buttons

sfx_on = Button(1530,10,on,0.25)
sfx_off = Button(1530,10,off,0.25)

play_btn = Button(600,474,play_img,0.8)
instructions_btn = Button(600,600,instructions_img,0.8)
credits_btn = Button(600,724,credits_img,0.8)

back_btn = Button(15,10,back_img)

play_again_btn = Button(144,97,play_again_img)
main_menu_btn = Button(144,392,return_img)
quit_btn = Button(144,685,quit_img)