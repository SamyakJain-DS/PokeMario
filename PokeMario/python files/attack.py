import pygame as pg
from settings import *

class Attack(pg.sprite.Sprite):

    enemy_attacks = []  # list of all Enemy Attack class objects
    player_attack = []  # list of all Player Attack class objects

    def __init__(self, x, y, direction, image, range, speed, player = False):

        super().__init__()

        self.x = self.initial_x = x
        self.y = y
        self.direction = direction
        self.velocity = speed  # speed of the projectile

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

        self.range = range  # number of blocks the projectile travels
        self.player = player  # if the projectile is of our player or the enemy

        self.active = False
        self.rem = True
        if self.player == False:
            Attack.enemy_attacks.append(self)
        else:
            Attack.player_attack.append(self)
    
    def shoot(self,screen):
        # blits the object on the screen and deals damage

        if self.direction == 'left':

            if self.rect.x >= (self.initial_x - self.range):
                self.rem = True
                self.active = True
                screen.blit(self.image,(self.rect.x,self.rect.y))
                self.rect.x -= self.velocity

            else:
                self.active = False
                if self.rem:
                    if not(self.player):
                        Attack.enemy_attacks.remove(self)
                    else:
                        Attack.player_attack.remove(self)
                    self.rem = False

        elif self.direction == 'right':

            if self.rect.x <= self.initial_x + self.range:
                self.rem = True
                self.active = True
                screen.blit(self.image,(self.rect.x,self.rect.y))
                self.rect.x += self.velocity
            else:
                self.active = False
                if self.rem:
                    if not(self.player):
                        Attack.enemy_attacks.remove(self)
                    else:
                        Attack.player_attack.remove(self)
                    self.rem = False