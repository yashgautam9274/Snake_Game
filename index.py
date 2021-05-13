import pygame
import random
import os

pygame.mixer.init()
pygame.init()


# Colours
white = (255, 255, 255)
red = (255,0,0)
green = (0,128,0)
black = (0,0,0)
blue = (0,0,255)

# Creating Window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (screen_width,screen_height)).convert_alpha()

# Creating Title
pygame.display.set_caption("Snake with Yash")
pygame.display.update()



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text , color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x, y, snake_size,snake_size])
      
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(bg,(0,0))
        text_screen("Welcome to Snake World",black,120,270)
        text_screen("Press Spacebar to start",blue,130,320)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()    
        pygame.display.update()
        clock.tick(30)


# Game Loop
def gameloop():
    # Game Specific Variable
    with open("highscore.txt","r") as f:
        hiscore = f.read()
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 60
    init_velocity = 6
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    food_x = random.randint(0,screen_width) 
    food_y = random.randint(0,screen_height)
    score = 0
    snake_size = 20
    fps = 30
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To continue",red,80,200)
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()    

        else:
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                    # snake_x = snake_x + 10;  
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                    # snake_x = snake_x - 10;  
                        velocity_x = -init_velocity  
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                    # snake_y = snake_y - 10
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                    # snake_y = snake_y + 10
                        velocity_y = init_velocity  
                        velocity_x = 0    
                    if event.key == pygame.K_y:
                        score += 20

            snake_x+=velocity_x
            snake_y+=velocity_y                     
                        
            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=10
                food_x = random.randint(0,screen_width) 
                food_y = random.randint(0,screen_height)
                snk_length +=5
            if score>int(hiscore):
                hiscore = score    
            gameWindow.fill(white)
            text_screen("Score: "+ str(score) + "  HighScore: "+ str(hiscore),blue,5,5)
            
            pygame.draw.rect(gameWindow,red,[food_x, food_y, snake_size,snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True 

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            #pygame.draw.rect(gameWindow,green,[snake_x, snake_y, snake_size,snake_size]) 
            plot_snake(gameWindow,green,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()
#gameloop()