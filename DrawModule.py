import pygame
import SnakeTools as TOOLS

######ТЕСТ Отрисовать Игровое поле
def draw_game_field(screen_of_game):
    for column in range(TOOLS.SIZE_X):
        for row in range(TOOLS.SIZE_Y):
            rect = pygame.Rect(TOOLS.BORDERS_SIZE + column * TOOLS.BLOCK_SIZE, TOOLS.BORDERS_SIZE + row * TOOLS.BLOCK_SIZE, TOOLS.BLOCK_SIZE, TOOLS.BLOCK_SIZE)
            if (column + row) % 2 == 0:
                pygame.draw.rect(screen_of_game, TOOLS.GAME_FIELD_COLOR, rect)
            else:
                pygame.draw.rect(screen_of_game, TOOLS.GAME_FIELD_ADD_COLOR, rect)    

#ОТРИСОВАТЬ ЗАДНИЙ ФОН
def draw_background(screen_of_game):
    if TOOLS.GRAPHIC_MODE==1:
        new_texture_background=pygame.transform.scale(TOOLS.BACGROUND_TEXTURE,(TOOLS.WIDTH_OF_WINDOW, TOOLS.HEIGHT_OF_WINDOW))
        screen_of_game.blit(new_texture_background,(0,0))
        new_texture_Grace=pygame.transform.scale(TOOLS.GRACE_TEXTURE,(TOOLS.WIDTH_OF_WINDOW, TOOLS.HEIGHT_OF_WINDOW))
        screen_of_game.blit(new_texture_Grace,(0,0))
    else:
        screen_of_game.fill(TOOLS.WALLS_COLOR)
        
