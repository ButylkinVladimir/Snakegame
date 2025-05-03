import pygame
import sys
import random
import DrawModule as DRAW
from DrawModule import TOOLS
############## 1. ФУНКЦИИ БЛОКА MAIN

### 1.1 Инициализация программы
def initialize_program():
    pygame.display.set_caption(TOOLS.WINDOW_CAPTION)                  #название окна                 
    pygame.display.set_icon(TOOLS.ICON_TEXTURE)                               #установка иконки
    screen_of_game = pygame.display.set_mode(TOOLS.SIZE_OF_WINDOW)    #инициализация окна
    clock = pygame.time.Clock()                                 #инициализация clock для стабильности             

    return screen_of_game, clock

### 1.2 Инициализация состояния игры
def initialize_game_state():
    game_state = {
        "program_running": True,
        "game_running": False,
        "game_paused": False,
        "game_won": False,
        "game_over": False,
        "apples": [],
        "grapes":[],
        "oranges":[],
        "snake": [],
        "direction": None,
        "last_direction": None,
        "score": 0,
        "apples_eaten": 0,
        "grapes_eaten": 0,
        "oranges_eaten": 0,
        "game_speed": TOOLS.INITIAL_GAME_SPEED
    }
    return game_state

### 1.3 Завершение игры
def perform_ending_actions():
    pygame.quit()
    sys.exit()


############## 2. ФУНКЦИИ состояния игры
 
### 2.1 Получение событий игры
def get_game_events():
    events = []                                 #список всех событий
    for event in pygame.event.get():            #получаем событие
        if event.type == pygame.QUIT:           #если событие - выход
            events.append('quit')
        elif event.type == pygame.KEYDOWN:      #если событие - нажатие клавиши
            if event.key == pygame.K_UP:        #вверх
                events.append('up')
            elif event.key == pygame.K_DOWN:    #вниз
                events.append('down')
            elif event.key == pygame.K_LEFT:    #влево
                events.append('left')
            elif event.key == pygame.K_RIGHT:   #вправо
                events.append('right')
            elif event.key == pygame.K_RETURN:  #Enter
                events.append('enter')
            elif event.key == pygame.K_SPACE:   #пробел
                events.append('space')
            elif event.key == pygame.K_ESCAPE:  #ESC
                events.append('escape')
             
    return events

### 2.2 Обновление состояния игры внутри программы
def update_game_state(game_state, events):
    process_keys_events(game_state, events)             #обработать нажатия клавиш
    if game_state["game_running"] and not game_state["game_paused"]:# если игра запущена и не на паузе
        move_snake(game_state)                          # передвинуть змейку
        check_collisions(game_state)                    # проверить столкновения
        check_eat_apple(game_state)                     # проверить съедание яблока
        check_eat_grape(game_state)                     # проверить съедание винограда
        check_eat_orange(game_state)                    # проверить съедание апельсина
        check_game_won(game_state)                      # проверить выигрыш

### 2.2.1 Обработка событий нажатия клавиш
def process_keys_events(game_state, events):
    if "quit" in events:                                #если событие - выход
        game_state["program_running"] = False
    elif not game_state["game_running"] and not game_state["game_over"]:#если игра не запущена
        if "escape" in events:                          #если нажата ESC
            game_state["program_running"] = False
        elif "enter" in events:                         #если нажата Enter
            initialize_new_game(game_state)             #начать новую игру
            game_state["game_running"] = True
    elif game_state["game_paused"] == True:             #если игра на паузе
        if "escape" in events:                          #если нажата ESC
            game_state["game_running"] = False
        elif "space" in events:                         #если нажата пробел
            game_state["game_paused"] = False
    elif game_state["game_over"]:
        if "escape" in events:                          #если нажата ESC
            game_state["program_running"] = False
        elif "enter" in events:                         #если нажата Enter
            game_state["game_over"] = False
            game_state["game_running"] = True
            initialize_new_game(game_state)             #начать новую игру

    else:                                               #игра запущена
        if "escape" in events or "space" in events:     #если нажата пауза
            game_state["game_paused"] = True
        for direction in ['down', 'up', 'right', 'left']:  #движение змейки
            if direction in events:                      #если нажата клавиша движения
                game_state["direction"] = direction
                break
            else:
                game_state["direction"] = game_state["last_direction"]

