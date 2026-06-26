#C
import pygame


C_ORANGE = (255, 175, 23)
C_WHITE = (255, 255, 255)
C_SKY = (72, 147, 255)
C_YELLOW = (235, 214, 40)
C_GREEN = (40, 143, 22)
C_PURPLE = (144, 30, 255)
C_RED = (255, 2, 2)

#E
ENTITY_SPEED = {
    'Level1bg0': 0,
    'Level1bg1': 1,
    'Level1bg2': 2,
    'Level1bg3': 3,

    'Level2bg0': 0,
    'Level2bg1': 1,
    'Level2bg2': 2,
    'Level2bg3': 3,
    'Player1': 6,
    'Player1shot': 5,
    'Player2': 4,
    'Player2shot': 4,
    'Enemy1': 3,
    'Enemy1shot': 5,
    'Enemy2': 2,
    'Enemy2shot': 4,

}

ENTITY_HEALTH ={
    'Level1bg0': 999,
    'Level1bg1': 999,
    'Level1bg2': 999,
    'Level1bg3': 999,

    'Level2bg0': 999,
    'Level2bg1': 999,
    'Level2bg2': 999,
    'Level2bg3': 999,
    'Player1': 300,
    'Player1shot': 1,
    'Player2': 500,
    'Player2shot': 1,
    'Enemy1': 50,
    'Enemy1shot': 1,
    'Enemy2': 60,
    'Enemy2shot': 1,
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 35,
    'Enemy1': 60,
    'Enemy2': 90

}

ENTITY_DAMAGE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,

    'Level2bg0': 0,
    'Level2bg1': 0,
    'Level2bg2': 0,
    'Level2bg3': 0,
    'Player1': 1,
    'Player1shot': 30,
    'Player2': 1,
    'Player2shot': 60,
    'Enemy1': 1,
    'Enemy1shot': 20,
    'Enemy2': 1,
    'Enemy2shot': 15,
}

ENTITY_SCORE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,

    'Level2bg0': 0,
    'Level2bg1': 0,
    'Level2bg2': 0,
    'Level2bg3': 0,
    'Player1': 1,
    'Player1shot': 0,
    'Player2': 0,
    'Player2shot': 0,
    'Enemy1shot': 0,
    'Enemy2shot': 0,
    'Enemy1': 100,
    'Enemy2': 200,
}


#
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
    'Player1': pygame.K_SPACE,
    'Player2': pygame.K_RCTRL
}

#S
SPAWN_TIME = 1000

#T
TIMEOUT_STEP = 100

TIMEOUT_LEVEL = 10000

#W
WIN_WIDTH = 576
WIN_HEIGHT = 324

#S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH/ 2, 80),
             'Label': (WIN_WIDTH/ 2, 90),
             'Name': (WIN_WIDTH/ 2, 100),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
}

