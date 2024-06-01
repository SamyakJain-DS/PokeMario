import pygame as pg
from assets import *
from button import *
from platform_class import *
from player_custom import *
from settings import *

pg.init()
clock = pg.time.Clock()         # to set frame rate

# creating window

screen = pg.display.set_mode((win_x,win_y))
srface = pg.Surface((win_x,win_y),pg.SRCALPHA)

pg.display.set_caption(title)
pg.display.set_icon(win_logo)

# animating background for the game

bg_width = main_menu_bg.get_width()

# text functioning

def print_text_decor(func):
    def inner(text,font,x,y,text_color = (255,255,255)):
        if isinstance(text,list):
            i = 0
            for line in text:
                img = font.render(line,True,text_color)
                screen.blit(img,(x,y+i))
                i += 50
        else:
            func(text,font,x,y,text_color = (255,255,255))
    return inner

@print_text_decor
def print_text(text,font,x,y,text_color = (255,255,255)):
    img = font.render(text, True, text_color)
    screen.blit(img,(x,y))

# sound button functioning

def sfx_state():
    if sound_state:         # SFX toggle (visual only rn)
        sfx_on.draw(screen)
    else:
        sfx_off.draw(screen)

# screens

def moving_background(img):      # to create a moving background

    global scroll, win_x
    scroll -= 5           # sets the amount by which the bg scrolls

    screen.blit(img,(-win_x + scroll,0))
    screen.blit(img,(0 + scroll,0))  # prints the bg at a slighlty different position each loop
    screen.blit(img,(win_x + scroll,0))

    if scroll == -win_x : # reset the images and scroll again
        scroll = win_x

def transparent_bg(rgba):

    # this is creating the background-foreground differentiation

    global srface,win_x,win_y

    screen.blit(srface,(0,0))
    pg.draw.rect(srface,rgba,(0,0,win_x,win_y))

def main_menu():

    reset_active()

    global state

    # background

    moving_background(main_menu_bg)
    transparent_bg((0,0,0,100))
    screen.blit(title_img,(228,50))

    #buttons

    if play_btn.draw(screen):
        state = state_list[1]  # changing state to change screens
    if instructions_btn.draw(screen):
        state = state_list[2]
    if credits_btn.draw(screen):
        state = state_list[3]
        
    sfx_state()

def start():

    reset_active()

    screen.blit(lvl_bg,(0,0))

    # drawing different platforms
    stat_plat_1.draw(screen)
    stat_plat_2.draw(screen)

    #horz_plat_1.draw(screen)
    #horz_plat_1.move(200,0)

    #vert_plat_1.draw(screen)
    #vert_plat_1.move(0,200)

    #horz_plat_2.draw(screen)
    #horz_plat_2.move(200,0)

    #vert_plat_2.draw(screen)
    #vert_plat_2.move(0,200)

    # drawing player
    player.draw(screen)

def instructions():

    reset_active()
    global state

    #background

    moving_background(main_menu_bg)
    transparent_bg((0,0,0,85))
    screen.blit(instructions_title,(300,50))
    print_text(instructions_txt,main_menu_font,350,400)
    sfx_state()
    
    if back_btn.draw(screen):
        state = state_list[0] # sending back to main menu if back button is pressed
    
def credits():

    reset_active()
    global state

    #background

    moving_background(main_menu_bg)
    transparent_bg((0,0,0,85))
    screen.blit(credits_title,(300,50))
    print_text(credits_txt,main_menu_font,250,150)
    
    sfx_state()

    if back_btn.draw(screen):
        state = state_list[0] # sending back to main menu if back button is pressed

def L():

    reset_active()    
    global state,running

    # background
    screen.blit(placeholder_background,(0,0))

    # losing screen image
    screen.blit(lost_img,(472,250))

    # buttons
    if try_again_btn.draw(screen):
        state = state_list[1]
    if main_menu_btn.draw(screen):
        state = state_list[0]
    if quit_btn.draw(screen):
        running = False

def W():

    reset_active()
    global state,running

    # background
    screen.blit(placeholder_background,(0,0))

    # winning screen image
    screen.blit(won_img,(472,250))

    # buttons
    if play_again_btn.draw(screen):
        state = state_list[1]
    if main_menu_btn.draw(screen):
        state = state_list[0]
    if quit_btn.draw(screen):
        running = False



# game loop to run the window


while running:

    mouse_pos = pg.mouse.get_pos()  # Get mouse position

    # change screens

    if state == state_list[0]:
        main_menu()
    elif state == state_list[1]:
        start()
    elif state == state_list[2]:
        instructions()
    elif state == state_list[3]:
        credits()
    elif state == state_list[4]:
        L()
    elif state == state_list[5]:
        W()
    
    #  event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:   # close button functioning
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if (sfx_off.rect.collidepoint(mouse_pos) or sfx_on.rect.collidepoint(mouse_pos)):
                sound_state = not sound_state   # switching between sfx on and off
                
        if event.type == pg.KEYDOWN:
            if state in state_list[2:6] and event.key == pg.K_ESCAPE:   
                state = state_list[0]       # pressing ESC key on some screens sends back to the main menu
            
            # player movement
            if event.key in (pg.K_d, pg.K_RIGHT):
                player.right_pressed = True
            if event.key in (pg.K_a, pg.K_LEFT):
                player.left_pressed = True
            if event.key in (pg.K_w, pg.K_UP):
                player.jump = True

        if event.type == pg.KEYUP:
            if event.key in (pg.K_d, pg.K_RIGHT):
                player.right_pressed = False
            if event.key in (pg.K_a, pg.K_LEFT):
                player.left_pressed = False

    player.move()
    player.onPlatform()
    clock.tick(fps)         
    pg.display.update()     # keeps updating the screen
