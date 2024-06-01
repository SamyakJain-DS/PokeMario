import pygame as pg, time
from assets import *
from button import *
from objects import *
from entities import *
from settings import *

pg.init()
clock = pg.time.Clock()         # to set frame rate

# creating window

srface = pg.Surface((win_x,win_y),pg.SRCALPHA)

pg.display.set_caption(title)
pg.display.set_icon(win_logo)
all_collidable_p = Block.objects_list + Enemy.objects_list + Trap.objects_list + Attack.enemy_attacks + Evolve.objects_list  # list of all objects collidable with the player

# animating background for the game

bg_width = main_menu_bg.get_width()

# sound button functioning

def sfx_state():
    if sound_state:         # SFX toggle
        if state not in [state_list[-1],state_list[-2]]:    
            sfx_on.draw(screen)
    else:
        mixer.music.play(-1)
        if state not in [state_list[-1],state_list[-2]]:    
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

def door(door_x,door_y,trig_list):    # level clearing door

    global state, state_list,doorBool

    if not(False in trig_list):
        doorBool = True

    if doorBool:     # if its open and conditions are met
        screen.blit(door_open,(door_x,door_y))
        door_open_rect = pg.Rect(door_x,door_y,door_dims[0],door_dims[1])
        if player.rect.colliderect(door_open_rect):
            level_reset()
            if state == state_list[-1]:   # if its the last level
                state = state_list[4]     # show victory screen
            else:
                state = state_list[state_list.index(state) + 1] # else go to the next level

            doorBool = False
    else:
        screen.blit(door_closed,(door_x,door_y))

def timer():

    global seconds, mins, hours, timer_running, start_timer, start_time, stop_timer

    if timer_running:

        if start_timer:
            start_time = time.time()
            start_timer = False
        current_time = time.time()
        seconds = int(current_time - start_time)
        if seconds == 60 :
            seconds = 0
            mins += 1
        if mins == 60:
            mins = 0
            hours += 1
        print_text(f'{hours}:{mins}:{seconds}',ingame_font,win_x/2,20,screen)

def level_reset():

    # to reset all active objects so that the player doesnt collide with invisible objects

    global state_list,state_list

    if state != state_list[-1]:
        for obj in Block.objects_list:
            obj.active = False

    player.rect.x, player.rect.y = player_starting_x, player_starting_y  # reset player pos
    player.SPRITES = Pikachu

    for obj in Trap.objects_list:

        obj.active = False

    for obj in Evolve.objects_list:

        obj.active = False

    for obj in all_enemy_objects:
        obj.tick = 0
        Enemy.objects_list.append(obj)
        obj.rem = True
    
    player.evolve = False

def reset_game():

    global doorBool

    player.rect.x, player.rect.y = player_starting_x, player_starting_y  # reset player pos

    for obj in all_enemy_objects:
        obj.tick = 0
        Enemy.objects_list.append(obj)
        obj.rem = True

    for obj in Evolve.objects_list:

        obj.active = True
        obj.display = True
    
    for obj in Block.objects_list:

        obj.active = False
    
    doorBool = False
    player.evolve = False

def main_menu():

    global state,start_timer,start_game,stop_timer

    # background

    moving_background(main_menu_bg)
    transparent_bg((0,0,0,85))
    screen.blit(title_img,(419,50))

    #buttons

    screen.blit(ques_btn,(520,480))
    screen.blit(ques_btn,(520,610))
    screen.blit(ques_btn,(520,740))

    if play_btn.draw(screen):

        reset_game()

        player.lives = 2
        start_game = True
        stop_timer = False
        start_timer = True

        state = state_list[5]  # changing state to change screens

    if instructions_btn.draw(screen):
        state = state_list[1]
    if credits_btn.draw(screen):
        state = state_list[2]

def lvl1():

    global timer_running,trigger_list

    trigger_list = []
    timer_running = True
    screen.blit(lvl_1,(0,0))
    transparent_bg((0,0,0,75))

    screen.blit(pikachu_face,(20,20))
    print_text(f' X {player.lives}',ingame_font,84,30,screen)   # lives count
    player.draw(screen)

    lvl1_dugtrio.draw(screen)
    lvl1_dugtrio.move()

    draw_floor_list(lvl1_floor,screen)                                # drawing  platform
    lvl1_floor_end.draw(screen)
    lvl1_floating.draw(screen)
    lvl1_bigtile.draw(screen)
    lvl1_endtile.draw(screen)

    # drawing player and enemies
    lvl1_pidgeott.loop()               # loops enemy running and shooting
    lvl1_bulbasaur.loop()
    lvl1_thunderstone.draw(screen)

    trigger_list.append(not(lvl1_pidgeott.active))
    trigger_list.append(not(lvl1_bulbasaur.active))

    # door
    door(win_x-door_dims[0] - 5,win_y - lvl1_block_size - door_dims[1] + 5,trigger_list)

