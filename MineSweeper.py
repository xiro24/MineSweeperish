import os
import random
import numpy as np

class MineSweeper:
	height = 9;
	width = 9;
	coordsX=[];
	coordsY=[];
	point=[0,0];
	discovered =[];
	graph = np.zeros((width,height));
	
	#clears the screen
	def cls(self):
		os.system('cls')
	
	#initializes the bombs position and amount of bombs for the game
	def bombs(self,coordsX,coordsY,height,width):
		count =0;
		while count < height and count < width:
			count = (random.randint(1,width*height));
		#print(count);
		for num in range(count):
			positionX = random.randint(1,width-1);
			positionY = random.randint(1,height-1);
			for i in range(len(coordsX)):
				while coordsX[i] == positionX and coordsY[i] == positionY:
					positionX = random.randint(1,width-1);
					positionY = random.randint(1,height-1);
			coordsX.insert(len(coordsX),positionX);
			coordsY.insert(len(coordsY),positionY);
		self.graph[coordsX,coordsY] = 1; 

	#represents the entirety of the game to the player
	def gameboard(self,coordsX,coordsY,height,width):
		x = coordsX;
		y = coordsY;
		if int(self.point[0]) >=0 and int(self.point[1]) >=0:
			self.graph[int(self.point[0]),int(self.point[1])] = 2;
			for row in range(width):
				for column in range(height):
					if int(self.point[0]) == row and int(self.point[1]) == column:
					#right
						for i in range(height-column):
							if self.graph[row,column+i] == 1 and self.graph[row,column+i-1] == 0:
								self.graph[row,column+i-1] = 3;
							if self.graph[row,column+i] == 1:
								break;
					#left	
						for i in range(column):
							if self.graph[row,column-i] == 1 and self.graph[row,column-i+1] == 0:
								self.graph[row,column-i+1] = 3;
							if self.graph[row,column-i] == 1:
								break;
					#up
						for i in range(width-row):
							if self.graph[row+i,column] == 1 and self.graph[row+i-1,column] == 0:
								self.graph[row+i-1,column] = 3;
							if self.graph[row+i,column] == 1:
								break;
					#down
						for i in range(row):
							if self.graph[row-i,column] == 1 and self.graph[row-i+1,column] == 0:
								self.graph[row-i+1,column] = 3;
							if self.graph[row-i,column] == 1:
								break;
						break;		
		print(self.graph);
		
		#draws the board from the graph
		print(" "*4,end='');
		for i in range(width):
			print("|",i,"",end='');
		print('|');
		for row in range(width):
			print('----'*(width+1));
			if row != 0:
				print(row,end='   ');
			if row ==0:
				print(row,end='   ');
			for column in range(height):
				print('|',end='');
				if self.graph[row,column] == 0:
					print('   ',end='');
				elif self.graph[row,column] == 1:
					print(' B ',end='');
				elif self.graph[row,column] == 2:
					print(' V ',end='');
				elif self.graph[row,column] == 3:
					print(' N ',end='');
				#replace this with the number of bombs surrounding it
			print('|');
		
	#gets player's input
	def turn(self):
		print('insert coordinates. (IE. row,column)');
		user = input('>');
		self.cls();
		
		#get the coords then plot the section
		self.point = user.split(',');
		if int(self.point[0])>=0 and int(self.point[1])<self.width+1:
			self.gameboard(self.coordsX,self.coordsY,self.height,self.width);
				
m = MineSweeper();
m.bombs(m.coordsX,m.coordsY,m.height,m.width);
m.gameboard(m.coordsX,m.coordsY,m.height,m.width);
while True:
	m.turn();
	
	
