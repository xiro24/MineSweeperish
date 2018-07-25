import os
import random

from Draw import drawBoardFinish


class MineSweeper:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.graph = [[0 for x in range(width)] for y in range(height)]

    coordsX = []
    coordsY = []
    point = [-1, -1]
    discovered = []

    # clears the screen
    def cls(self):
        os.system('cls')

    # initializes the bombs position and amount of bombs for the game
    def bombs(self, coordsX, coordsY, height, width):
        count = 0
        while count < height and count < width:
            count = (random.randint(1, width * height))
        # print(count)
        for num in range(count):
            positionX = random.randint(0, width - 1)
            positionY = random.randint(0, height - 1)
            for i in range(len(coordsX)):
                while coordsX[i] == positionX and coordsY[i] == positionY:
                    positionX = random.randint(0, width - 1)
                    positionY = random.randint(0, height - 1)

                    self.graph[positionY][positionX] = 9
            coordsX.insert(len(coordsX), positionX)
            coordsY.insert(len(coordsY), positionY)


    # represents the entirety of the game to the player
    def calculateGameboard(self, coordsX, coordsY, height, width):
        x = coordsX
        y = coordsY
        if int(self.point[0]) >= 0 and int(self.point[1]) >= 0:
            row = int(self.point[0])
            column = int(self.point[1])
            # right
            for i in range(height - column):
                bomb = 0
                if row + 1 < 9:
                    # bottom right
                    if column + i + 1 < 9 and column + i - 1 >= 0:
                        if self.graph[row + 1][column + i + 1] == 9 and self.graph[row][column + i] != 9:
                            bomb += 1
                    # bottom left
                    if column + i - 1 >= 0:
                        if self.graph[row + 1][column + i - 1] == 9 and self.graph[row][column + i] != 9:
                            bomb += 1
                    # down
                    if self.graph[row + 1][column + i] == 9 and self.graph[row][column + i] != 9:
                        bomb += 1
                if row - 1 >= 0:
                    # top right
                    if column + i + 1 < 9 and column + i + 1 >= 0:
                        if self.graph[row - 1][column + i + 1] == 9 and self.graph[row][column + i] != 9:
                            bomb += 1
                    # top
                    if column + i < 9:
                        if self.graph[row - 1][column + i] == 9 and self.graph[row][column + i] != 9:
                            bomb += 1
                    # top left
                    if column + i - 1 >= 0:
                        if self.graph[row - 1][column + i - 1] == 9 and self.graph[row][column + i] != 9:
                            bomb += 1
                # right
                if self.graph[row][column + i] == 9 and self.graph[row][column + i] != 9:
                    bomb += 1
                # left
                if column - i >= 0:
                    if self.graph[row][column + i - 1] == 9 and self.graph[row][column + i] != 9:
                        bomb += 1
                if bomb != 0:
                    self.graph[row][column + i] = bomb
                elif self.graph[row][column + i] == 0:
                    self.graph[row][column + i] = 11
                if self.graph[row][column + i] == 9:
                    break

            # left
            for i in range(column + 1):
                bomb = 0
                if row + 1 < 9:
                    # bottom right
                    if column - i + 1 < 9:
                        ##can't seem to get the alst coords :/
                        ##i see what's wrong now there's a value already there which is not 9 or 0
                        if self.graph[row + 1][column - i + 1] == 9 and self.graph[row][column - i] != 9:
                            bomb += 1
                    # bottom left
                    if column - i - 1 >= 0:
                        if self.graph[row + 1][column - i - 1] == 9 and self.graph[row][column - i] != 9:
                            bomb += 1
                    # down
                    if column - i >= 0:
                        if self.graph[row + 1][column - i] == 9 and self.graph[row][column - i] != 9:
                            bomb += 1
                if row - 1 >= 0:
                    # top right
                    if column - i + 1 < 9:
                        if self.graph[row - 1][column - i + 1] == 9 and self.graph[row][column - i] != 9:
                            bomb += 1
                    # top
                    if column - i >= 0:
                        if self.graph[row - 1][column - i] == 9 and self.graph[row][column - i] != 9:
                            bomb += 1
                    # top left
                    if column - i - 1 >= 0:
                        if self.graph[row - 1][column - i - 1] == 9 and self.graph[row][column - i] != 9:
                            bomb += 1
                # right
                ##sill a bit weird
                if column - i + 1 < 9:
                    if self.graph[row][column - i + 1] == 9 and self.graph[row][column - i] != 9:
                        bomb += 1
                # left
                if column - i - 1 >= 0:
                    if self.graph[row][column - i - 1] == 9 and self.graph[row][column - i] != 9:
                        bomb += 1
                if bomb != 0:
                    self.graph[row][column - i] = bomb
                elif self.graph[row][column - i] == 0:
                    self.graph[row][column - i] = 11
                if self.graph[row][column - i] == 9:
                    break
            # up
            for i in range(row + 1):
                bomb = 0
                if row - i + 1 < 9:
                    # bottom right
                    if column + 1 < 9:
                        if self.graph[row - i + 1][column + 1] == 9 and self.graph[row - i][column] != 9:
                            bomb += 1
                    # bottom left
                    if column - 1 >= 0:
                        if self.graph[row - i + 1][column - 1] == 9 and self.graph[row - i][column] != 9:
                            bomb += 1
                    # down
                    if row - i + 1 < 9:
                        if self.graph[row - i + 1][column] == 9 and self.graph[row - i][column] != 9:
                            bomb += 1
                if row - i - 1 >= 0:
                    # top right
                    if column + 1 < 9:
                        if self.graph[row - i - 1][column + 1] == 9 and self.graph[row - i][column] != 9:
                            bomb += 1
                    # top
                    if self.graph[row - i - 1][column] == 9 and self.graph[row - i][column] != 9:
                        bomb += 1
                    # top left
                    if column - 1 >= 0:
                        if self.graph[row - i - 1][column - 1] == 9 and self.graph[row - i][column] != 9:
                            bomb += 1
                # right
                if column + 1 < 9:
                    if self.graph[row - i][column + 1] == 9 and self.graph[row - i][column] != 9:
                        bomb += 1
                # lefts
                if column - 1 >= 0:
                    if self.graph[row - i][column - 1] == 9 and self.graph[row - i][column] != 9:
                        bomb += 1
                if bomb != 0:
                    self.graph[row - i][column] = bomb
                elif self.graph[row - i][column] == 0:
                    self.graph[row - i][column] = 11
                if self.graph[row - i][column] == 9:
                    break
            # down
            for i in range(height - row):
                bomb = 0
                if row + i + 1 < 9:
                    # bottom right
                    if column + 1 < 9:
                        if self.graph[row + i + 1][column + 1] == 9 and self.graph[row + i][column] != 9:
                            bomb += 1
                    # bottom left
                    if column - 1 >= 0:
                        if self.graph[row + i + 1][column - 1] == 9 and self.graph[row + i][column] != 9:
                            bomb += 1
                    # down
                    if row + i + 1 < 9:
                        if self.graph[row + i + 1][column] == 9 and self.graph[row + i][column] != 9:
                            bomb += 1
                if row + i - 1 >= 0:
                    # top right
                    if column + 1 < 9:
                        if self.graph[row + i - 1][column + 1] == 9 and self.graph[row + i][column] != 9:
                            bomb += 1
                    # top
                    if self.graph[row + i - 1][column] == 9 and self.graph[row + i][column] != 9:
                        bomb += 1
                    # top left
                    if column - 1 >= 0:
                        if self.graph[row + i - 1][column - 1] == 9 and self.graph[row + i][column] != 9:
                            bomb += 1
                # right
                if column + 1 < 9:
                    if self.graph[row + i][column + 1] == 9 and self.graph[row + i][column] != 9:
                        bomb += 1
                # left
                if column - 1 >= 0:
                    if self.graph[row + i][column - 1] == 9 and self.graph[row + i][column] != 9:
                        bomb += 1
                if bomb != 0:
                    self.graph[row + i][column] = bomb
                elif self.graph[row + i][column] == 0:
                    self.graph[row + i][column] = 11
                if self.graph[row + i][column] == 9:
                    break

            # self
            if self.graph[row][column] != 9:
                bomb = 0
                if row + 1 < 9:
                    # bottom right
                    if column + 1 < 9:
                        if self.graph[row + i][column + 1] == 9:
                            bomb += 1
                    # bottom left
                    if column - 1 >= 0:
                        if self.graph[row + 1][column - 1] == 9:
                            bomb += 1
                    # down
                    if self.graph[row + 1][column] == 9:
                        bomb += 1
                if row - 1 >= 0:
                    # top right
                    if column + 1 < 9:
                        if self.graph[row - 1][column + 1] == 9:
                            bomb += 1
                    # top
                    if self.graph[row - 1][column] == 9:
                        bomb += 1
                    # top left
                    if column - 1 >= 0:
                        if self.graph[row - 1][column - 1] == 9:
                            bomb += 1
                # right
                if column + 1 < 9:
                    if self.graph[row][column + 1] == 9:
                        bomb += 1
                # left
                if column - 1 >= 0:
                    if self.graph[row][column - 1] == 9:
                        bomb += 1
                print('start', bomb)
                if bomb != 0:
                    self.graph[row][column] = bomb
                elif self.graph[row][column] == 0:
                    self.graph[row][column] = 10
                print(self.graph)
