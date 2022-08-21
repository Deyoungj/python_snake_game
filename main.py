import pygame
import random
import time


pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
yellow = (255, 255, 102)
bg_color = (255,255,255)
# font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

def snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(screen,blue, [x[0], x[1], snake_block,snake_block])

def message(msg,color):
	mesg = font_style.render(msg, True, color)
	screen.blit(mesg,[screen_width/3,screen_height/3])



def snake_game():
	running = True
	failed = False
	# initial position of the snake
	snake_pos_x = screen_width/2
	snake_pos_y = screen_width/2
	

	snake_block = 10
	# if snake position change 
	snake_pos_x_change = 0
	snake_pos_y_change = 0

	snake_list = []
	snake_length = 1

	# food position
	food_pos_x = round(random.randint(0, screen_width-snake_block)/10.0)*10.0
	food_pos_y = round(random.randint(0, screen_height-snake_block)/10.0)*10.0
	
	snake_speed = 15

	clock = pygame.time.Clock()
	while running:

		while failed:
			screen.fill(bg_color)
			message('you lost', red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					failed = False
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_k:
						snake_game()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					snake_pos_x_change = -snake_block
					snake_pos_y_change = 0

				if event.key == pygame.K_RIGHT:
					snake_pos_x_change = snake_block
					snake_pos_y_change = 0

				if event.key == pygame.K_UP:
					snake_pos_x_change = 0
					snake_pos_y_change = -snake_block

				if event.key == pygame.K_DOWN:
					snake_pos_x_change = 0
					snake_pos_y_change = snake_block

		snake_pos_x += snake_pos_x_change 
		snake_pos_y += snake_pos_y_change

		screen.fill(bg_color)
		pygame.draw.rect(screen,black,[food_pos_x, food_pos_y,snake_block,snake_block])

		snake_head = []
		snake_head.append(snake_pos_x)
		snake_head.append(snake_pos_y)
		snake_list.append(snake_head)

		if len(snake_list) > snake_length:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x == snake_head:
				failed = True

		snake(snake_block, snake_list)
		Your_score(snake_length - 1)
	
		pygame.display.update()

		if snake_pos_x > screen_width or snake_pos_x < 0 or snake_pos_y > screen_height or snake_pos_y < 0:
			failed = True

		if snake_pos_x == food_pos_x and snake_pos_y == food_pos_y:
			food_pos_x = round(random.randint(0, screen_width-snake_block)/10.0)*10.0
			food_pos_y = round(random.randint(0, screen_height-snake_block)/10.0)*10.0
			snake_length += 1

		clock.tick(snake_speed)

	pygame.quit()


snake_game()