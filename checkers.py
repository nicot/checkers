# Dominic Tonozzi 101350219
# Michael Asnes 811014752
# Dillon Drenzek
# This is a game of checkers so far, 1 is red, and 2 is black
# we have not yet implemented queening or whatever at the end of the board   (update, this is now partially implemented)
# the AI is very simplistic and simply takes a piece if it can				(it's set up for everything except the takepiece function)
# otherwise it just moves forward.
# 0 means no piece is there.


import math

board = []
user = 1
check=[]
score_1=0
score_2=0
players=1
takepiece_return=0

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

# a test to see if the piece has been placed at the end of the board.
# if true, then make_king
# for coding simplicity, I'm assuming that players will never move to
# the edge of the board closest to them - only the one away from them
def end_of_board(piece):
	if piece >= 0 and piece <= 7 and user==2:
		return True
	if piece >= 56 and piece <= 63 and user==1:
		return True
	return False

# makes the piece a king. By convention, kings are represented by a
# number which is 3 times what the player's number was
def make_king(piece):
	if board[piece] < 3 and board[piece] > 0: # making sure not to king a king
		board[piece] = board[piece] * 3
		print("Your piece has been made a king!")


#increases the score
def addscore():
    global score_1
    global score_2
    if user == 1:
        score_1 += 1
    elif user == 2:
        score_2 = score_2 + 1
    else:
        print("Unknown player!!!!")

# the move function takes a piece in the array as the first input and the position you
# want to move it to as the second argument. It should move the piece and delete the origonal.
def move(piece, position):
    if valid(piece, position):
        board[position]=board[piece]
        board[piece]=0
        piece = position
        if end_of_board(piece):
                 make_king(piece)
                 return True
        else:
                 return True
    elif takepiece(piece, position):
        board[position]=0
        board[takepiece_return] = board[piece]
        board[piece]=0
        addscore()
        piece = position
        if end_of_board(piece):
                 make_king(piece)
                 return True
        else:
                 return True
    else:
        return False


# valid kinda evolved into a lot more than just checking if a move is valid.
# Update (Michael): I've changed this so it merely checks to see if a move is valid or not.
# Check does not include takepiece (that's another check)
# I guess thats how it works sometimes.
def valid(piece, position):
    offset=piece%8-position%8
    if math.fabs(piece - position) < 3 or math.fabs(piece - position) > 12: ##prevents moving the piece one to the right/left # prevents piece from moving two spaces
        offset = 10
    if takepiece(piece, position):
        return False                #This way the move command get's it's input from the takepiece function instead
    elif board[piece]==user:
        if board[position]==0 and math.fabs(offset)==1:
            if user==1 and position>piece:
                #print("normal move")
                #print(position)
                #print(piece)
                return True
            elif user==2 and position<piece:
                #print("normal move")
                #print(position)
                #print(piece)
                return True
    elif board[piece] == user * 3:
        if board[position] == 0 and (math.fabs(offset) == 1):
           return True
    return False


