import pygame
import time
import random

pygame.init()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Game field dimensions
width = 600
height = 400

# Snake size
snake_size = 10

# Create window
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 25)


def message_to_screen(msg, color, y_displace=0, size="normal"):
    if size == "normal":
        screen_text = font.render(msg, True, color)
    else:
        screen_text = small_font.render(msg, True, color)
    game_window.blit(screen_text,
                     [width / 2 - screen_text.get_width() / 2, height / 2 - screen_text.get_height() / 2 + y_displace])


# Game loop
def game_loop():
    game_over = False
    game_exit = False

    x = width / 2
    y = height / 2
    x_change = snake_size
    y_change = 0
    snake_list = []
    snake_length = 3

    # Food position
    foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_exit == True:
            game_window.fill(black)
            message_to_screen("Game Over", red)
            message_to_screen("(press Spacebar to start new game)", white, 50, size="small")
            pygame.display.update()

            # Quit or restart
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = False
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_loop()
                    if event.key == pygame.K_q:
                        game_over = True
                        game_exit = False

        # Control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0

        # Boundary check
        if x >= width or x < 0 or y >= height or y < 0:
            game_exit = True

        x += x_change
        y += y_change

        game_window.fill(black)

        # Display food
        pygame.draw.rect(game_window, white, [foodx, foody, snake_size, snake_size])

        # Move snake
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Collision with self
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_exit = True

        # Draw snake
        for segment in snake_list:
            pygame.draw.rect(game_window, white, [segment[0], segment[1], snake_size, snake_size])

        pygame.display.update()

        # When the snake reaches the food
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        time.sleep(0.1)

    pygame.quit()


game_loop()