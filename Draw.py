def drawBoardFinish(minesweeper, draw):
    width = minesweeper.width
    height = minesweeper.height
    graph = minesweeper.graph

    print(" " * 4, end='')
    for i in range(width):
        print("|", i, "", end='')
    print('|')
    for row in range(width):
        print('----' * (width + 1))
        if row != 0:
            print(row, end='   ')
        if row == 0:
            print(row, end='   ')
        for column in range(height):
            print('|', end='')
            if graph[row][column] == 0:
                print('   ', end='')
            elif graph[row][column] == 9 and draw:
                print(' B ', end='')
            elif graph[row][column] == 9 and not draw:
                print('   ', end='')
            elif graph[row][column] == 10:
                print(' X ', end='')
            elif graph[row][column] == 11:
                print(' N ', end='')
            elif graph[row][column] == 1:
                print(' 1 ', end='')
            elif graph[row][column] == 2:
                print(' 2 ', end='')
            elif graph[row][column] == 3:
                print(' 3 ', end='')
            elif graph[row][column] == 4:
                print(' 4 ', end='')
            elif graph[row][column] == 5:
                print(' 5 ', end='')
            elif graph[row][column] == 6:
                print(' 6 ', end='')
            elif graph[row][column] == 7:
                print(' 7 ', end='')
            elif graph[row][column] == 8:
                print(' 8 ', end='')
        # replace this with the number of bombs surrounding it
        print('|')
