import pygame

#КОНСТАНТЫ ОКНА ПРОГРАММЫ
SIZE_OF_WINDOW = WIDTH_OF_WINDOW, HEIGHT_OF_WINDOW = 800, 600       #размер окна
WINDOW_ICON = 'icon.png'                                            #иконка
WINDOW_CAPTION = 'Snake-Game'                                       #название окна

#КОНСТАНТЫ ИГРОВОГО ПОЛЯ
BLOCK_SIZE = 30                                                #размер квадратика
WALL_BLOCKS = 3                                                 #количество блоков в стене 
AMOUNT_OF_RECTS = 20                                            #количество квадратиков
SIZE_X = (WIDTH_OF_WINDOW // BLOCK_SIZE  - WALL_BLOCKS * 2)     #количество блоков поля по X
SIZE_Y = (HEIGHT_OF_WINDOW // BLOCK_SIZE - WALL_BLOCKS * 2)     #количество блоков поля по Y
AMOUNT_OF_BLOCKS = SIZE_X * SIZE_Y

#КОНСТАНТЫ ОТРИСОВКИ БЛОКОВ ИГРЫ
START_SNAKE_X = SIZE_X // 2                         #X_0 координата головы змейки
START_SNAKE_Y = SIZE_Y // 2                         #Y_0 координата головы змейки
APPLE_RADIUS = BLOCK_SIZE // 2                      #радиус яблока
HALF_BLOCK_SIZE = BLOCK_SIZE // 2                   #половина размера квадратика
THREE_QUARTERS_BLOCK_SIZE = BLOCK_SIZE * 3 / 4      #три четверти размера квадратика
QUARTER_BLOCK_SIZE = BLOCK_SIZE // 4                #четверть размера квадратика
BORDERS_SIZE = BLOCK_SIZE * WALL_BLOCKS             #размер границ
SNAKE_X_SEGMENT = (HALF_BLOCK_SIZE, QUARTER_BLOCK_SIZE)     #размер сегмента змейки по OX
SNAKE_Y_SEGMENT = (QUARTER_BLOCK_SIZE, HALF_BLOCK_SIZE)     #размер сегмента змейки по OY

#КОНСТАНТЫ ИГРОВОГО ПРОЦЕССА
INITIAL_FRUIT_COUNT = 3                                #постоянное количество яблок
INITIAL_GAME_SPEED  = 4                          #начальная скорость игры
INITIAL_SNAKE_SIZE = 3                              #начальный размер змейки
MAX_GAME_SPEED = 25                               #максимальная скорость игры
APPLES_TO_INCREASE_SPEED = SIZE_X * SIZE_Y // MAX_GAME_SPEED

# КОНСТАНТЫ ЦВЕТОВ ИГРЫ
WALLS_COLOR = (34, 139, 34)                     # цвет стен (более мягкий зелёный)
GAME_FIELD_COLOR = (240, 255, 240)              # цвет игрового поля (мягкий зелёный)
GAME_FIELD_ADD_COLOR = (220, 225, 220)          # цвет клеток (темный серый)
SNAKE_COLOR = (50, 205, 50)                     # цвет змейки (светло-зелёный)
APPLE_COLOR = (255, 69, 0)                      # цвет яблока (оранжево-красный)
GRAPE_COLOR = (255, 0, 255)
ORANGE_COLOR = (255, 165, 0)

#КОНСТАНТЫ ОЧКОВ
INITIAL_APPLES_SCORE = 1                                #СТОИМОСТЬ ЯБЛОКА
INITIAL_GRAPES_SCORE = 3                                #СТОИМОСТЬ ВИНОГРАДА
INITIAL_ORANGE_SCORE = 1

#КОНСТАНТЫ ВЕРОЯТНОСТЕЙ %
CHANCE_GRAPE =  25
CHANCE_ORANGE = 25                                  
CHANCE_TOTAL = 100

# КОНСТАНТЫ ТЕКСТА
FONT_PATH='shrift.ttf'
CAPTION_FONT_COLOR = (255, 255, 255)
TEXT_FONT_COLOR = (255, 255, 255)
TEXT_FONT_SIZE = BLOCK_SIZE * 2  # размер шрифта текста
CAPTION_FONT_SIZE = BLOCK_SIZE * (WALL_BLOCKS + 1)  # размер шрифта заголовка

# КОНСТАНТА РЕЖИМА ГРАФИКИ
GRAPHIC_MODE=1

#ИНИЦИАЛИЗАЦИЯ PYGAME
pygame.init()

#ИНИЦИАЛИЗАЦИЯ ШРИФТОВ
CAPTION_FONT = pygame.font.SysFont(FONT_PATH, CAPTION_FONT_SIZE)  # шрифт заголовка
CAPTION_FONT=pygame.font.Font(FONT_PATH,CAPTION_FONT_SIZE)
TEXT_FONT = pygame.font.SysFont(FONT_PATH, TEXT_FONT_SIZE)  # шрифт текста
TEXT_FONT = pygame.font.Font(FONT_PATH,39)
TEXT_FONT_74 = pygame.font.Font(FONT_PATH, 74)
TEXT_FONT_33 = pygame.font.Font(FONT_PATH, 33)

#ИНИЦИАЛИЗАЦИЯ МУЗЫКИ
LIST_OF_SOUND=[
    pygame.mixer.Sound('appleSound.mp3'),
    pygame.mixer.Sound('grapeSound.mp3'),
    pygame.mixer.Sound('orangeSound.mp3'),
    pygame.mixer.Sound('appleSound2.mp3'),
    pygame.mixer.Sound('appleSound3.mp3'),
    pygame.mixer.Sound('appleSound4.mp3')
]
GAMEOVER_SOUND = pygame.mixer.Sound('gameOver2.mp3')
pygame.mixer.music.load('music.mp3')

#КОНСТАНТЫ ТЕКСТУР
APPLE_TEXTURE = pygame.image.load('apple.png')  
GRAPE_TEXTURE =  pygame.image.load('grape.png') 
ORANGE_TEXTURE = pygame.image.load('orange.png')
BACGROUND_TEXTURE = pygame.image.load('background.png')
GRACE_TEXTURE = pygame.image.load('Grace.png')
ICON_TEXTURE = pygame.image.load('icon.png')