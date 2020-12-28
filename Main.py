# IMPORTING MODULES
import pygame
import random
import os

# INITILIZING PYGAME MODULE
pygame.init()

# COLOUR VARIABLE
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]
green = [45, 156, 45]

# CREATING WINDOW AND ITS SIZE
screen_width = 900
screen_hight = 600
game_window = pygame.display.set_mode((screen_width,screen_hight))

# GIVING TITLE FOR WINDOW
window_caption = pygame.display.set_caption("BASIC SNAKE GAME")
pygame.display.update()

# DEFINE CLOCK FUNCTION FORM PYGAME MODULE
clock = pygame.time.Clock()

# CREATING A FUNCTION FOR SNAKE, AND GIVING ITS COLOUR SIZE IN GAME WINDOW
def plot_snake(game_window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

# CREATING A FUNCTION FOR TEXT
def text_screen(text, color, x, y, text_size):
    font = pygame.font.SysFont(None, text_size)
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

# CREATING A FUNCTION FOR WELCOME WINDOW
def welcome():
    # WHEN GAME DOES NOT EXIT
    exit_game = False
    # CREATING WELCOME WINDOW, GIVING COLOUR,TEXTS TO WINDOW
    while not exit_game:
        game_window.fill(black)
        text_screen("WELCOME TO THE BASIC SNAKE GAME", white, 100, 245, 50)
        text_screen("PRESS ENTER TO START THE GAME", white, 225, 295, 35)
        text_screen("BY AKASH PATEL", white, 760, 580, 23)

        # FOR CONTROLING, KEY, QUIT AND ENTER
        for event in pygame.event.get():
            # FOR QUIT, WHEN USER CLICK ON X BUTTON ON WINDOW
            if event.type == pygame.QUIT:
                exit_game = True
            # ENTER KEY, WHEN USER PRESS ENTER TO PLAY THE GAME IN WELCOME WINDOW
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # CALLING GAME LOOP, WHEN USER PRESS ENTER AND GAME START
                    gameloop()

            # UPADTING WINDOW
            pygame.display.update()
            clock.tick(60)

# CREATING A FUNCTION FOR GAME LOOP (FOR PLAYING GAME)
def gameloop():

    # CREATING VARIABALE
    exit_game = False  # FOR EXITING GAME
    game_over = False  # FOE GAME OVER
    snake_x = 45  # FOR GAME HEIGHT
    snake_y = 55  # FOR GAME WEADTH
    velocity_x = 0  # FOR GAME VELOCITY
    velocity_y = 0  # FOR GAME VELOCITY
    init_velocity = 5  # FOR INITILAZING VELOCITY
    snake_size = 20  # FOR SNAKE HEAD SIZE
    fps = 60  # THIS IS FPS FOR REFRESING WINDOE
    food_x = random.randint(0, screen_width/1.5)  # FOR FOOD
    food_y = random.randint(0, screen_hight/1.5)  # FOR FOOD
    score = 0  # FOR SCORE
    snake_len = 1  # FOR SNAKE LENGTH
    snake_list = []  # FOR SNAKE LIST, (SNAKE BODY)

    # CREATING CONDITION, WHEN HIGH SCORE FILE EXITS OR NOT
    if (not  os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    # IF HIGH SCORE FILE EXIT WHEN THIS CODE RUN
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    # STARTING LOOP
    while not exit_game:
        # CONDITION, IF GAME OVER, WRITE PRESENT HIGHSCORE ON FILE
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            game_window.fill(black)
            # PRINTING GAME OVER IN GAME OVER WINDOW
            text_screen("GAME OVER !!", white, 310, 245, 50)
            text_screen("YOUR SCORE IS " + str(score), white, 320, 295, 35)
            text_screen("PRESS ENTER TO RESTART THE GAME", white, 200, 339, 35)

            # CREATING EVENT FORM PYGAME
            for event in pygame.event.get():
                # FOR QUITING GAME, KEY QUIT, WHEN USER PRESS ON X BUTTON FROM MOUSE, GAME EXIT
                if event.type == pygame.QUIT:
                    exit_game = True

                # FOR KEY, ENTER TO RESTART GAME
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            # CREATING EVENT FORM PYGAME
            for event in pygame.event.get():
                # FOR QUITING GAME, KEY QUIT, WHEN USER PRESS ON X BUTTON FROM MOUSE, GAME EXIT
                if event.type == pygame.QUIT:
                    exit_game = True

                # GIVING KEYS TO CONTROL SNAKE, LEFT,RIGHT,UP,DOWN
                # RIGHT KEY
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity = 5
                        velocity_y = 0

                # LEFT KEY
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                # UP KEY
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                # DOWN KEY
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            # GIVING VELOCITY
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            # GIVING FOOD IN DIFFRENT PLACE IN GAME WINDOW
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                # FOR SCORE
                score = score + 10
                # FOR FOOD
                food_x = random.randint(0, screen_width/1.5)
                food_y = random.randint(0, screen_hight/1.5)
                snake_len = snake_len + 5
                # FOR SCORE
                if score > int(highscore):
                    highscore = score

            # CONVERTING WINDOW IN WHITE COLOUR
            game_window.fill(black)
            # DISPLAY TEXT FUNCTION OF PRESENT SCORE AND HEIGH SCORE
            text_screen("Score - " + str(score) + "  Highscore - " + str(highscore), white, 320, 5, 30)
            # MAKING FOOD FOR SNAKE, COLOUR, SIDE, PLACE IN GAME WINDOW
            pygame.draw.rect(game_window, white, [food_x, food_y, snake_size, snake_size])
            # CREATING HEAD STORE
            head = []
            # APPENDING BODY IN FORM OF LINT IN SNAKE HEAD
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            # A LOOP FOR CUTTING HEAD
            if len(snake_list) > snake_len:
                del snake_list[0]

            # WHEN SNAKE TOUCH HIS OWN BODY,GAME OVER
            if head in snake_list[:-1]:
                game_over = True

            # GAME OVER CODITION, WHEN SNAKE TOUCH WINDOW BODER, GAME OVER
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_hight:
                game_over = True

            # CALLING FUNCTION, SNAKE
            plot_snake(game_window, green, snake_list, snake_size)
        # UPDATE CHANGES
        pygame.display.update()
        # FOR CLOCK FROM PYGAME, FRAME PER SECOND(FPS)
        clock.tick(fps)

    # CALLING INBULT FUNCTION ,FOR EXIT GAME
    pygame.quit()
    quit()

# CALLING WELCOME SCREEN
welcome()