### 2.3.1 Отрисовать Новая игра
def draw_new_game_screen(screen_of_game):
    draw_background(screen_of_game)
    newgame_caption_text = TOOLS.CAPTION_FONT.render("Змейка", True, TOOLS.CAPTION_FONT_COLOR)
    start_game_text = TOOLS.TEXT_FONT.render("Нажмите Enter для начала игры", True, TOOLS.TEXT_FONT_COLOR)
    exit_text = TOOLS.TEXT_FONT.render("Нажмите Escape для выхода", True, TOOLS.TEXT_FONT_COLOR)

    newgame_caption_rect = newgame_caption_text.get_rect(center=(TOOLS.SIZE_OF_WINDOW[0] // 2, TOOLS.SIZE_OF_WINDOW[1] // 3))
    start_game_rect = start_game_text.get_rect(center=(TOOLS.SIZE_OF_WINDOW[0] // 2, TOOLS.SIZE_OF_WINDOW[1] // 2))
    exit_rect = exit_text.get_rect(center=(TOOLS.SIZE_OF_WINDOW[0] // 2, TOOLS.SIZE_OF_WINDOW[1] // 1.5))

    screen_of_game.blit(newgame_caption_text, newgame_caption_rect)
    screen_of_game.blit(start_game_text, start_game_rect)
    screen_of_game.blit(exit_text, exit_rect)

### 2.3.2 Отрисовать Пауза
def draw_paused_screen(screen_of_game):
    overlay = pygame.Surface((TOOLS.SIZE_OF_WINDOW))
    overlay.set_alpha(180)          # Устанавливаем прозрачность
    overlay.fill((0, 0, 0))         # Черный фон
    screen_of_game.blit(overlay, (0, 0))
    
    pause_caption_text = TOOLS.CAPTION_FONT.render("Игра на паузе", True, TOOLS.CAPTION_FONT_COLOR)
    continue_text = TOOLS.TEXT_FONT.render("Нажмите Пробел для продолжения", True, TOOLS.TEXT_FONT_COLOR)
    exit_text = TOOLS.TEXT_FONT.render("Нажмите Escape чтобы выйти", True, TOOLS.TEXT_FONT_COLOR)
    
    pause_caption_rect = pause_caption_text.get_rect(center=(TOOLS.SIZE_OF_WINDOW[0] // 2, TOOLS.SIZE_OF_WINDOW[1] // 3))
    continue_rect = continue_text.get_rect(center=(TOOLS.SIZE_OF_WINDOW[0] // 2, TOOLS.SIZE_OF_WINDOW[1] // 2))
    exit_rect = exit_text.get_rect(center=(TOOLS.SIZE_OF_WINDOW[0] // 2, TOOLS.SIZE_OF_WINDOW[1] // 1.6))
    
    screen_of_game.blit(pause_caption_text, pause_caption_rect)
    screen_of_game.blit(continue_text, continue_rect)
    screen_of_game.blit(exit_text, exit_rect)

### 2.3.3.2.1 Отрисовать Тело ЛЕВУЮ часть сегмента тела
def draw_snake_body_left(screen_of_game, x_0, y_0):
    x_start_point = x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE
    y_start_point = (y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE) + TOOLS.QUARTER_BLOCK_SIZE
    rect_segement = (x_start_point, y_start_point, TOOLS.HALF_BLOCK_SIZE, TOOLS.HALF_BLOCK_SIZE)
    pygame.draw.rect(screen_of_game, TOOLS.SNAKE_COLOR, rect_segement)

### 2.3.3.2.2 Отрисовать Тело ВЕРХНЮЮ часть сегмента тела
def draw_snake_body_top(screen_of_game, x_0, y_0):
    x_start_point = (x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE) + TOOLS.QUARTER_BLOCK_SIZE
    y_start_point = y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE
    rect_segement = (x_start_point, y_start_point, TOOLS.HALF_BLOCK_SIZE, TOOLS.HALF_BLOCK_SIZE)
    pygame.draw.rect(screen_of_game, TOOLS.SNAKE_COLOR, rect_segement)

### 2.3.3.2.3 Отрисовать Тело ПРАВУЮ часть сегмента тела
def draw_snake_body_right(screen_of_game, x_0, y_0):
    x_start_point = (x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE) + TOOLS.HALF_BLOCK_SIZE
    y_start_point = (y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE) + TOOLS.QUARTER_BLOCK_SIZE
    rect_segement = (x_start_point, y_start_point, TOOLS.HALF_BLOCK_SIZE, TOOLS.HALF_BLOCK_SIZE)
    pygame.draw.rect(screen_of_game, TOOLS.SNAKE_COLOR, rect_segement) 

### 2.3.3.2.4 Отрисовать Тело НИЖНЮЮ часть сегмента тела
def draw_snake_body_bottom(screen_of_game, x_0, y_0):
    x_start_point = (x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE) + TOOLS.QUARTER_BLOCK_SIZE
    y_start_point = (y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE) + TOOLS.HALF_BLOCK_SIZE
    rect_segement = (x_start_point, y_start_point, TOOLS.HALF_BLOCK_SIZE, TOOLS.HALF_BLOCK_SIZE)
    pygame.draw.rect(screen_of_game, TOOLS.SNAKE_COLOR, rect_segement)

### 2.3.3.2.5 Отрисовать Тело КРУГ для сглаживания
def draw_snake_body_circle(screen_of_game, x_0, y_0):
    x_start_point = (x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE) + TOOLS.HALF_BLOCK_SIZE
    y_start_point = (y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE) + TOOLS.HALF_BLOCK_SIZE
    pygame.draw.circle(screen_of_game, TOOLS.SNAKE_COLOR, (x_start_point, y_start_point), TOOLS.QUARTER_BLOCK_SIZE)

### 2.3.3.1 Отрисовать Голову
def draw_snake_head(screen_of_game, head, neck):
    x_head, y_head = head
    x_prev, y_prev = neck
    delta_x_prev = x_head - x_prev             #изменение X координаты по отношению к ПРЕДЫДУЩЕМУ
    delta_y_prev = y_head - y_prev             #изменение Y координаты по отношению к ПРЕДЫДУЩЕМУ

    if (delta_x_prev > 0):
        draw_snake_body_left(screen_of_game, x_head, y_head)
    if (delta_y_prev > 0):
        draw_snake_body_top(screen_of_game, x_head, y_head)
    if (delta_x_prev < 0):
        draw_snake_body_right(screen_of_game, x_head, y_head)
    if (delta_y_prev < 0):
        draw_snake_body_bottom(screen_of_game, x_head, y_head)
    
    x_start_point = (x_head * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE) + TOOLS.HALF_BLOCK_SIZE
    y_start_point = (y_head * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE) + TOOLS.HALF_BLOCK_SIZE
    pygame.draw.circle(screen_of_game, TOOLS.SNAKE_COLOR, (x_start_point, y_start_point), TOOLS.HALF_BLOCK_SIZE)

### 2.3.3.2 Отрисовать Тело
def draw_snake_body(screen_of_game, snake):
    for i, segment in enumerate(snake[1:-1]):
        i +=1                                   #счётчик сегментов +1 т.к. начинаем со snake[1]
        x_0, y_0 = segment                      #кооридаты текущего сегмента
        x_next, y_next = snake[i + 1]           #кооридаты следующего сегмента
        x_prev, y_prev = snake[i - 1]           #кооридаты предыдущего сегмента

        delta_x_next = x_0 - x_next             #изменение X координаты по отношению к СЛЕДУЮЩЕМУ
        delta_y_next = y_0 - y_next             #изменение Y координаты по отношению к СЛЕДУЮЩЕМУ
        delta_x_prev = x_0 - x_prev             #изменение X координаты по отношению к ПРЕДЫДУЩЕМУ
        delta_y_prev = y_0 - y_prev             #изменение Y координаты по отношению к ПРЕДЫДУЩЕМУ

        if (delta_x_next > 0 or delta_x_prev > 0):
            draw_snake_body_left(screen_of_game, x_0, y_0)
        if (delta_y_next > 0 or delta_y_prev > 0):
            draw_snake_body_top(screen_of_game, x_0, y_0)
        if (delta_x_next < 0 or delta_x_prev < 0):
            draw_snake_body_right(screen_of_game, x_0, y_0)
        if (delta_y_next < 0 or delta_y_prev < 0):
            draw_snake_body_bottom(screen_of_game, x_0, y_0)
        if (not (delta_x_next == 0 and delta_x_prev == 0)) or (not (delta_y_next == 0 and delta_y_prev == 0)):
            draw_snake_body_circle(screen_of_game, x_0, y_0)

### 2.3.3.3.1 Отрисовать Хвост ЛЕВУЮ часть сегмента тела
def draw_snake_tail_left(screen_of_game, x_0, y_0):
    draw_snake_body_right(screen_of_game, x_0, y_0)

    tail_points = []
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE))
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.QUARTER_BLOCK_SIZE))
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.BLOCK_SIZE  * 3 / 4))
    
    pygame.draw.polygon(screen_of_game, TOOLS.SNAKE_COLOR, tail_points)
    tail_points = []

### 2.3.3.3.2 Отрисовать Хвост ВЕРХНЮЮ часть сегмента тела
def draw_snake_tail_top(screen_of_game, x_0, y_0):
    draw_snake_body_bottom(screen_of_game, x_0, y_0)

    tail_points = []
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE))
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.THREE_QUARTERS_BLOCK_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE))
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.QUARTER_BLOCK_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE +TOOLS.HALF_BLOCK_SIZE))
    
    pygame.draw.polygon(screen_of_game, TOOLS.SNAKE_COLOR, tail_points)
    tail_points = []

