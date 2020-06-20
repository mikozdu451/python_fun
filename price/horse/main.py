def move1(x, y):
    if x + 2 < 8 & y + 1 < 8:
        x += 2
        y += 1
        return True
    return False


def move2(x, y):
    if x + 2 < 8 & y - 1 >= 0:
        x += 2
        y -= 1
        return True
    return False


def move3(x, y):
    if x - 2 >= 0 & y + 1 < 8:
        x -= 2
        y += 1
        return True
    return False


def move4(x, y):
    if x - 2 >= 0 & y - 1 >= 0:
        x -= 2
        y -= 1
        return True
    return False


def move5(x, y):
    if x + 1 < 8 & y + 2 < 8:
        x += 1
        y += 2
        return True
    return False


def move6(x, y):
    if x + 1 < 8 & y - 2 >= 0:
        x += 1
        y -= 2
        return True
    return False


def move7(x, y):
    if x - 1 >= 0 & y + 2 < 8:
        x -= 1
        y += 2
        return True
    return False


def move8(x, y):
    if x - 1 >= 0 & y - 2 >= 0:
        x -= 1
        y -= 2
        return True
    return False

def jump():
    moveList.append()


moveList = []
emptyFields = True
possibleMove = True
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]


x, y = input().split()
print(x + " and " + y)
x -= 1
y -= 1

board[x][y] = 1

