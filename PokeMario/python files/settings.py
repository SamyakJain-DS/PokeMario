win_x, win_y = 1600,900   # width,height 
title = "Pokémario"    # window Title
fps = 45                 # sets frame rate to 60

state_list = ['main','ins','credits','L','W','lvl1','lvl2']   # different game states
state = state_list[0]    # current game state (initial is 'main')

sound_state = False   # sounds off by default
scroll = 0       #background scroll variable

running = True     # game loop run   

doorBool = False    # if door is open or not
door_dims = (96,96)    # dimensions of the door

timer_running = False    # if we want to show the timer
start_timer = False      # to record the start time
stop_timer = False
seconds = mins = hours = 0
start_time = 0

start_game = False

enemy_projectile_speed = 10
charmander_dims = (64,32)
pidgeott_dims = (64,64)
golbat_dims = (150,150)
haunter_dims = (96,96)
dugtrio_dims = (76,64)

pikachu_dims = (64,64)
pikabolt_dims = (60,50)
raichu_dims = (96,96)
player_speed = 5

trigger_list = []