### 2.3.3.3.3 Отрисовать Хвост ПРАВУЮ часть сегмента тела
def draw_snake_tail_right(screen_of_game, x_0, y_0):
    draw_snake_body_left(screen_of_game, x_0, y_0)

    tail_points = []
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE +TOOLS.BORDERS_SIZE + TOOLS.BLOCK_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE))
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.THREE_QUARTERS_BLOCK_SIZE))
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.QUARTER_BLOCK_SIZE))
    
    pygame.draw.polygon(screen_of_game, TOOLS.SNAKE_COLOR, tail_points)
    tail_points = []

### 2.3.3.3.4 Отрисовать Хвост НИЖНЮЮ часть сегмента тела
def draw_snake_tail_bottom(screen_of_game, x_0, y_0):
    draw_snake_body_top(screen_of_game, x_0, y_0)

    tail_points = []
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.BLOCK_SIZE))
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.QUARTER_BLOCK_SIZE, y_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE))
    tail_points.append((x_0 * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.THREE_QUARTERS_BLOCK_SIZE, y_0 *TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.HALF_BLOCK_SIZE))
    
    pygame.draw.polygon(screen_of_game, TOOLS.SNAKE_COLOR, tail_points)
    tail_points = []

### 2.3.3.3 Отрисовать Хвост
def draw_snake_tail(screen_of_game, pretail, tail):
    x_tail, y_tail = tail
    x_next, y_next = pretail

    x_tail_delta = x_tail - x_next
    y_tail_delta = y_tail - y_next

    if (x_tail_delta < 0):
        draw_snake_tail_left(screen_of_game, x_tail, y_tail)
    if (y_tail_delta < 0):
        draw_snake_tail_top(screen_of_game, x_tail, y_tail)
    if (x_tail_delta > 0):
        draw_snake_tail_right(screen_of_game, x_tail, y_tail)
    if (y_tail_delta > 0):
        draw_snake_tail_bottom(screen_of_game, x_tail, y_tail)
    pass

### 2.3.3 Отрисовать Змейка
def draw_snake(screen_of_game, snake, direction):
    draw_snake_head(screen_of_game, snake[0], snake[1])
    draw_snake_body(screen_of_game, snake)
    draw_snake_tail(screen_of_game, snake[-2], snake[-1])

