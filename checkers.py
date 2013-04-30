# Dominic Tonozzi
# Aaron Beck
# This is a game of checkers so far, 1 is red, and 2 is black
# we have not yet implemented queening or whatever at the end of the board
# the AI is very simplistic and simply takes a piece if it can
# otherwise it just moves forward.
# 0 means no piece is there.


import math

board = []
user = 1
check=[]
score_1=0
score_2=0
players=1

def new_board():
    for i in range(0,64):
        board.append(0)
        check.append(i)
        i+=1

def print_board():
    print("")
    for i in range(1,9):
        # including a second board to try to play the game!
        print(repr(board[(i*8-8):(i*8)])+"        "+repr(check[(i*8-8):(i*8)]))
        i+=1
    print("")

def set_pieces():
    global board
    for i in range(0,8,2):
        board[i]=1
    for i in range(9,16,2):
        board[i]=1
    for i in range(16,24,2):
        board[i]=1
    for i in range(41,48,2):
        board[i]=2
    for i in range(48,56,2):
        board[i]=2
    for i in range(57,64,2):
        board[i]=2


# the move function takes a piece in the array as the first input and the position you
# want to move it to as the second argument. It should move the piece and delete the origonal.
def move(piece, position):
    if valid(piece, position):
        switch_user()


# valid kinda evolved into a lot more than just checking if a move is valid.
# I guess thats how it works sometimes.
def valid(piece, position):
    offset=math.fabs(piece%8-position%8)
    if board[piece]==user:
        if takepiece(piece, position):
            return True
        elif board[position]==0 and offset==1:
            #print("normal move")
            #print(position)
            #print(piece)
            board[position]=board[piece]
            board[piece]=0
            return True
    return False

# this took a bit of thinking, I figured it out by visualising what the difference between an edge position
# and a center position would be.
def takepiece(piece, position):
    global score_1
    global score_2
    offset=piece%8-position%8
    #print(offset)
    if math.fabs(offset)==1 and user==1 and position>piece and board[position] != 1:
        if board[position]==2:
            #print(offset)
            #print(board[position+9])
            #print(piece%8-(position+9)%8)
            if offset<0 and board[position+9]==0 and piece%8-(position+9)%8==-2:
                #print("HA! I took a piece!!")
                board[piece]=0
                board[position]=0
                board[position+9]=1
                score_1+=1
                return True
            if offset>0 and board[position-7]==0 and piece%8-(position-7)%8==2:
                #print("HA! I took a piece!!")
                board[piece]=0
                board[position]=0
                board[position+7]=1
                score_1+=1
                return True
    if math.fabs(offset)==1 and user==2 and position<piece and board[position] != 2:
        if board[position]==1:
            #print(offset)
            #print(board[position-7])
            #print(piece%8-(position-7)%8)
            if offset<0 and board[position-7]==0 and piece%8-(position-7)%8==-2:
                #print("HA! I took a piece!!")
                board[piece]=0
                board[position]=0
                board[position-7]=2
                score_2+=1
                return True
            if offset>0 and board[position-9]==0 and piece%8-(position-9)%8==2:
                #print("HA! I took a piece!!")
                board[piece]=0
                board[position]=0
                board[position-9]=2
                score_2+=1
                return True 
    return False

def switch_user():
    global user
    if user == 2:
        user = 1
    else:
        user = 2

#def print_score():

def turn():
    print_board()
    print("User %s, enter a piece to move and a position to move it to."%user)
    if players==1 and user==1:
        computer()
    else:
        if move(int(input("piece: ")),int(input("position: "))):
            print("That is not a valid move. Please try again.")
    # where a piece would normally be knighted, it instead is lost.
    for i in range(0,8,2):
        if board[i]==2:
            score_1+=1
            board[i]=0
    for i in range(56,64,2):
        if board[i]==1:
            score_2+=1
            board[i]=0

# Makes the computer take a piece. If it can't, it makes a random valid move.
def computer():
    #take a piece if we can
    for i in range(0,64):
        if board[i]==1:
            if takepiece(i, i+9):
                print("BORK!")
                switch_user()
                return True
            if takepiece(i, i+7):
                print("BORK!")
                switch_user()
                return True
            #print("\n\nadsfasdfasdfasdf\n\n")
            #if takepiece(18,27):
            #    print("\n\nOMGEEZY\n\n")
            #    switch_user()
            #    return True
                
    # otherwise make a random valid move. Actually its not random. Its moving the furthest right and up piece
    # thats valid first. I have no idea if this is a good strategy.
    #print("no computer moves to take player pieces\nMaking a silly move.")
    for i in range(0,64,2):
        if board[i]==1:
            if valid(i, i+9):
                #print("good")
                switch_user()
                return True
            if valid(i, i+7):
                #print("good")
                switch_user()
                return True

print("Welcome to a new game of checkers. Good luck!\n")
new_board()
set_pieces()
#board[27]=2
#switch_user()
while True:
    turn()
    if score_1>11:
        print("Congrats! You worked through the bugs and won the game player 1!")
        break
    if score_2>1:
        print("Congrats! You worked through the bugs and won the game player 2!")
        break



