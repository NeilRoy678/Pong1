import pygame
import sys
import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostname()
port = 5555
client.connect((ip,port))
# initialize pygame
pygame.init()
clock = pygame.time.Clock()
# making the screen
screen_width = 1530
screen_height = 810
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("P0NG")
# shapes that are empty rectangles without pygame.draw
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)
bg_color = (0, 0, 0)
white = (255, 255, 255)
   
def player_animation():
	player.y += player_speed
	if player.top<= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def opponent_animation(n,e):
	opponent.y += opponent_speed
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height
	opponent.move_ip(n,e)
# the base speed of the ball
ball_speed_x = 6
ball_speed_y = 6
# players
player_speed = 0
opponent_speed = 0
# game loop
while True:
	# input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				player_speed += 7
			if event.key == pygame.K_UP:
				player_speed -= 7
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				player_speed -= 7
			if event.key == pygame.K_UP:
				player_speed += 7
		# player 2
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				opponent_speed += 7
			if event.key == pygame.K_w:
				opponent_speed -= 7
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_s:
				opponent_speed -= 7
			if event.key == pygame.K_w:
				opponent_speed += 7
	player_animation()
	client.sendall(str.encode("\n".join([str(player.top),str(player.bottom)])))
	n, e = [int(i) for i in client.recv(2048).decode("utf-8").split('\n')]
	print(n,e)
	#opponent_animation(n,e)


	# objects
	screen.fill(bg_color)
	pygame.draw.rect(screen, white, player)
	pygame.draw.rect(screen, white, opponent)
 
	# updates the game window
	pygame.display.flip()
	clock.tick(65)