def lvl2():

    trigger_list = []
    screen.blit(lvl_2,(0,0))
    transparent_bg((0,0,0,50))

    player.draw(screen)

    starting_block_1.draw(screen)
    starting_block_2.draw(screen)
    starting_block_3.draw(screen)
    starting_block_4.draw(screen)

    bridge.draw(screen)

    floating_1.draw(screen)
    floating_2.draw(screen)
    floating_3.draw(screen)
    floating_4.draw(screen)
    floating_5.draw(screen)

    lvl2_charmander.draw(screen)

    lvl2_golbat.loop()
    lvl2_haunter.loop()

    trigger_list.append(not(lvl2_golbat.active))
    trigger_list.append(not(lvl2_haunter.active))

    lvl2_thunderstone.draw(screen)

    door(win_x-door_dims[0],win_y-(3*lvl1_block_size) - door_dims[1],trigger_list)

    screen.blit(pikachu_face,(20,20))
    print_text(f' X {player.lives}',ingame_font,84,30,screen)   # lives count

def instructions():

    global state,screen

    #background

    moving_background(main_menu_bg)
    transparent_bg((0,0,0,125))
    screen.blit(instructions_title,(332.5,50))
    print_text(instructions_txt,ins_font,375,200,screen)
    
    if back_btn.draw(screen):
        state = state_list[0] # sending back to main menu if back button is pressed
    
def credits():

    global state,screen

    #background

    moving_background(main_menu_bg)
    transparent_bg((0,0,0,125))
    screen.blit(credits_title,(375,50))
    print_text(credits_txt,credits_font,425,200,screen)

    if back_btn.draw(screen):
        state = state_list[0] # sending back to main menu if back button is pressed

def L():

    global state,running, timer_running, start_timer,stop_timer

    reset_game()

    # background
    timer_running = False
    stop_timer = True
    screen.blit(lost_screen_bg,(0,0))

    screen.blit(ques_btn,(50,100))
    screen.blit(ques_btn,(50,400))
    screen.blit(ques_btn,(50,700))

    # losing screen image
    screen.blit(lost_img,(700,50))

    print_text(f"It took you:\n {hours} Hours {mins} Minutes and {seconds} Seconds.", lastscreen_font,450,750,screen)

    # buttons
    if play_again_btn.draw(screen):

        player.lives = 2
        stop_timer = False
        start_timer = True

        state = state_list[5]
    if main_menu_btn.draw(screen):
        state = state_list[0]
    if quit_btn.draw(screen):
        running = False

def W():

    global state,running,timer_running,start_timer,stop_timer

    reset_game()

    # background
    stop_timer = True
    timer_running = False
    screen.blit(win_screen_bg,(0,0))

    screen.blit(ques_btn,(50,100))
    screen.blit(ques_btn,(50,400))
    screen.blit(ques_btn,(50,700))

    # winning screen image
    screen.blit(won_img,(625,50))

    print_text(f"It took you:\n {hours} Hours {mins} Minutes and {seconds} Seconds.", lastscreen_font,450,750,screen)

    # buttons
    if play_again_btn.draw(screen):

        player.lives = 2
        start_timer = True
        stop_timer = False

        state = state_list[5]
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
        instructions()
    elif state == state_list[2]:
        credits()
    elif player.lives < 1:
        L()
    elif state == state_list[4]:
        W()
    elif state == state_list[5]:
        lvl1()
    elif state == state_list[6]:
        lvl2()
    
    #  event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:   # close button functioning
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if (sfx_off.rect.collidepoint(mouse_pos) or sfx_on.rect.collidepoint(mouse_pos)):
                sound_state = not sound_state   # switching between sfx on and off
                
        if event.type == pg.KEYDOWN:
            if state in state_list[1:5] and event.key == pg.K_ESCAPE:
                state = state_list[0]       # pressing ESC key on some screens sends back to the main menu
            if event.key == pg.K_w and not(player.jumpBool) :
                player.jump()
            if event.key == pg.K_j and player.attackBool:
                if player.direction == 'right':
                    if not player.evolve:
                        player.attack = Attack(player.rect.x + pikachu_dims[0],player.rect.y + (pikachu_dims[1]*(0.25)),player.direction,pikachu_bolt_right,10,1,True)
                    else:
                        player.attack = Attack(player.rect.x + raichu_dims[0],player.rect.y + (raichu_dims[1]*(0.25)),player.direction,pikachu_bolt_right,10,1,True)
                else:
                    if not player.evolve:
                        player.attack = Attack(player.rect.x - pikachu_dims[0],player.rect.y + (pikachu_dims[1]*(0.25)),player.direction,pikachu_bolt_left,10,1,True)
                    else:
                        player.attack = Attack(player.rect.x - raichu_dims[0],player.rect.y + (raichu_dims[1]*(0.25)),player.direction,pikachu_bolt_left,10,1,True)
                player.attackBool = False               

    all_collidable_p = Block.objects_list + Enemy.objects_list + Trap.objects_list + Attack.enemy_attacks + Evolve.objects_list  # list of all objects collidable with the player
    if start_game:
        player.loop(fps) # loops the player's functions
        handle_move(player,all_collidable_p) # handles player movements and collision
        handle_collision_enemy(Enemy.objects_list,Attack.player_attack)
    if not(stop_timer):
        timer()
    sfx_state()
    clock.tick(fps)
    pg.display.update()     # keeps updating the screen