from Draw import drawBoardFinish
from MineSweeper import MineSweeper


# gets player's input
def turn(minesweeper):
    print('insert coordinates. (IE. row,column)')
    user = input('>')
    ##self.cls()

    # get the coords then plot the section
    minesweeper.point = user.split(',')
    if int(minesweeper.point[0]) >= 0 and int(minesweeper.point[1]) < minesweeper.width + 1:
        minesweeper.calculateGameboard(minesweeper.coordsX, minesweeper.coordsY, minesweeper.height, minesweeper.width)
        drawBoardFinish(m, True)


if __name__ == '__main__':
    m = MineSweeper(9, 9)
    m.bombs(m.coordsX, m.coordsY, m.height, m.width)
    m.calculateGameboard(m.coordsX, m.coordsY, m.height, m.width)
    drawBoardFinish(m, True)

    while True:
        turn(m)
        if m.graph[int(m.point[0])][int(m.point[1])] == 9:
            drawBoardFinish(m, True)
            print('you hit a bomb ur dead')
            print('GAME OVER')
            break
    # needs a way to finish the game
