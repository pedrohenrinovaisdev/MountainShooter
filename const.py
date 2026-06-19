#C
import pygame

COLOR_ORANGE= (255, 175, 23)
COLOR_WHITE = (255, 255, 255)
COLOR_SKY = (72, 147, 255)
COLOR_YELLOW = (235, 214, 40)
COLOR_GREEN = (40, 143, 22)

#E
ENTITY_SPEED = {
    'c1_bg0': 0,
    'c1_bg1': 1,
    'c1_bg2': 2,
    'c1_bg3': 3,
    'Player1': 5,
    'Player1shot': 5,
    'Player2': 3,
    'Player2shot': 4,
    'Enemy1': 2,
    'Enemy1shot': 5,
    'Enemy2': 1,
    'Enemy2shot': 4,

}

ENTITY_HEALTH ={
    'c1_bg0': 999,
    'c1_bg1': 999,
    'c1_bg2': 999,
    'c1_bg3': 999,
    'Player1': 300,
    'Player1shot': 1,
    'Player2': 300,
    'Player2shot': 1,
    'Enemy1': 50,
    'Enemy1shot': 1,
    'Enemy2': 60,
    'Enemy2shot': 1,
}

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 45,
    'Enemy1': 60,
    'Enemy2': 90


}

#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {
    'Player1': pygame.K_w,
    'Player2': pygame.K_UP
}
PLAYER_KEY_DOWN = {
    'Player1': pygame.K_s,
    'Player2': pygame.K_DOWN
}
PLAYER_KEY_LEFT = {
    'Player1': pygame.K_a,
    'Player2': pygame.K_LEFT
}
PLAYER_KEY_RIGHT = {

    'Player1': pygame.K_d,
    'Player2': pygame.K_RIGHT
}
PLAYER_KEY_SHOT = {
    'Player1': pygame.K_LCTRL,
    'Player2': pygame.K_RCTRL
}

#S
SPAWN_TIME = 4000

#W
WIN_WIDTH = 576
WIN_HEIGHT = 324



