import pygame
import os
import random
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)

# Display Variables
screen_width = 1550 # Must be Divisible by block_width_pixels
screen_height = screen_width - 600 # Must be Divisible by block_height_pixels
background_width = screen_width-100
background_height = screen_height-100
block_width_pixels = 25
block_height_pixels = 25
blocks_w = background_width // block_width_pixels
blocks_h = background_height // block_height_pixels
# Colors
border_color = (0, 0, 153)
background_color = (204, 0, 0)
snake_color = (255, 255, 0)
food_color = (0, 102, 0)

filler_char = "-"
boundary = "0"
snake_char = "S"
food = "F"

# X, Y
# 0 = North; 1 = East; 2 = South; 3 = West
class Snake():
    def __init__(self):
        self.direction = 5
        self.positions = []
        self.food_pos = [[0, 0]]
        self.growing = 0

score = 0

snake = Snake()
run = True
def quit_game():
    global run
    run = False

food_pos = []
def get_food_pos():
    global food_pos
    randx = random.randint(0, blocks_w-1)
    randy = random.randint(0, blocks_h-1)
    food_pos = [randx, randy]
    place_food()


def place_food():
    global food_pos
    c = 0
    for i in range(len(snake.positions)):
        if snake.positions[i] == food_pos:
            pass
        else:
            c+=1
    if len(snake.positions) == c: # Confirmed that the random location will not be inside of the snake
        randy = food_pos[1]
        randx = food_pos[0]
        grid[randy].pop(randx)
        grid[randy].insert(randx, food)
        snake.food_pos.pop(0)
        snake.food_pos.append([randx, randy])
    else:
        get_food_pos()


# 0 = North; 1 = East; 2 = South; 3 = West
def move_snake():
    global score
    pos_x = snake.positions[0][0]
    pos_y = snake.positions[0][1]
    tail_pos_x = snake.positions[-1][0]
    tail_pos_y = snake.positions[-1][1]

    if snake.direction == 0:
        if pos_y - 1 >= 0 and grid[pos_y-1][pos_x] != snake_char:
            if len(snake.positions) > 1:
                grid[pos_y-1].pop(pos_x)
                grid[pos_y-1].insert(pos_x, snake_char)
                snake.positions.insert(0, [pos_x, pos_y - 1])
                if snake.growing == 0:
                    grid[tail_pos_y].pop(tail_pos_x)
                    grid[tail_pos_y].insert(tail_pos_x, filler_char)
                    snake.positions.pop(-1)
                else:
                    snake.growing -= 1
            elif len(snake.positions) == 1:
                grid[pos_y-1].pop(pos_x)
                grid[pos_y-1].insert(pos_x, snake_char)
                if snake.growing > 0:
                    snake.positions.insert(0, [pos_x, pos_y-1])
                    snake.growing -= 1
                else:
                    grid[pos_y].pop(pos_x)
                    grid[pos_y].insert(pos_x, filler_char)
                    snake.positions[0][1] = pos_y - 1
        else:
            quit_game()

    elif snake.direction == 1:
        if pos_x + 1 < blocks_w and grid[pos_y][pos_x + 1] != snake_char:
            if len(snake.positions) > 1:
                grid[pos_y].pop(pos_x + 1)
                grid[pos_y].insert(pos_x + 1, snake_char)
                snake.positions.insert(0, [pos_x + 1, pos_y])
                if snake.growing == 0:
                    grid[tail_pos_y].pop(tail_pos_x)
                    grid[tail_pos_y].insert(tail_pos_x, filler_char)
                    snake.positions.pop(-1)
                else:
                    snake.growing -= 1
            elif len(snake.positions) == 1:
                grid[pos_y].pop(pos_x + 1 )
                grid[pos_y].insert(pos_x + 1, snake_char)
                if snake.growing > 0:
                    snake.positions.insert(0, [pos_x + 1, pos_y])
                    snake.growing -= 1
                else:
                    grid[pos_y].pop(pos_x)
                    grid[pos_y].insert(pos_x, filler_char)
                    snake.positions[0][0] = pos_x + 1
        else:
            quit_game()

    elif snake.direction == 2:
        if pos_y + 1 < blocks_h and grid[pos_y + 1][pos_x] != snake_char:
            if len(snake.positions) > 1:
                grid[pos_y + 1].pop(pos_x)
                grid[pos_y + 1].insert(pos_x, snake_char)
                snake.positions.insert(0, [pos_x, pos_y + 1])
                if snake.growing == 0:
                    grid[tail_pos_y].pop(tail_pos_x)
                    grid[tail_pos_y].insert(tail_pos_x, filler_char)
                    snake.positions.pop(-1)
                else:
                    snake.growing -= 1
            elif len(snake.positions) == 1:
                grid[pos_y + 1].pop(pos_x)
                grid[pos_y + 1].insert(pos_x, snake_char)
                if snake.growing > 0:
                    snake.positions.insert(0, [pos_x, pos_y + 1])
                    snake.growing -= 1
                else:
                    grid[pos_y].pop(pos_x)
                    grid[pos_y].insert(pos_x, filler_char)
                    snake.positions[0][1] = pos_y + 1
        else:
            quit_game()

    elif snake.direction == 3:
        if pos_x - 1 >= 0 and grid[pos_y][pos_x - 1] != snake_char:
            if len(snake.positions) > 1:
                grid[pos_y].pop(pos_x - 1)
                grid[pos_y].insert(pos_x - 1, snake_char)
                snake.positions.insert(0, [pos_x - 1, pos_y])
                if snake.growing == 0:
                    grid[tail_pos_y].pop(tail_pos_x)
                    grid[tail_pos_y].insert(tail_pos_x, filler_char)
                    snake.positions.pop(-1)
                else:
                    snake.growing -= 1
            elif len(snake.positions) == 1:
                grid[pos_y].pop(pos_x - 1 )
                grid[pos_y].insert(pos_x - 1, snake_char)
                if snake.growing > 0:
                    snake.positions.insert(0, [pos_x - 1, pos_y])
                    snake.growing -= 1
                else:
                    grid[pos_y].pop(pos_x)
                    grid[pos_y].insert(pos_x, filler_char)
                    snake.positions[0][0] = pos_x - 1
        else:
            quit_game()



    # Replace Food
    if snake.positions[0] == snake.food_pos[0]:
        score += 5
        snake.growing += 5
        place_food()


