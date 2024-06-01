import pygame as pg
from settings import *
from assets import *

class Object(pg.sprite.Sprite):

    def __init__(self, x, y, width, height):
        
        super().__init__()

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.active = False
  
    def draw(self, screen):
        # draws the objects on the screen

        self.active = True

        screen.blit(self.image, (self.rect.x,self.rect.y))
        
class Block(Object): # inheriting Obejct class

    objects_list = []

    def __init__(self, x, y, width, height, path):

        super().__init__(x, y, width, height)

        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

        self.mask = pg.mask.from_surface(self.image)

        Block.objects_list.append(self)

class Trap(Object): # inheriting Obejct class

    objects_list = []

    def __init__(self, x, y, width, height, sprite):

        super().__init__(x, y, width, height)

        Trap.objects_list.append(self)
        self.velocity = -1

        self.tick = 0

        self.spritesheet = sprite
        self.sprite_index = 0

        self.image = self.spritesheet[self.sprite_index]

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
        self.mask = pg.mask.from_surface(self.image)

        self.initial_y = self.rect.y

        self.up = True
        self.down = False

    def update_sprite(self):

        if self.tick % 18 == 0:
            try:
                self.sprite_index += 1
                self.image = self.spritesheet[self.sprite_index]
            except IndexError:
                self.sprite_index = 0
                self.image = self.spritesheet[self.sprite_index]
    
    def move(self):

        if self.up:
            if self.rect.y >= self.initial_y - self.height + 10:
                self.rect.y += self.velocity
            else:
                self.up = False
                self.down = True

        if self.down:
            if self.rect.y <= self.initial_y:
                self.rect.y -= self.velocity
            else:
                self.up = True
                self.down = False
    
    def draw(self, screen):
    # draws the objects on the screen

        self.active = True

        self.tick += 1
        self.update_sprite()
        
        screen.blit(self.image, (self.rect.x,self.rect.y))

class Evolve(Object):

    objects_list = []

    def __init__(self, x, y, width, height, path):

        super().__init__(x, y, width, height)

        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

        self.mask = pg.mask.from_surface(self.image)

        Evolve.objects_list.append(self)

        self.display = True
    
    def draw(self,screen):

        if self.display:
            self.active = True
            screen.blit(self.image,(self.rect.x,self.rect.y))

# creating objects
            
# level 1
            
lvl1_block_size = 200
lvl1_floor = [Block(i,win_y - lvl1_block_size,lvl1_block_size,lvl1_block_size,join('assets', 'tileset','GRASSLAND', 'TILE1.png')) for i in range(0,200,lvl1_block_size)]     # list of block objects in line, which look like a floor
lvl1_floor_end = Block(lvl1_block_size, win_y - lvl1_block_size+1,lvl1_block_size/2,lvl1_block_size,join('assets', 'tileset','GRASSLAND', 'TILE2.png'))
lvl1_floating = Block(450,win_y - (2*lvl1_block_size) + 20,lvl1_block_size*1.5,lvl1_block_size,join('assets', 'tileset','GRASSLAND', 'FLOATING TILE.png'))
lvl1_bigtile = Block(850,win_y - (3*lvl1_block_size) + 20,lvl1_block_size*2,lvl1_block_size*4,join('assets', 'tileset','GRASSLAND', 'ONE BIG TILE 2.png'))
lvl1_endtile = Block(win_x-lvl1_block_size,win_y - lvl1_block_size,lvl1_block_size*1.3,lvl1_block_size,join('assets', 'tileset','GRASSLAND', 'TILE1.png'))


lvl1_dugtrio = Trap(win_x-lvl1_block_size,win_y - lvl1_block_size,dugtrio_dims[0],dugtrio_dims[1],dugtrio_trap)

lvl1_thunderstone = Evolve(100,600,32,32,join('assets','player_assets','thunderstone.png'))

# level 2
starting_block_1 = Block(0,win_y-lvl1_block_size,lvl1_block_size,75,join('assets','DARK AREA BLOCKS','Block 1.png'))
starting_block_2 = Block(lvl1_block_size,win_y-lvl1_block_size,lvl1_block_size,75,join('assets','DARK AREA BLOCKS','middle block.png'))
starting_block_3 = Block(lvl1_block_size*2,win_y-lvl1_block_size,lvl1_block_size,75,join('assets','DARK AREA BLOCKS','BLOCK 1 REVERSED.png'))
bridge = Block(lvl1_block_size*3,win_y-lvl1_block_size,lvl1_block_size,50,join('assets','DARK AREA BLOCKS','bRIDGE.png'))
starting_block_4 = Block(lvl1_block_size*4,win_y-lvl1_block_size,lvl1_block_size,75,join('assets','DARK AREA BLOCKS','middle block.png'))
floating_1 = Block(win_x-96,win_y-(0.65*lvl1_block_size),96,96,join('assets','DARK AREA BLOCKS','SMALL BLOCK 2.png'))
floating_2 = Block(win_x-lvl1_block_size,win_y-(3*lvl1_block_size),lvl1_block_size,75,join('assets','DARK AREA BLOCKS','middle block.png'))
floating_3 = Block(lvl1_block_size*5.75,win_y-(1.5*lvl1_block_size),lvl1_block_size,75,join('assets','DARK AREA BLOCKS','middle block.png'))
floating_4 = Block(lvl1_block_size*4.5,win_y-(2.5*lvl1_block_size),lvl1_block_size,75,join('assets','DARK AREA BLOCKS','middle block.png'))
floating_5 = Block(win_x-lvl1_block_size-95,win_y-(3*lvl1_block_size),100,75,join('assets','DARK AREA BLOCKS','SMALL BLOCK 2.png'))

lvl2_charmander = Trap(lvl1_block_size*3 - charmander_dims[0],win_y - lvl1_block_size - charmander_dims[1],charmander_dims[0],charmander_dims[1],charmander_trap)

lvl2_thunderstone = Evolve(win_x-96 + 50,win_y-(0.65*lvl1_block_size) - 50,32,32,join('assets','player_assets','thunderstone.png'))

def draw_floor_list(list_obj, screen):
    # draws each individual block in the floor list on the screen

    for obj in list_obj:
        obj.draw(screen)