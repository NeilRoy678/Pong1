# pong game 0.3
import pygame
import sys
import threading
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clients = []
ip = socket.gethostname()
port = 55555
client.connect((ip,port))
pygame.init()
clock = pygame.time.Clock()
screen_width = 1530
screen_height = 810
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("P0NG")
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)
bg_color = (0, 0, 0)
white = (255, 255, 255)
ball_speed_x = 6
ball_speed_y = 6
player_speed = 0

def player_animation(player_speed):
	player.y += player_speed
	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height
def opponent_animation(opponent_speed,count):
	opponent.y += opponent_speed
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height
	opponent.move_ip(count,0)

def opp():
	opponent_speed = 0
	player_speed = 0
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
		player_animation(player_speed)
		client.send(str(player.top).encode('ascii'))


						
			# player 2
			
		count = client.recv(1024).decode('ascii')
		print(count)
		

		# objects
		screen.fill(bg_color)
		pygame.draw.rect(screen, white, player)
		pygame.draw.rect(screen, white, opponent)
	
		# updates the game window
		pygame.display.flip()
		clock.tick(65)
if __name__ == '__main__':
	opp()