def create_snake():
    center_w = blocks_w//2
    center_h = blocks_h//2
    snake.positions.append([center_w, center_h])
    grid[center_h].pop(center_w)
    grid[center_h].insert(center_w, snake_char)


def create_grid():
    grid = [[filler_char for _ in range(blocks_w)] for _ in range(blocks_h)]
    return grid


pygame.init()
pygame.display.set_caption("Python Snake")
screen = pygame.display.set_mode((screen_width, screen_height), 0, 0)
def print_grid():
    screen.fill(border_color)
    pygame.draw.rect(screen, background_color, (screen_width//2 - background_width//2, screen_height//2 - background_height//2, background_width, background_height))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == snake_char:
                pygame.draw.rect(screen, snake_color, (
                screen_width//2 - background_width//2 + j * block_width_pixels,
                screen_height//2 - background_height//2 + i * block_height_pixels,
                block_width_pixels, block_height_pixels))
                pygame.draw.rect(screen, background_color, (
                screen_width//2 - background_width//2 + j * block_width_pixels,
                screen_height//2 - background_height//2 + i * block_height_pixels,
                block_width_pixels, block_height_pixels), 2)
            if grid[i][j] == food:
                pygame.draw.rect(screen, food_color, (
                screen_width // 2 - background_width // 2 + j * block_width_pixels,
                screen_height // 2 - background_height // 2 + i * block_height_pixels,
                block_width_pixels, block_height_pixels))
                pygame.draw.rect(screen, background_color, (
                screen_width // 2 - background_width // 2 + j * block_width_pixels,
                screen_height // 2 - background_height // 2 + i * block_height_pixels,
                block_width_pixels, block_height_pixels), 2)
    pygame.display.update()

# Game loop
grid = create_grid()
r = 0
while run:
    if r == 0:
        create_snake()
        get_food_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = 0
            elif event.key == pygame.K_RIGHT:
                snake.direction = 1
            elif event.key == pygame.K_DOWN:
                snake.direction = 2
            elif event.key == pygame.K_LEFT:
                snake.direction = 3
    move_snake()
    print_grid()
    time.sleep(.075)
    r += 1



pygame.quit()