# this took a bit of thinking, I figured it out by visualising what the difference between an edge position
# and a center position would be.
# Michael: So you understand offset because you used it. Also, math.fabs(x) returns the absolute value of x.
# In the takepiece function there is two initial caes either its user 1 jumping 2's piece or the other way around.
# You then check to see which diagonal the piece is being jumped from. The way I did this is check which direction
# the offset is to, either less than or greater than 0. Then if its less than I check the array spot thats down and
# to the left of the jumped piece (eg board[position+9]) So for going backwards we'll have to add to the innermost
# if statement and check if board[piece]%3==0 and then see if it can go that way. So we'll end up with four nested
# ifs instead of 2.
def takepiece(piece, position):
    global takepiece_return # for use with the move function.
    global score_1
    global score_2
    offset=piece%8-position%8
    if math.fabs(piece - position) < 3 or math.fabs(piece - position) > 12:
        offset = 10
    #print(offset)
    if math.fabs(offset)==1 and user==1 and board[position] != 1 and board[position] != 3:
        if board[position]==2 or board[position]==6:
            #print(offset)
            #print(board[position+9])
            #print(piece%8-(position+9)%8)
            if offset<0 and board[position+9]==0 and piece%8-(position+9)%8==-2 and position>piece:
                #print("HA! I took a piece!!")
                takepiece_return = position + 9
                return True
            elif offset>0 and board[position+7]==0 and piece%8-(position+7)%8==2 and position>piece:
                #print("HA! I took a piece!!")
                takepiece_return = position + 7
                return True
            elif offset<0 and board[position-7]==0 and piece%8-(position-7)%8==-2 and board[piece] == user*3:
             #print("HA! I took a piece!!")
                takepiece_return = position - 7
                return True
            elif offset>0 and board[position-9]==0 and piece%8-(position-9)%8==2 and board[piece] == user*3:
                #print("HA! I took a piece!!")
                takepiece_return = position - 9
                return True
            else:
                return False
    elif math.fabs(offset)==1 and user==2 and position<piece and board[position] != 2 and board[position] != 6:
        if board[position]==1 or board[position]==3:
            #print(offset)
            #print(board[position-7])
            #print(piece%8-(position-7)%8)
            if offset<0 and board[position-7]==0 and piece%8-(position-7)%8==-2 and position<piece:
                #print("HA! I took a piece!!")
                takepiece_return = position -7
                return True
            elif offset>0 and board[position-9]==0 and piece%8-(position-9)%8==2 and position<piece:
                #print("HA! I took a piece!!")
                takepiece_return = position -9
                return True
            elif offset<0 and board[position+9]==0 and piece%8-(position+9)%8==-2 and board[piece] == user*3:
                #print("HA! I took a piece!!")
                takepiece_return = position + 9
                return True
            elif offset>0 and board[position+7]==0 and piece%8-(position-7)%8==2 and board[piece] == user*3:
                #print("HA! I took a piece!!")
                takepiece_return = position + 7
                return True
            else:
                return False
    else:
        return False

def switch_user():
    global user
    if user == 2:
        user = 1
    else:
        user = 2

#def print_score():

def turn():
    print_v = 0
    print_board()
    print("User %s, enter a piece to move and a position to move it to."%user)
#    if players==1 and user==1:
#        computer()
 #   else:
    while move(int(input("piece: ")),int(input("position: "))) == False:
            if print_v == 0:
                print("That is not a valid move. Please try again.")
                print_v = 1
            elif print_v == 1:
                print("You're still not making valid moves. Please try again")
                print_v = 2
    print("player 1 score: ", score_1, "player 2 score: ", score_2)

    # where a piece would normally be knighted, it instead is lost.
    #for i in range(0,8,2):
    #    if board[i]==2:
    #        score_1+=1
    #        board[i]=0
    #for i in range(56,64,2):
    #    if board[i]==1:
    #        score_2+=1
    #        board[i]=0

# Makes the computer take a piece. If it can't, it makes a random valid move.
def computer():
    #take a piece if we can
    done = False
    for i in range(0,64,2):
        if done == False:
            print("done false!")
            if board[i]==1:
                print("step 2!")
                if takepiece(i, i+9):
                    print("takepiece 1 true")
                    move(i, i+9)
                    #print("BORK!")
                    done = True
                    return True
                    break
                if takepiece(i, i+7):
                    print("takepiece 2 true")
                    move(i, i+9)
                    #print("BORK!")
                    done = True
                    return True
                    break
                print("step 3")
                print(done)
            #print("\n\nadsfasdfasdfasdf\n\n")
            #if takepiece(18,27):
            #    print("\n\nOMGEEZY\n\n")
            #    switch_user()
            #    return True

    # otherwise make a random valid move. Actually its not random. Its moving the furthest right and up piece
    # thats valid first. I have no idea if this is a good strategy.
    #print("no computer moves to take player pieces\nMaking a silly move.")
    for i in range(0,64,2):
        if done == False:
            if board[i]==1:
                if valid(i, i+9):
                    move(i, i+9)
                    #print("good")
                    done = True
                    return True
                    break
                if valid(i, i+7):
                    move(i, i+7)
                    #print("good")
                    done = True
                    return True
                    break

print("Welcome to a new game of checkers. Good luck!\n")
new_board()
set_pieces()
#board[27]=2
#switch_user()
while True:
    print(score_1, score_2)
    turn()
    switch_user()
    if score_1>11:
        print("Congrats! You worked through the bugs and won the game player 1!")
        break
    if score_2>11:
        print("Congrats! You worked through the bugs and won the game player 2!")
        break



