import pygame as pg
import time
from settings import *
from assets import *
from objects import *
from attack import *

screen = pg.display.set_mode((win_x,win_y))
player_starting_x, player_starting_y = 0, win_y - (lvl1_block_size + pikachu_dims[1] + 10)
all_enemy_objects = set()

class Player(pg.sprite.Sprite):

    lives = 2
    gravity = 1     # speed by which player falls/comes down
    SPRITES = Pikachu
    animation_delay = 3   # to change sprites

    def __init__(self,x,y,width,height):

        super().__init__()

        self.width = width
        self.height = height
        self.rect = pg.Rect(x,y,width,height)

        # setting player movement speeds
        self.x_vel = 0
        self.y_vel = 0

        self.mask = None

        # for sprites animation image
        self.direction = 'right'
        self.animation_count = 0

        # for fallings or gravity
        self.fall_count = 0      # number of frames we have been falling for
        self.jumpBool = False    # if the player is jumping or not

        self.attackBool = True    # if the player is ready to attack or not
        self.hit = False          # if the player is taking damage or not
        
        self.evolve = False
        self.start_time = time.time()

    def move(self,dx,dy):

        # moves player
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self,vel):

        # moves left

        if not (self.rect.x <= 0):
            self.x_vel = -vel
        if self.direction != 'left':          # updates direction to correctly show sprites animation
            self.direction = 'left'
            self.animation_count = 0

    def move_right(self,vel):

        # moves right
        if not (self.rect.x + self.width >= win_x):
            self.x_vel = vel
        if self.direction != 'right':          # updates direction to correctly show sprites animation
            self.direction = 'right'
            self.animation_count = 0

    def jump(self):
        # to jump the player

        self.jumpBool = True
        self.y_vel = -12     # decreasing from Y makes the player jump up
        self.animation_count = 0

    def loselife(self):
        # to make the player lose life in case they are hit

        if not self.hit:       # player must not be hit already        
            self.lives -= 1   
            self.hit = True    # set to true until the player stops colliding with any damage giver
    
    def landed(self):
        # to enable player land on blocks or platforms

        self.y_vel = 0

    def hit_head(self):
        # player hits head and falls down if the block is hit from below

        self.y_vel *= -1
    
    def powerup(self):
        # evolves pikachu into raichu for some seconds, providing invincibility

        if self.evolve:
            self.current_time = time.time()

            if self.current_time - self.start_time <= 5:
                print_text(f'{abs(5 - int(self.current_time - self.start_time))}',ingame_font,self.rect.x,self.rect.y-25,screen)
                self.SPRITES = raichu
            else:
                self.evolve = False 
                self.SPRITES = Pikachu
                

    def loop(self,fps):                        
        # what the player should be doing every loop iteration

        self.y_vel += min(1,(self.fall_count/fps) * Player.gravity)  # to bring the player down
        
        if self.rect.y > win_y:   # if player goes below the screen or falls in a pit
            if not(self.evolve):
                self.lives -= 1
            self.rect.x, self.rect.y = player_starting_x, player_starting_y

        if self.attackBool:
            self.move(self.x_vel,self.y_vel)

        self.fall_count += 1
        self.update_sprite()
        self.powerup()

        if not(self.attackBool):
            self.attack.shoot(screen)
            if self.attack.active == False:
                self.attackBool = True


    def update_sprite(self):
        # updates the player image according to the action being performed

        sprite_sheet = 'idle'
        if self.y_vel < 0 :
            if self.jumpBool:
                sprite_sheet = 'jump'
        elif self.y_vel > Player.gravity * 2 :
            sprite_sheet = 'fall'
        elif self.x_vel != 0:
            sprite_sheet = 'run'
        elif not self.attackBool:
            sprite_sheet = 'attack'

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (int(self.animation_count) // self.animation_delay) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 0.3
        self.update()

    def update(self):
        # updating rect according to the sprite

        self.rect = self.sprite.get_rect(topleft = (self.rect.x, self.rect.y))  
        self.mask = pg.mask.from_surface(self.sprite)  # masking our sprite image for collision

    def draw(self,screen):
        # draws player on the screen

        screen.blit(self.sprite,(self.rect.x,self.rect.y))

class Enemy(pg.sprite.Sprite):

    objects_list = []  # stores all Enemy instances to help detecting collision

    def __init__(self, x, y, dx, direction, rangeBool, speed, spritesheets):
        
        super().__init__()
        self.initial_x = x

        self.spritesheets = spritesheets
        self.sprite_index = 0

        self.image = spritesheets[f'run_{direction}'][0]
        self.rect = self.image.get_rect()
        
        self.rect.topleft = (x,y)

        self.dx = dx

        self.x_vel = speed   # enemy speed
        
        self.active = False   # only active when being drawn on the screen
        self.rem = True
        if rangeBool:
            self.ranged = True    # if the enemy is a ranged type
        else:
            self.ranged = False

        self.left = self.right = False     # initial direction of movement

        if direction.lower() == 'left':
            self.left = True
        elif direction.lower() == 'right':
            self.right = True

        self.current_direction = direction    # to help with the ranged projectile's direction
        Enemy.objects_list.append(self)
        self.tick = 0

    def activate(self):
        # activates the enemy

        if self.tick == 1:
            self.active = True

    def update_sprite(self):
        # changes sprite sheets to look like animation

        if self.tick % 15 == 0:
            try:
                self.image = self.spritesheets[f'run_{self.current_direction}'][self.sprite_index]
                self.sprite_index += 1
            except:
                self.sprite_index = 0
                self.image = self.spritesheets[f'run_{self.current_direction}'][self.sprite_index]


    def move(self):
        # moves enemy according to the parameters provided

        screen.blit(self.image,(self.rect.x,self.rect.y))
        if self.dx > 0:

            if self.left:
                if self.rect.x >= (self.initial_x - self.dx):
                    self.rect.x -= self.x_vel
                else:
                    self.left = False
                    self.right = True
            
            if self.right:
                if self.rect.x <= (self.initial_x + self.dx):
                    self.rect.x += self.x_vel
                else:
                    self.right = False
                    self.left = True

    def attack(self):
        # shoots if enemy is ranged type

        if (self.tick == 1 or self.atk.rem == False) and self.active: # shoot the first tick, then every 100 ticks
            self.atk = Attack(self.rect.x, self.rect.y,self.current_direction,bulb_attack,500,enemy_projectile_speed)   # an attack object is created every attack
        if self.active:
            self.atk.shoot(screen)
    
    def loop(self):
        # performs this every iteration

        self.tick += 1
        self.update_sprite()
        self.activate()
        if self.active:
            self.move()
        elif self.rem:
            self.rem = False
            if self.ranged:
                Attack.enemy_attacks.remove(self.atk)
            Enemy.objects_list.remove(self)
            all_enemy_objects.add(self)
        self.current_direction = 'left' if self.left else 'right' if self.right else None
        if self.ranged:
                self.attack()

# creating player and enemy objects
player = Player(player_starting_x, player_starting_y,pikachu_dims[0],pikachu_dims[1])

# level 1

lvl1_pidgeott = Enemy(375,win_y - (2.5*lvl1_block_size) + 20 - 64,300,'right',False, 7,pidgeott)
lvl1_bulbasaur = Enemy(1000,win_y - (3*lvl1_block_size) + 20 - pidgeott_dims[1],150,'right',True,3,bulbasaur)

# level 2

lvl2_golbat = Enemy(lvl1_block_size*5.75,win_y-(1.5*lvl1_block_size) - golbat_dims[1] + 25,300,'right',False,5,golbat)
lvl2_haunter = Enemy(lvl1_block_size*4.5,win_y-(2.5*lvl1_block_size)-haunter_dims[1],250,'left',False,9,haunter)


def handle_move(player,objects):
    # handles player movement and collision

    keys = pg.key.get_pressed()

    player.x_vel = 0
    if keys[pg.K_a]:
        player.move_left(player_speed)
    if keys[pg.K_d]:
        player.move_right(player_speed)

    handle_collision_player(player,objects,player.y_vel)  # checks collision with different objects

def handle_collision_player(player,objects,dy):

    collided_objects = []

    indices = player.rect.collidelistall(objects)    # index of all objects being collided with

    BoolList = []   # will store if we collide with a platform or not

    for index in indices:
        
        if isinstance(objects[index],Block):
            BoolList.append(True)      # list full of Trues if we only collide with Block
        else:
            BoolList.append(False)
    if not (False in BoolList): # if there are no Falses, i.e. if we do not collide with anything else
        player.hit = False


    for obj in objects:

        # if player is colliding with an active object
        if pg.sprite.collide_mask(player,obj) and obj.active:

            if isinstance(obj, Block):  # if the object is a block object or platform
                player.fall_count = 0
                if dy > 0 and player.rect.y <= obj.rect.y:              # if we are colliding from above
                    player.rect.bottom = obj.rect.top
                    player.landed()
                    player.jumpBool = False
                elif dy < 0 :           # if we ar colliding from below
                    player.rect.top = obj.rect.bottom
                    player.hit_head()

            elif isinstance(obj, Enemy) and not(player.evolve):  # if it is an enemy
                player.loselife()

            elif isinstance(obj, Attack) and obj.player == False and not(player.evolve):  # if it is an enemy attack object
                player.loselife()
            
            elif isinstance(obj, Trap) and not(player.evolve):      # if it is a trap object
                player.loselife()
            
            elif isinstance(obj,Evolve):
                obj.active = False
                obj.display = False
                player.evolve = True
                player.start_time = time.time()

        collided_objects.append(obj)

    return collided_objects

def handle_collision_enemy(enemy_list,objects_list):

    for enemy in enemy_list:
        for obj in objects_list:

            if pg.sprite.collide_mask(enemy,obj):
                if enemy.active:
                    enemy.active = False