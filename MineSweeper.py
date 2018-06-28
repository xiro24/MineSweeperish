import os
import random

class MineSweeper:
	height = 9;
	width = 9;
	coordsX=[];
	coordsY=[];
	point=[0,0];
	pointX=[0];
	pointY=[0];
	discovered =[];
	
	def cls(self):
		os.system('cls')
		
	def bombs(self,coordsX,coordsY,height,width):
		count =0;
		
		while count < height and count < width:
			count = (random.randint(1,width)%(width*height));
		print(count);
		
		for num in range(count):
			positionX = random.randint(1,width);
			positionY = random.randint(1,height);
			coordsX.insert(len(coordsX),positionX);
			coordsY.insert(len(coordsY),positionY);
		print(str(coordsX),"",str(coordsY));
		##fix duplicates
	
	def gameboard(self,coordsX,coordsY,height,width):
		x = coordsX;
		y = coordsY;
		
		for i in range(height+1):
			print('----'*(width+1));
			if i != 0:
				print(i,end='   ');
			if i ==0:
				print(i,end='   ');
			for j in range(width):	
				if i == 0:
					print("|",j+1,"",end='');
				else:
					print('|',end='');
					checker = False;
					for a in range(len(coordsX)):
						if i==x[a] and j==y[a]:
							print(' B ',end='');
							checker = True;
							break;
							
							##need an array for this
					for a in range(len(self.pointX)):
						if i == self.pointX[a] and j == self.pointY[a]:
							print(' V ',end='');
							checker = True;
							break;
						
					if checker==False:
						print('   ',end='');  
			print('|');

	def turn(self):
		print('insert coordinates. (IE. 2,2)');
		user = input('>');
		self.cls();
		
		#get the coords then plot the section
		self.point = user.split(',');
		self.pointX.insert(len(self.pointX),int(self.point[0]));
		self.pointY.insert(len(self.pointY),int(self.point[1]));
		for i in range(len(self.pointX)):
			if self.pointX[i]>0 and self.pointY[i] <self.width+1:
				self.gameboard(self.coordsX,self.coordsY,self.height,self.width);
				break;
m = MineSweeper();
m.bombs(m.coordsX,m.coordsY,m.height,m.width);
m.gameboard(m.coordsX,m.coordsY,m.height,m.width);
while True:
	m.turn();
	
	
	
	
##current issues:
	##grid scaling/coords is incorrect
	