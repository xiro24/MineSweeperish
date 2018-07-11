import os
import random
import numpy as np

class MineSweeper:
	height = 9;
	width = 9;
	coordsX=[];
	coordsY=[];
	point=[-1,-1];
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
			positionX = random.randint(0,width-1);
			positionY = random.randint(0,height-1);
			for i in range(len(coordsX)):
				while coordsX[i] == positionX and coordsY[i] == positionY:
					positionX = random.randint(0,width-1);
					positionY = random.randint(0,height-1);
			coordsX.insert(len(coordsX),positionX);
			coordsY.insert(len(coordsY),positionY);
		self.graph[coordsX,coordsY] = 9; 

	#represents the entirety of the game to the player
	def gameboard(self,coordsX,coordsY,height,width):
		x = coordsX;
		y = coordsY;
		if int(self.point[0]) >=0 and int(self.point[1]) >=0:
			row = int(self.point[0]);
			column = int(self.point[1]);
					#right
			for i in range(height-column):
				bomb =0;
				if row+1 <9:
					#bottom right
					if column+i+1<9 and column+i-1>=0:
						if self.graph[row+1,column+i+1] == 9 and self.graph[row,column+i]!= 9:
							bomb+=1;
					#bottom left
					if column+i-1>=0:
						if self.graph[row+1,column+i-1] == 9 and self.graph[row,column+i] != 9:
							bomb+=1;
					#down
					if self.graph[row+1,column+i] == 9 and self.graph[row,column+i] != 9:
						bomb+=1;
				if row-1 >=0:
					#top right
					if column+i+1<9 and column+i+1>=0:
						if self.graph[row-1,column+i+1] == 9 and self.graph[row,column+i] != 9:
							bomb+=1;
					#top
					if column+i<9:
						if self.graph[row-1,column+i] == 9 and self.graph[row,column+i] != 9:
							bomb+=1;
					#top left
					if column+i-1>=0:
						if self.graph[row-1,column+i-1] == 9 and self.graph[row,column+i] != 9:
							bomb+=1;
				#right
				if self.graph[row,column+i] == 9 and self.graph[row,column+i] != 9:
					bomb+=1;
				#left
				if column-i >= 0:
					if self.graph[row,column+i-1] == 9 and self.graph[row,column+i] != 9:
						bomb+=1;
				if bomb !=0:
					self.graph[row,column+i] = bomb;
				elif self.graph[row,column+i] == 0:
					self.graph[row,column+i] = 11;
				if self.graph[row,column+i] == 9:
					break;

		#left	
			for i in range(column+1):
				bomb =0;
				if row+1 <9:
					#bottom right
					if column-i+1<9:
					##can't seem to get the alst coords :/
					##i see what's wrong now there's a value already there which is not 9 or 0
						if self.graph[row+1,column-i+1] == 9 and self.graph[row,column-i] != 9:
							bomb+=1;
					#bottom left
					if column-i-1>=0:
						if self.graph[row+1,column-i-1] == 9 and self.graph[row,column-i] != 9:
							bomb+=1;
					#down
					if column-i>=0:
						if self.graph[row+1,column-i] == 9 and self.graph[row,column-i] != 9:
							bomb+=1;
				if row-1 >=0:
					#top right
					if column-i+1<9:
						if self.graph[row-1,column-i+1] == 9 and self.graph[row,column-i] != 9:
							bomb+=1;
					#top
					if column-i>=0:
						if self.graph[row-1,column-i] == 9 and self.graph[row,column-i] != 9:
							bomb+=1;
					#top left
					if column-i-1>=0:
						if self.graph[row-1,column-i-1] == 9 and self.graph[row,column-i] != 9:
							bomb+=1;
				#right
				##sill a bit weird
				if column-i+1<9:
					if self.graph[row,column-i+1] == 9 and self.graph[row,column-i] != 9:
						bomb+=1;
				#left
				if column-i-1 >= 0:
					if self.graph[row,column-i-1] == 9 and self.graph[row,column-i] != 9:
						bomb+=1;
				if bomb !=0:
					self.graph[row,column-i] = bomb;
				elif self.graph[row,column-i] == 0:
					self.graph[row,column-i] = 11;
				if self.graph[row,column-i] == 9:
					break;
		#up
			for i in range(row+1):
				bomb =0;
				if row-i+1<9:
					#bottom right
					if column+1<9:
						if self.graph[row-i+1,column+1] == 9 and self.graph[row-i,column] != 9:
							bomb+=1;
					#bottom left
					if column-1>=0:
						if self.graph[row-i+1,column-1] == 9 and self.graph[row-i,column] != 9:
							bomb+=1;
					#down
					if row-i+1<9:
						if self.graph[row-i+1,column] == 9 and self.graph[row-i,column] != 9:
							bomb+=1;
				if row-i-1>=0:
				#top right
					if column+1<9:
						if self.graph[row-i-1,column+1] == 9 and self.graph[row-i,column] != 9:
							bomb+=1;
					#top
					if self.graph[row-i-1,column] == 9 and self.graph[row-i,column] != 9:
						bomb+=1;
					#top left
					if column-1>=0:
						if self.graph[row-i-1,column-1] == 9 and self.graph[row-i,column] != 9:
							bomb+=1;
				#right
				if column+1<9:
					if self.graph[row-i,column+1] == 9 and self.graph[row-i,column] != 9:
						bomb+=1;
				#lefts
				if column-1>= 0:
					if self.graph[row-i,column-1] == 9 and self.graph[row-i,column] != 9:
						bomb+=1;
				if bomb !=0:
					self.graph[row-i,column] = bomb;
				elif self.graph[row-i,column] == 0:
					self.graph[row-i,column] = 11;
				if self.graph[row-i,column] == 9:
					break;
		#down
			for i in range(height-row):
				bomb =0;
				if row+i+1<9:
					#bottom right
					if column+1<9:
						if self.graph[row+i+1,column+1] == 9 and self.graph[row+i,column] != 9:
							bomb+=1;
					#bottom left
					if column-1>=0:
						if self.graph[row+i+1,column-1] == 9 and self.graph[row+i,column] != 9:
							bomb+=1;
					#down
					if row+i+1<9:
						if self.graph[row+i+1,column] == 9 and self.graph[row+i,column] != 9:
							bomb+=1;
				if row+i-1>=0:
				#top right
					if column+1<9:
						if self.graph[row+i-1,column+1] == 9 and self.graph[row+i,column] != 9:
							bomb+=1;
					#top
					if self.graph[row+i-1,column] == 9 and self.graph[row+i,column] != 9:
						bomb+=1;
					#top left
					if column-1>=0:
						if self.graph[row+i-1,column-1] == 9 and self.graph[row+i,column] != 9:
							bomb+=1;
				#right
				if column+1<9:
					if self.graph[row+i,column+1] == 9 and self.graph[row+i,column] != 9:
						bomb+=1;
				#left
				if column-1>= 0:
					if self.graph[row+i,column-1] == 9 and self.graph[row+i,column] != 9:
						bomb+=1;
				if bomb !=0:
					self.graph[row+i,column] = bomb;
				elif self.graph[row+i,column] == 0:
					self.graph[row+i,column] = 11;
				if self.graph[row+i,column] == 9:
					break;
								
			#self
			if self.graph[row,column] !=9:
				bomb=0;
				if row+1<9:
					#bottom right
					if column+1<9:
						if self.graph[row+1,column+1] == 9:
							bomb+=1;
					#bottom left
					if column-1>=0:
						if self.graph[row+1,column-1] == 9:
							bomb+=1;
					#down
					if self.graph[row+1,column] == 9:
						bomb+=1;
				if row-1>=0:
					#top right
					if column+1<9:
						if self.graph[row-1,column+1] == 9:
							bomb+=1;
					#top
					if self.graph[row-1,column] == 9:
						bomb+=1;
					#top left
					if column-1 >=0:
						if self.graph[row-1,column-1] == 9:
							bomb+=1;
				#right
				if column+1<9:
					if self.graph[row,column+1] == 9:
						bomb+=1;
				#left
				if column-1>=0:
					if self.graph[row,column-1] == 9:
						bomb+=1;
				print('start',bomb);
				if bomb !=0:
					self.graph[row,column] = bomb;	
				elif self.graph[row,column] == 0:
					self.graph[row,column] = 10;
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
				elif self.graph[row,column] == 9:
					print('   ',end='');
				elif self.graph[row,column] == 10:
					print(' X ',end='');
				elif self.graph[row,column] == 11:
					print(' N ',end='');
				elif self.graph[row,column] == 1:
					print(' 1 ',end='');
				elif self.graph[row,column] == 2:
					print(' 2 ',end='');
				elif self.graph[row,column] == 3:
					print(' 3 ',end='');
				elif self.graph[row,column] == 4:
					print(' 4 ',end='');
				elif self.graph[row,column] == 5:
					print(' 5 ',end='');
				elif self.graph[row,column] == 6:
					print(' 6 ',end='');
				elif self.graph[row,column] == 7:
					print(' 7 ',end='');
				elif self.graph[row,column] == 8:
					print(' 8 ',end='');
				#replace this with the number of bombs surrounding it
			print('|');
	def drawBoardFinsih(self,height,width):
	
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
				elif self.graph[row,column] == 9:
					print(' B ',end='');
				elif self.graph[row,column] == 10:
					print(' X ',end='');
				elif self.graph[row,column] == 11:
					print(' N ',end='');
				elif self.graph[row,column] == 1:
					print(' 1 ',end='');
				elif self.graph[row,column] == 2:
					print(' 2 ',end='');
				elif self.graph[row,column] == 3:
					print(' 3 ',end='');
				elif self.graph[row,column] == 4:
					print(' 4 ',end='');
				elif self.graph[row,column] == 5:
					print(' 5 ',end='');
				elif self.graph[row,column] == 6:
					print(' 6 ',end='');
				elif self.graph[row,column] == 7:
					print(' 7 ',end='');
				elif self.graph[row,column] == 8:
					print(' 8 ',end='');
				#replace this with the number of bombs surrounding it
			print('|');
		
	#gets player's input
	def turn(self):
		print('insert coordinates. (IE. row,column)');
		user = input('>');
		##self.cls();
		
		#get the coords then plot the section
		self.point = user.split(',');
		if int(self.point[0])>=0 and int(self.point[1])<self.width+1:
			self.gameboard(self.coordsX,self.coordsY,self.height,self.width);
				
m = MineSweeper();
m.bombs(m.coordsX,m.coordsY,m.height,m.width);
m.gameboard(m.coordsX,m.coordsY,m.height,m.width);
while True:
	m.turn();
	if m.graph[int(m.point[0]),int(m.point[1])] == 9:
		m.drawBoardFinsih(m.height,m.width);
		print('you hit a bomb ur dead');
		print('GAME OVER');
		break;
## needs a way to finish the game
