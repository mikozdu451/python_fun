import random
def opponent(x):
    y = random.choice(x)
    x.remove(y)
    return y

def check_w():

    outcome = '_'
    if field[0][0] == field[0][1] == field[0][2]:
        if field[0][0] != '_':
            outcome = field[0][0]
    elif field[1][0] == field[1][1] == field[1][2]:
        if field[1][0] != '_':
            outcome = field[1][0]
    elif field[2][0] == field[2][1] == field[2][2]:
        if field[2][0] != '_':
            outcome = field[2][0]
    elif field[0][0] == field[1][0] == field[2][0]:
        if field[0][0] != '_':
            outcome = field[0][0]
    elif field[0][1] == field[1][1] == field[2][1]:
        if field[0][1] != '_':
            outcome = field[0][1]
    elif field[0][2] == field[1][2] == field[2][2]:
        if field[0][2] != '_':
            outcome = field[0][2]
    elif field[0][0] == field[1][1] == field[2][2]:
        if field[0][0] != '_':
            outcome = field[0][0]
    elif field[0][2] == field[1][1] == field[2][0]:
        if field[0][2] != '_':
            outcome = field[0][2]


    if outcome == '_':
        return True
    else:
        if outcome == 'X':
            print("You won! congratulations!!!")
            return False
        elif outcome == 'O':
            print("Computer wins! You lose!")
            return False

moves = [[0, 0], [0, 1], [0, 2],
         [1, 0], [1, 1], [1, 2],
         [2, 0], [2, 1], [2, 2]]

field = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]
check_g = True
# for i in field:
#     for j in i:
#         print(j, end = " ")
#     print("")

print('TIC-TAC-TOE')
print("""You will be playing on a 3 x 3 grid which will look like this:
             1  2  3
            ----------
          1 |  |  |  |
            ----------
          2 |  |  |  |
            ----------
          3 |  |  |  |
            ----------
Input the coordinates of slice where yuu want the X to be put, for example input '1 2' will output:
             1  2  3
            ----------
          1 |  | X|  |
            ----------
          2 |  |  |  |
            ----------
          3 |  |  |  |
            ----------
You know the rest of the rules! Get 3 in a row! And try to win against the computer! Good luck!""")
while check_g:
    in_line = input("Coordinates: ")
    if len(in_line) == 3:
        try:
            x, y = in_line.split()  #decleraing x and y variable
        except ValueError:
            print("Your input is wrong!! Try again please")
        else:
            x = int(x)
            y = int(y)
            acceptable = [1,2,3]
            if x in acceptable and y in acceptable: #checking if they are in range
                x -= 1
                y -= 1
                in_choice = [x,y]
                #print(in_choice)
                if in_choice not in moves:          #in case the spot that was chosen is already taken
                    print("That spot is already taken, try somewhere else")
                else:
                    field[x][y] = 'X'               #mark the spot for the pleyer
                    for i in moves:
                        if i == in_choice:
                            moves.remove(i)

                    if len(moves) < 5:
                        check_g = check_w()

                    elif len(moves) < 0:             #check if there are still places left on the board
                        print("You are out of moves! Game over")
                        check_g = False

                    else:

                        #opponent(field)
                        o_move = opponent(moves)            #call the oponent function
                        field[o_move[0]][o_move[1]] = 'O'

                        #print(moves)           use if you want to check if the move list is ok

                        for i in field:         #print the field
                            for j in i:
                                print(j, end= ' ')
                            print("")

                        if len(moves) < 4:
                            check_g = check_w()
            else:
                print("Your number are out of range! You can use only numbers 1, 2 ,3 in combination: first number second number")
    else:
        print("Your line is to long or to short! it is supposed to be 3 characters! First number from 1 to 3 space and second character from 1 to 3")

input("\nPress enter to exit")