### 2.2.1.1 Начать новую игру
def initialize_new_game(game_state):
    #музыка
    pygame.mixer.music.set_volume(0.2)

    # положение змейки
    game_state["snake"] = []
    place_snake(TOOLS.INITIAL_SNAKE_SIZE, game_state)

    # положение фруктов
    game_state["apples"] =  []
    game_state["grapes"] =  []
    game_state["oranges"] = []

    for _ in range(0, TOOLS.INITIAL_FRUIT_COUNT):
        place_fruit(game_state)

    # направление движения змейки
    game_state["direction"] = 'right'
    game_state["last_direction"] = 'right'

    # состояние игр
    game_state["game_paused"] = False
    game_state["game_over"] = False
    game_state["game_speed"] = TOOLS.INITIAL_GAME_SPEED 

    # сколько очков
    game_state["score"] = 0
    pygame.mixer.music.play(-1)

### 2.2.1.1.1 Разместить змейку
def place_snake(length, game_state):
    x = TOOLS.START_SNAKE_X
    y = TOOLS.START_SNAKE_Y
    game_state["snake"].append((x, y))
    for i in range(1, length):
        game_state["snake"].append((x - i, y))

def place_fruit(game_state):
    x = random.randint(0, TOOLS.SIZE_X - 1)
    y = random.randint(0, TOOLS.SIZE_Y - 1)
    while (x, y) in game_state["apples"]   \
        or (x, y) in game_state["grapes"]  \
        or (x, y) in game_state["oranges"] \
        or (x, y) in game_state["snake"]:
        x = random.randint(0, TOOLS.SIZE_X - 1)
        y = random.randint(0, TOOLS.SIZE_Y - 1)

    chance_grape  = TOOLS.CHANCE_GRAPE
    chance_orange = TOOLS.CHANCE_ORANGE
    if chance_grape + chance_orange > TOOLS.CHANCE_TOTAL:
        chance_grape  = 25
        chance_orange = 25

    chance = random.randint(0,TOOLS.CHANCE_TOTAL)
    if chance >= 0 and chance <= chance_grape:
        game_state["grapes"].append((x, y))
    elif chance >= chance_grape and chance <= chance_grape + chance_orange:
        game_state["oranges"].append((x, y))
    else:
        game_state["apples"].append((x, y))

### 2.2.2 Передвинуть змейку
def move_snake(game_state):
    if game_state["direction"] == "up" and game_state["last_direction"] != "down":
        x_dir, y_dir = get_x_y_directions("up")
        game_state["last_direction"] = "up"
    elif game_state["direction"] == "down" and game_state["last_direction"] != "up":
        x_dir, y_dir = get_x_y_directions("down")
        game_state["last_direction"] = "down"
    elif game_state["direction"] == "left" and game_state["last_direction"] != "right":
        x_dir, y_dir = get_x_y_directions("left")
        game_state["last_direction"] = "left"
    elif game_state["direction"] == "right" and game_state["last_direction"] != "left":
        x_dir, y_dir = get_x_y_directions("right")
        game_state["last_direction"] = "right"
    else:
        x_dir, y_dir = get_x_y_directions(f"{game_state['last_direction']}")
    head = game_state["snake"][0]
    new_head = (head[0] + x_dir, head[1] + y_dir)
    game_state["snake"].insert(0, new_head)
    game_state["snake"].pop()

### 2.2.2.1 Расшифровать движения
def get_x_y_directions(forward):
    if forward == "right":
        return (1, 0)
    elif forward == "left":
        return (-1, 0)
    elif forward == "up":
        return (0, -1)
    elif forward == "down":
        return (0, 1)
    
def get_forward(direction_x,direction_y):
    if  direction_x == 1 and direction_y == 0:
        return "right"
    elif  direction_x == -1 and direction_y == 0:
        return "left"
    elif  direction_x == 0 and direction_y == -1:
        return "up"
    elif  direction_x ==0 and direction_y == 1:
        return "down"
    
### 2.2.3 Проверить столкновения
def check_collisions(game_state):
    x_head, y_head = game_state["snake"][0]
    if x_head < 0 or x_head >= TOOLS.SIZE_X or y_head < 0 or y_head >= TOOLS.SIZE_Y:
        game_state["game_running"] = False
        game_state["game_over"] = True

    if len(game_state["snake"]) > len(set(game_state["snake"])):
        game_state["game_running"] = False
        game_state["game_over"] = True

    if game_state["game_over"]:
        pygame.mixer.music.stop()
        TOOLS.GAMEOVER_SOUND.play()

