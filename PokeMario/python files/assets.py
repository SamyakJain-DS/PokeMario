import pygame as pg
from pygame import mixer
from settings import *
from os import listdir
from os.path import join,isfile


mixer.init()
pg.init()

win_logo = pg.image.load(join('assets','window_assets','pika.png'))  #Loading window logo
main_menu_bg = pg.transform.scale(pg.image.load(join('assets','main_menu_assets','mario-game.jpg')),(1600,900)) #main menu background
lost_screen_bg = pg.image.load(join('assets','lostscreen_assets','lost2.png'))
win_screen_bg = pg.image.load(join('assets','winscreen_assets','won3.png'))
# button images

on = pg.transform.scale(pg.image.load(join('assets', 'main_menu_assets', 's_on.png')),(250,250))
off = pg.transform.scale(pg.image.load(join('assets', 'main_menu_assets', 's_off.png')),(250,250))

play_img = pg.transform.scale(pg.image.load(join('assets', 'main_menu_assets', 'play_btn.png')),(200,108))
instructions_img = pg.transform.scale(pg.image.load(join('assets', 'main_menu_assets', 'ins_btn.png')),(500,100))
credits_img = pg.transform.scale(pg.image.load(join('assets', 'main_menu_assets', 'credits_btn.png')),(300,108))
ques_btn = pg.transform.scale(pg.image.load(join('assets','main_menu_assets','ques_button1.png')),(64,64))

play_again_img = pg.transform.scale(pg.image.load(join('assets', 'main_menu_assets', 'play_again_btn.png')),(375,75))
return_img = pg.transform.scale(pg.image.load(join('assets', 'main_menu_assets', 'return_btn.png')),(337.5,75))
quit_img = pg.transform.scale(pg.image.load(join('assets', 'main_menu_assets', 'quit_btn.png')),(150,75))

back_img = pg.transform.scale(pg.image.load(join('assets', 'instructions_assets', 'back.png')),(128,64))

# title logo
title_img = pg.image.load(join('assets', 'main_menu_assets', 'pokemario.png'))

instructions_title = pg.image.load(join('assets', 'instructions_assets', 'INSTRUCTIONS-button.png'))

credits_title = pg.image.load(join('assets', 'credits_assets', 'credits.png'))
credits_title = pg.transform.scale(credits_title,(850,100)) # rescaling

won_img = pg.image.load(join('assets', 'winscreen_assets', 'won.png'))
won_img = pg.transform.scale(won_img,(600,400))

lost_img = pg.image.load(join('assets', 'lostscreen_assets', 'lose1.png'))
lost_img = pg.transform.scale(lost_img,(600,400))


# levels

lvl_1 = pg.image.load(join('assets', 'BACKGROUNDS', 'evening.jpg'))
lvl_2 = pg.image.load(join('assets', 'BACKGROUNDS','night.png'))

# objects

platform = pg.image.load(join('assets', 'tileset','GRASSLAND', 'ONE BIG TILE.png'))

# door

door_open = pg.transform.scale(pg.image.load(join('assets', 'door_assets', 'Door open.png')),door_dims)
door_closed = pg.transform.scale(pg.image.load(join('assets', 'door_assets', 'Door closed.png')),door_dims)

# music

mixer.music.load(join('assets','bg_music','bg.mp3'))
mixer.music.set_volume(0.5)

# txt files

file1 = open("Docs/INSTRUCTIONS.txt",'r')
file2 = open("Docs/CREDITS.txt",'r')

instructions_txt = file1.read()
credits_txt = file2.read()

file1.close()
file2.close()

# fonts

credits_font = pg.font.Font(join('assets','retro_computer_personal_use.ttf'), 27)
ins_font = pg.font.Font(join('assets','retro_computer_personal_use.ttf'), 19)
ingame_font = pg.font.Font(join('assets','retro_computer_personal_use.ttf'), 35)
lastscreen_font = pg.font.Font(join('assets','retro_computer_personal_use.ttf'), 40)

# player

pikachu_face = pg.transform.scale(pg.image.load(join('assets','pikachu face.png')),(64,64))

Pikachu = {'idle_left':[pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','idle pikachu','1.png')),pikachu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','idle pikachu','2.png')),pikachu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','idle pikachu','3.png')),pikachu_dims),True,False)],'idle_right':[pg.transform.scale(pg.image.load(join('assets','Pikachu','idle pikachu','1.png')),pikachu_dims),pg.transform.scale(pg.image.load(join('assets','Pikachu','idle pikachu','2.png')),pikachu_dims),pg.transform.scale(pg.image.load(join('assets','Pikachu','idle pikachu','3.png')),pikachu_dims)],'run_left' : [pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','running sprite','1.png')),pikachu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','running sprite','2.png')),pikachu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','running sprite','3.png')),pikachu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','running sprite','4.png')),pikachu_dims),True,False)],'run_right' : [pg.transform.scale(pg.image.load(join('assets','Pikachu','running sprite','1.png')),pikachu_dims),pg.transform.scale(pg.image.load(join('assets','Pikachu','running sprite','2.png')),pikachu_dims),pg.transform.scale(pg.image.load(join('assets','Pikachu','running sprite','3.png')),pikachu_dims),pg.transform.scale(pg.image.load(join('assets','Pikachu','running sprite','4.png')),pikachu_dims)],'jump_left':[pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','Jump','Jump.png')),pikachu_dims),True,False)],'jump_right':[pg.transform.scale(pg.image.load(join('assets','Pikachu','Jump','Jump.png')),pikachu_dims)],'fall_left':[pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','Jump','Jump.png')),pikachu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','Jump','Jump.png')),pikachu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','Jump','Jump.png')),pikachu_dims),True,False)],'fall_right':[pg.transform.scale(pg.image.load(join('assets','Pikachu','Jump','Jump.png')),pikachu_dims),pg.transform.scale(pg.image.load(join('assets','Pikachu','Jump','Jump.png')),pikachu_dims),pg.transform.scale(pg.image.load(join('assets','Pikachu','Jump','Jump.png')),pikachu_dims)],'attack_left' : [pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','Attack','1.png')),pikachu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','Attack','2.png')),pikachu_dims),True,False)], 'attack_right' : [pg.transform.scale(pg.image.load(join('assets','Pikachu','Attack','1.png')),pikachu_dims),pg.transform.scale(pg.image.load(join('assets','Pikachu','Attack','2.png')),pikachu_dims)]}

