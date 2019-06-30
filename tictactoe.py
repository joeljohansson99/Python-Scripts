import os
clear = lambda: os.system('cls')

Win = True

board = [' ']*9

def init():
    global Draw
    Draw = False
    for n in range(0,9):
        board[n] = ' '

def display():
    print ( "   |   |   ")
    print (" "+board[6]+" | "+board[7]+" | "+board[8]+"  ")
    print ("   |   |")
    print ("---|---|---")
    print ("   |   |")
    print (" "+board[3]+" | "+board[4]+" | "+board[5]+"  ")
    print ("   |   |")
    print ("---|---|---")
    print ("   |   |")
    print (" "+board[0]+" | "+board[1]+" | "+board[2]+"  ")
    print ("   |   |   ")

def player_one():
    chose = int(input('Choose your move: '))
    while True:
        if chose<10 and chose>=0:
            if board[chose-1]==' ':
                board[chose-1]= 'O'
                break
        chose = int(input('Unclear choice, try again: '))

def player_two():
    chose = int(input('Choose your move: '))
    while True:
        if chose<10 and chose>=0:
            if board[chose-1]==' ':
                board[chose-1]= 'X'
                break
        chose = int(input('Unclear choice, try again: '))

def check_win():     
    global Draw
    #Horizontal winning condition    
    if(board[0] == board[1] and board[1] == board[2] and board[0] != ' '):    
        return False    
    elif(board[3] == board[4] and board[4] == board[5] and board[3] != ' '):    
        return False    
    elif(board[6] == board[7] and board[7] == board[8] and board[6] != ' '):    
        return False    
    #Vertical Winning Condition    
    elif(board[0] == board[3] and board[3] == board[6] and board[0] != ' '):    
        return False    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        return False    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        return False    
    #Diagonal Winning Condition    
    elif(board[0] == board[4] and board[4] == board[8] and board[4] != ' '):    
        return False    
    elif(board[2] == board[4] and board[4] == board[6] and board[4] != ' '):    
        return False    
    #Match Tie or Draw Condition    
    elif(board[0]!=' ' and board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' '):    
        Draw = True
        return False
    else:            
        return True 

def run():
    while True:
        clear()
        init()
        display()
        while True:
            player_one()
            clear()
            check_win()
            display()
            if not check_win():
                Win = True
                break
            player_two()
            clear()
            check_win()
            display()
            if not check_win():
                Win = False
                break
        if Draw:
            s = input("Draw! \n Wanna play again? [y/n]:")
            if s!='y':
                break
        elif Win:
            s = input("Player One Wins! \n Wanna play again? [y/n]:")
            if s!='y':
                break
        else:
            s = input("Player Two Wins! \n Wanna play again? [y/n]:")
            if s!='y':
                break

run()