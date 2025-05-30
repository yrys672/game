# import pygame
# import random

# Инициализация Pygam
# pygame.init()

# # Окно
# WIDTH, HEIGHT = 600, 400
# CELL_SIZE = 20
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Простая змейка")

# Цвета
# GREEN = (0, 200, 0)
# RED = (255, 0, 0)
# BG = (100, 200, 255)
# WHITE = (255, 255, 255)

# # Змейка
# snake = [(100, 100)] #[] бир квадраттан кошот бул set.py
# direction = (CELL_SIZE, 0) #direction --- направление

# # Еда
# def new_food():
#     x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
#     y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
#     return (x, y)
# food = new_food()

# # Счёт
# score = 1 #очко
# font = pygame.font.SysFont("Arial", 24)

# clock = pygame.time.Clock()
# run = True
# while run:
#     clock.tick(6)  # скорость змейки

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     # Управление
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
#         direction = (-CELL_SIZE, 0) # в лево
#     if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
#         direction = (CELL_SIZE, 0) # в право
#     if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
#         direction = (0, -CELL_SIZE) # вверх
#     if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
#         direction = (0, CELL_SIZE) # вниз

#     # Движение змейки
#     head = snake[0]
#     new_head = (head[0] + direction[0], head[1] + direction[1])
#     snake.insert(0, new_head)

#     # Проверка еды
#     if new_head == food:
#         score += 23
#         food = new_food()
#     else:
#         snake.pop()

#     # Столкновение
#     if (
#         new_head in snake[1:] or
#         new_head[0] < 0 or new_head[0] >= WIDTH or
#         new_head[1] < 0 or new_head[1] >= HEIGHT
#     ):
#         run = False

#     # Рисование
#     screen.fill(BG)
#     for part in snake:
#         pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))
#     pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

#     text = font.render(f"Очки: {score}", True, WHITE)
#     screen.blit(text, (10, 10))

#     pygame.display.update()

# pygame.quit()


import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простая змейка")
clock = pygame.time.Clock()


GREEN = (0, 200, 0)
RED = (255, 0, 0)
BG = (100, 200, 255)
WHITE = (255, 255, 255)
FOOD_COLORS = [(255, 0, 0), (255, 128, 0), (0, 255, 0), (0, 255, 255), (255, 0, 255)]

obstacles = [(200, 200), (220, 200), (240, 200)]

def new_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in obstacles:
            return (x, y)

def start_screen():
    waiting = True
    while waiting:
        screen.fill(BG)
        font = pygame.font.SysFont("Arial", 32)
        text_surface = font.render("Нажми любую клавишу, чтобы начать", True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def game_loop():
    snake = [(100, 100)]
    direction = (CELL_SIZE, 0)
    food = new_food()
    food_color = random.choice(FOOD_COLORS)
    score = 0
    speed = 10
    game_over_state = False

    while True:
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_over_state and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return  

        if not game_over_state:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
            if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)

            head = snake[0]
            new_head = (head[0] + direction[0], head[1] + direction[1])

            new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)

            snake.insert(0, new_head)

            if new_head == food:
                score += 1
                if score % 5 == 0:
                    speed += 2
                food = new_food()
                food_color = random.choice(FOOD_COLORS)
            else:
                snake.pop()

            if new_head in snake[1:] or new_head in obstacles:
                game_over_state = True

        screen.fill(BG)
        for part in snake:
            pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))

        for obs in obstacles:
            pygame.draw.rect(screen, (50, 50, 50), (obs[0], obs[1], CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, food_color, (food[0], food[1], CELL_SIZE, CELL_SIZE))

        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Очки: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        if game_over_state:
            font_big = pygame.font.SysFont("Arial", 28)
            end_text = font_big.render("Игра окончена. Нажми R для перезапуска", True, WHITE)
            text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(end_text, text_rect)

        pygame.display.flip()


start_screen()
game_loop()
pygame.quit()   