pikachu_bolt_right = pg.transform.scale(pg.image.load(join('assets','Pikachu','Attack','lightning bolt.png')),pikabolt_dims)
pikachu_bolt_left = pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','Attack','lightning bolt.png')),pikabolt_dims),True,False)

raichu = {'run_left' : [pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','1.png')),raichu_dims),pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','2.png')),raichu_dims),pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','3.png')),raichu_dims),pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','4.png')),raichu_dims),pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','5.png')),raichu_dims)], 'run_right' : [pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','1.png')),raichu_dims),True,False),pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','2.png')),raichu_dims),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','3.png')),raichu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','4.png')),raichu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','5.png')),raichu_dims),True,False)], 'fall_right' : [pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','1.png')),raichu_dims),True,False)], 'fall_left' : [pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','1.png')),raichu_dims)],'jump_right' : [pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','1.png')),raichu_dims),True,False)], 'jump_left' : [pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','1.png')),raichu_dims)],'idle_right' : [pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','1.png')),raichu_dims),True,False)], 'idle_left' : [pg.transform.scale(pg.image.load(join('assets','Raichu','Raichu running','1.png')),raichu_dims)],'attack_left' : [pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','Attack','1.png')),pikachu_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pikachu','Attack','2.png')),pikachu_dims),True,False)], 'attack_right' : [pg.transform.scale(pg.image.load(join('assets','Pikachu','Attack','1.png')),pikachu_dims),pg.transform.scale(pg.image.load(join('assets','Pikachu','Attack','2.png')),pikachu_dims)]}

# enemy

pidgeott = {'run_left' : [pg.transform.scale(pg.image.load(join('assets','Pidgeott','1.png')),pidgeott_dims),pg.transform.scale(pg.image.load(join('assets','Pidgeott','2.png')),pidgeott_dims),pg.transform.scale(pg.image.load(join('assets','Pidgeott','3.png')),pidgeott_dims)],'run_right' : [pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pidgeott','1.png')),pidgeott_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pidgeott','2.png')),pidgeott_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Pidgeott','3.png')),pidgeott_dims),True,False)]}

golbat = {'run_left' : [pg.transform.scale(pg.image.load(join('assets','golbat','1.png')),golbat_dims),pg.transform.scale(pg.image.load(join('assets','golbat','2.png')),golbat_dims),pg.transform.scale(pg.image.load(join('assets','golbat','3.png')),golbat_dims),pg.transform.scale(pg.image.load(join('assets','golbat','4.png')),golbat_dims)],'run_right' : [pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','golbat','1.png')),golbat_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','golbat','2.png')),golbat_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','golbat','3.png')),golbat_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','golbat','4.png')),golbat_dims),True,False)]}

haunter = {'run_left' : [pg.transform.scale(pg.image.load(join('assets','Haunterr','front.png')),haunter_dims)],'run_right' : [pg.transform.scale(pg.image.load(join('assets','Haunterr','back.png')),haunter_dims)]}

bulbasaur = {'run_right' : [pg.transform.scale(pg.image.load(join('assets','Bulbasaur','3.png')),pidgeott_dims),pg.transform.scale(pg.image.load(join('assets','Bulbasaur','4.png')),pidgeott_dims),pg.transform.scale(pg.image.load(join('assets','Bulbasaur','5.png')),pidgeott_dims)],'run_left' : [pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Bulbasaur','3.png')),pidgeott_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Bulbasaur','4.png')),pidgeott_dims),True,False),pg.transform.flip(pg.transform.scale(pg.image.load(join('assets','Bulbasaur','5.png')),pidgeott_dims),True,False)]}

bulb_attack = pg.image.load(join('assets','Bulbasaur','Projectile','projectile 1.png'))

enemy_attack = pg.image.load(join('assets', 'player_assets', 'bullet.png'))

# traps

charmander_trap = [pg.transform.scale(pg.image.load(join('assets','Charmander','1.png')),charmander_dims),pg.transform.scale(pg.image.load(join('assets','Charmander','2.png')),charmander_dims),pg.transform.scale(pg.image.load(join('assets','Charmander','3.png')),charmander_dims),pg.transform.scale(pg.image.load(join('assets','Charmander','4.png')),charmander_dims)]

dugtrio_trap = [pg.transform.scale(pg.image.load(join('assets','traps_assets','Dugtrio_(Sprite_1).png')),dugtrio_dims)]

# text functioning

def print_text_decor(func):
    def inner(text,font,x,y,screen,text_color = (255,255,255)):
        if isinstance(text,list):       # to handle list inputs differently
            i = 0
            for line in text:
                img = font.render(line,True,text_color)
                screen.blit(img,(x,y+i))
                i += 50                     # line spacing
        else:
            func(text,font,x,y,screen,text_color = (255,255,255))    # if not list then just blit normally
    return inner

@print_text_decor
def print_text(text,font,x,y,screen,text_color = (255,255,255)):
    img = font.render(text, True, text_color)
    screen.blit(img,(x,y))