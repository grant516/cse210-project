import os

RANGE = 65
TRACKING = 150
BOSS_TRACKING = 300

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAP_HEIGHT = 2400
MAP_WIDTH = 2400

MAX_X = 800
MAX_Y = 600
NUM_ENEMY = 50

BOSS_SPEED = 1
ENEMY_SPEED = 2

NUM_KEYS = 5


ENEMY_Y = MAX_Y / 2

PLAYER_Y = 25

PLAYER_MOVE_SCALE = 3

BRICK_WIDTH = 25
BRICK_HEIGHT = 15
BRICK_SPACE = 10

ENEMY_CAN_DIE = False

PLAYER_ATTACK_POWER = 2

HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10

HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25

TILE_SCALING = 1

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 325
RIGHT_VIEWPORT_MARGIN = 325
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 150


PATH = os.path.dirname(os.path.abspath(__file__))
ENEMY_IMAGE = os.path.join(PATH, "..", "assets/goomba.png")
PLAYER_IMAGE = os.path.join(PATH, "..", "assets/player.png")
ATTACK_PLAYER_IMAGE = os.path.join(PATH, "..", "assets/goomba2.png")
KEY_IMAGE = os.path.join(PATH, "..", "assets/keys.png")
MAP = os.path.join(PATH, "..", "assets/final_map.tmx")
GROUND = os.path.join(PATH, "..", "assets/ground.png")

#Boss Image
BOSS_1 = os.path.join(PATH, "..", "assets/boss_1.png")
BOSS_2 = os.path.join(PATH, "..", "assets/boss_2.png")

#The walking sprite images
PLAYER_RIGHT1 = os.path.join(PATH, "..", "assets/player_walking_right_1.png")
PLAYER_RIGHT2 = os.path.join(PATH, "..", "assets/player_walking_right_2.png")
PLAYER_LEFT1 = os.path.join(PATH, "..", "assets/player_walking_left_1.png")
PLAYER_LEFT2 = os.path.join(PATH, "..", "assets/player_walking_left_2.png")
PLAYER_UP1 = os.path.join(PATH, "..", "assets/player_walking_up_1.png")
PLAYER_UP2 = os.path.join(PATH, "..", "assets/player_walking_up_2.png")
PLAYER_DOWN1 = os.path.join(PATH, "..", "assets/player_walking_down_1.png")
PLAYER_DOWN2 = os.path.join(PATH, "..", "assets/player_walking_down_2.png")

#Sword Images
PLAYER_SWORD_RIGHT_1 = os.path.join(PATH, "..", "assets/right_sword_1.png")
PLAYER_SWORD_RIGHT_2 = os.path.join(PATH, "..", "assets/right_sword_2.png")
PLAYER_SWORD_RIGHT_3 = os.path.join(PATH, "..", "assets/right_sword_3.png")

PLAYER_SWORD_LEFT_1 = os.path.join(PATH, "..", "assets/left_sword_1.png")
PLAYER_SWORD_LEFT_2 = os.path.join(PATH, "..", "assets/left_sword_2.png")
PLAYER_SWORD_LEFT_3 = os.path.join(PATH, "..", "assets/left_sword_3.png")

PLAYER_SWORD_DOWN_1 = os.path.join(PATH, "..", "assets/down_sword_1.png")
PLAYER_SWORD_DOWN_2 = os.path.join(PATH, "..", "assets/down_sword_2.png")
PLAYER_SWORD_DOWN_3 = os.path.join(PATH, "..", "assets/down_sword_3.png")

PLAYER_SWORD_UP_1 = os.path.join(PATH, "..", "assets/up_sword_1.png")
PLAYER_SWORD_UP_2 = os.path.join(PATH, "..", "assets/up_sword_2.png")
PLAYER_SWORD_UP_3 = os.path.join(PATH, "..", "assets/up_sword_3.png")

PLAYER_FRAMES = 4

RIGHT_FACING = 0
LEFT_FACING = 1
UP_FACING = 2
DOWN_FACING = 3

PLAYER_MAX_HEALTH = 100
ENEMY_MAX_HEALTH = 5
BOSS_MAX_HEALTH = 150

MUSIC_VOLUME = 0.2
BACKGROUND_MUSIC = os.path.join(PATH, "..", "sounds/Overworld.mp3")
#BACKGROUND_MUSIC = os.path.join(PATH, "..", "sounds/1_MainTheme_320bit.mp3")

SWORD_WOOSH = os.path.join(PATH, "..", "sounds/sword_woosh.mp3")

