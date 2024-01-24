def getChessSquareColor(column, row):
    while column in range(0,8) and row in range(0,8):
        if column % 2 == 0 and row % 2 == 0:
            return 'white'
        if column % 2 != 0 and row % 2 != 0:
            return 'white'
        else:
            return 'black'
    else:
        return ''


assert getChessSquareColor(0, 0) == 'white'

assert getChessSquareColor(1, 0) == 'black'

assert getChessSquareColor(0, 1) == 'black'

assert getChessSquareColor(7, 7) == 'white'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''