### 2.2.4 Проверить съедание яблока
def check_eat_apple(game_state):
    x_head, y_head = game_state["snake"][0]
    if (x_head, y_head) in game_state["apples"]:
        game_state["apples"].remove((x_head, y_head))
        game_state["snake"].append((x_head, y_head))   

        place_fruit(game_state)

        game_state["score"] += TOOLS.INITIAL_APPLES_SCORE
        game_state["apples_eaten"] += 1

        if (game_state["game_speed"] < TOOLS.MAX_GAME_SPEED) and (game_state["apples_eaten"] % TOOLS.APPLES_TO_INCREASE_SPEED) == 0:
            game_state["game_speed"] += 1

        TOOLS.LIST_OF_SOUND[ random.randint(0, len(TOOLS.LIST_OF_SOUND)-1)].play()
### Проверить съедание винограда
def check_eat_grape(game_state):
    
    x_head, y_head = game_state["snake"][0]
    if (x_head, y_head) in game_state["grapes"]:
        game_state["grapes"].remove((x_head, y_head))
        game_state["snake"].append((x_head, y_head))

        place_fruit(game_state)

        game_state["score"] += TOOLS.INITIAL_GRAPES_SCORE
        game_state["grapes_eaten"] += 1

        TOOLS.LIST_OF_SOUND[ random.randint(0, len(TOOLS.LIST_OF_SOUND)-1)].play()

def check_eat_orange(game_state):
    x_head, y_head = game_state["snake"][0]
    if (x_head, y_head) in game_state["oranges"]:
        game_state["oranges"].remove((x_head, y_head))

        tail1 = game_state["snake"][-1]
        tail2 = game_state["snake"][-2]

        game_state["snake"].reverse()
        game_state["snake"].append(game_state["snake"][0]) 

        place_fruit(game_state)

        game_state["score"] += TOOLS.INITIAL_ORANGE_SCORE
        game_state["oranges_eaten"] += 1
 
        direction_x=tail1[0]-tail2[0]
        direction_y=tail1[1]-tail2[1]

        forward=get_forward(direction_x,direction_y)
        game_state["direction"] = forward
        game_state["last_direction"] = forward

        move_snake(game_state) 

        TOOLS.LIST_OF_SOUND[ random.randint(0, len(TOOLS.LIST_OF_SOUND)-1)].play()
### 2.2.5 Проверить выигрыш
def check_game_won(game_state):
    if TOOLS.AMOUNT_OF_BLOCKS - len(game_state["snake"]) == 0:
        game_state["game_won"] = True
        game_state["game_running"] = False

### 2.3 Отрисовка состояния игры
def update_game_screen(screen_of_game, game_state):
    screen_of_game.fill(TOOLS.GAME_FIELD_COLOR)
    if not game_state["game_running"] and not game_state["game_over"]:
        DRAW.draw_new_game_screen(screen_of_game)
    elif game_state["game_won"]:
        DRAW.draw_game_won_screen(screen_of_game)
    elif game_state["game_over"]:
        DRAW.draw_game_over_screen(screen_of_game)
    else:
        DRAW.draw_background(screen_of_game)
        DRAW.draw_game_field(screen_of_game)
        DRAW.draw_snake(screen_of_game, game_state["snake"], game_state["direction"])
        DRAW.draw_apples(screen_of_game, game_state["apples"])
        DRAW.draw_grapes(screen_of_game, game_state["grapes"])
        DRAW.draw_oranges(screen_of_game, game_state["oranges"])
        if game_state["game_paused"]:
            DRAW.draw_paused_screen(screen_of_game)
        DRAW.draw_score(screen_of_game, game_state["score"], game_state["game_speed"])
    pygame.display.update()
############## MAIN ##############
def main():

    screen_of_game, clock = initialize_program()
    game_state = initialize_game_state()

    while game_state["program_running"]:
        clock.tick(game_state["game_speed"])

        # 1. считать все события
        events = get_game_events()

        # 2. изменить состояние игры внутри pyhton
        update_game_state(game_state, events)

        # 3. отрисовать состояние игры на игре
        update_game_screen(screen_of_game, game_state)

    perform_ending_actions()

if __name__ == "__main__":
    main()