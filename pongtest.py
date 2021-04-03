# pong game 0.3
import pygame
import sys
import threading
import socket
from networking import Network

class Player():
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.screen_width = 1530
		self.screen_height = 810
		#self.rect = pygame.Rect(self.x,self.y,self.height,self.width)
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
		pygame.display.set_caption("P0NG")
		#self.ball = pygame.Rect(self.screen_width/2 - 15, self.screen_height/2 - 15, 30, 30)
		self.player1 = pygame.Rect(self.width, self.height, 10, 140)
		self.bg_color = (0, 0, 0)
		self.white = (255, 255, 255)
		self.ball_speed_x = 6
		self.ball_speed_y = 6
		self.player_speed = 0
		
	def player_animation(self,player_speed):
		self.player1.y += player_speed
		if self.player1.top <= 0:
			self.player1.top = 0
		if self.player1.bottom >= self.screen_height:
			self.player1.bottom = self.screen_height
		return(self.player1.top,self.player1.bottom)
	
	def draw1(self):
		self.screen.fill(self.bg_color)
		#self.opponent.screen.fill(self.player.bg_color)
		pygame.draw.rect(self.screen, self.white,self.player1)


class pong:
	def __init__(self):
		pygame.init()
		
		self.y = 0
		self.top = 0
		self.bottom = 0

		#return (self.player.top,self.player.bottom)
		self.opponent_speed = 0
		self.player_speed = 0
		self.opp()
	def opp(self):
		clock = pygame.time.Clock()
		self.net = Network()
		x,y = self.read_pos(self.net.getPos())
		self.player = Player(335,475,1510,335)
		self.opponent = Player(335,480,10,335)
		while True:
			clock.tick(65)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit() 	
					sys.exit()	
				if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_DOWN:
								self.player_speed += 7
						if event.key == pygame.K_UP:
								self.player_speed -= 7
				if event.type == pygame.KEYUP:
						if event.key == pygame.K_DOWN:
							self.player_speed -= 7
						if event.key == pygame.K_UP:
							self.player_speed += 7  
			self.x,self.y = self.player.player_animation(self.player_speed)
			n,e = self.read_pos(self.net.send(self.make_pos(self.x,self.y)))
			print(n,e)
			self.opponent.top = n
			self.opponent.bottom = e

			#self.x,self.y = self.player.player_animation(self.player_speed,self.y,self.top,self.bottom)
			self.player.screen.fill(self.player.bg_color)
			self.opponent.screen.fill(self.player.bg_color)
			self.player.draw1()
			self.opponent.draw1()
		#	self.opponent.top, self.opponent.bottom = self.read_pos(self.make_pos(n,e))
			
			#self.opponent = Player(n,e)
			#client.sendall(str.encode("\n".join([str(player.top), str(player.bottom)])))
			#n, e = [int(i) for i in client.recv(2048).decode('utf-8').split('\n')]
			pygame.display.flip()
	

	
	def make_pos(self,x,y):
		#data = str(self.net.pos) + ":" + str(x) + "," + str(y)
		reply = str.encode(",".join([str(self.x),str(self.y)]))
		return reply

	def read_pos(self,data):
		n,e = data.split(",")
		return n,e
		
	#updates the game window
			
if __name__ == '__main__':
	pong()