### 2.3.4 Отрисовать Яблоки
def draw_apples(screen_of_game, apples):
    for apple in apples:
        x_apple = apple[0] * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE
        y_apple = apple[1] * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE
        if TOOLS.GRAPHIC_MODE==0:
            rect_apple = (x_apple, y_apple, TOOLS.BLOCK_SIZE, TOOLS.BLOCK_SIZE)
            pygame.draw.rect(screen_of_game, TOOLS.APPLE_COLOR, rect_apple, border_radius=TOOLS.APPLE_RADIUS)
        else:
            new_texture=pygame.transform.scale(TOOLS.APPLE_TEXTURE,(TOOLS.BLOCK_SIZE,TOOLS.BLOCK_SIZE))
            screen_of_game.blit(new_texture,(x_apple,y_apple))
### 2.3.4 Отрисовать Винограда 

def draw_grapes(screen_of_game, grapes):
    for grape in grapes:
        offset_x=-1
        if TOOLS.GRAPHIC_MODE==0:
            for i in range(1,TOOLS.BLOCK_SIZE-1):
                if i%2!=0:
                    offset_x+=1
                x_grape_start = grape[0] * TOOLS.BLOCK_SIZE +TOOLS.BORDERS_SIZE + offset_x
                y_grape_start = grape[1] * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + i
                x_grape_end = grape[0] * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + TOOLS.BLOCK_SIZE - 1 - offset_x
                y_grape_end = grape[1] * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE + i
                pygame.draw.line(screen_of_game, TOOLS.GRAPE_COLOR, (x_grape_start, y_grape_start),(x_grape_end, y_grape_end))
        else:
            x_grape=grape[0] * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE
            y_grape=grape[1] * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE
            new_texture=pygame.transform.scale(TOOLS.GRAPE_TEXTURE,(TOOLS.BLOCK_SIZE,TOOLS.BLOCK_SIZE))
            screen_of_game.blit(new_texture,(x_grape,y_grape))
### 2.3.4 Отрисовать Апельсин 
def draw_oranges(screen_of_game, apples):
    for apple in apples:
        x_apple = apple[0] * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE
        y_apple = apple[1] * TOOLS.BLOCK_SIZE + TOOLS.BORDERS_SIZE
        if TOOLS.GRAPHIC_MODE==0:
            rect_apple = (x_apple, y_apple, TOOLS.BLOCK_SIZE, TOOLS.BLOCK_SIZE)
            pygame.draw.rect(screen_of_game, TOOLS.APPLE_COLOR, rect_apple, border_radius=TOOLS.APPLE_RADIUS)
        else:
            new_texture=pygame.transform.scale(TOOLS.ORANGE_TEXTURE,(TOOLS.BLOCK_SIZE,TOOLS.BLOCK_SIZE))
            screen_of_game.blit(new_texture,(x_apple,y_apple))    

### 2.3.6 Отрисовать счет и скорость
def draw_score(screen_of_game, score, speed):
    #счет
    score_text = TOOLS.TEXT_FONT.render(f"Score: {score}", True, TOOLS.TEXT_FONT_COLOR)
    score_text_rect = score_text.get_rect()
    score_text_rect.topleft = (TOOLS.BORDERS_SIZE, TOOLS.BLOCK_SIZE)
    screen_of_game.blit(score_text, score_text_rect)

    #скорость
    speed_text = TOOLS.TEXT_FONT.render(f"Speed: {speed}", True, TOOLS.TEXT_FONT_COLOR)
    speed_text_rect = speed_text.get_rect()
    speed_text_rect.topright = (TOOLS.WIDTH_OF_WINDOW -TOOLS.BORDERS_SIZE, TOOLS.BLOCK_SIZE)
    screen_of_game.blit(speed_text, speed_text_rect)

### 2.3.7 Отрисовать Выигрыш
def draw_game_won_screen(screen_of_game):
    screen_of_game.fill(TOOLS.WALLS_COLOR)
    text = TOOLS.TEXT_FONT_74.render("Победа!", True, (220, 220, 220))
    text_rect = text.get_rect(center=(TOOLS.SIZE_OF_WINDOW[0] // 2, TOOLS.SIZE_OF_WINDOW[1] // 3))
    screen_of_game.blit(text, text_rect)

### 2.3.8 Отрисовать Поражение
def draw_game_over_screen(screen_of_game):

    draw_background(screen_of_game)
    text = TOOLS.TEXT_FONT_74.render("Проигрыш", True, (220, 220, 220))
    text_rect = text.get_rect(center=(TOOLS.SIZE_OF_WINDOW[0] // 2, TOOLS.SIZE_OF_WINDOW[1] // 3))
    screen_of_game.blit(text, text_rect)

    text = TOOLS.TEXT_FONT_33.render("Нажмите Enter чтобы начать с начала", True, (255, 255, 255))
    text_rect = text.get_rect(center=(TOOLS.SIZE_OF_WINDOW[0] // 2, TOOLS.SIZE_OF_WINDOW[1] // 2))
    screen_of_game.blit(text, text_rect)