# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:05:35 2023

@author: jessi
"""

# To commit and push do:
# 0. If you made changes elsewhere do `git pull` to start
# 1. Add the files you want to track (e.g. `git add chess.py`)
# 2. Commit the changes (e.g. `git commit -m "commit message"`)
# 3. Push the changes to GitHub (`git push`)


board_dim = 8
letters = [' a', 'b', 'c','d','e','f','g','h']
        
def chess_board():
           return [['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎'],
            ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'],
            ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'],
            ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'],
            ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']]
      
def print_board(board):
    
    
    print("  ", end= "")
    for i in range(len(board)):
        print(letters[i], end = "  ")
    print()
    
    
    for i in range(len(board)):
        print(i+1, end = "  ")
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()
        
# function that checks if a move is valid
def validity(board, row, column, new_row, new_column):
    
    # check that the row and col are within the range
    if column in range(len(board)) and row in range(len(board)):
        return True 
    else:
        return False
    

# a function that moves the piece (assumes it is valid)

def move(board, row, column, new_row, new_column):
    
    #print the new chess board
   
    board[new_row][new_column] = board[row][column]
    board[row][column] = '[]'
    
    
# convert user input into board indexes
def process_move(piece):
    # takes in the user input string
    # returns row and column they asked for, as integers
    # if it's bad, return -1, -1. 
    
    row = int(piece[1]) - 1 
    column = ord(piece[0]) - ord('a')
    if row in range(board_dim) and column in range(board_dim): 
        return row, column
    else:
        return -1, -1
    
# Create chess rules 
# Define a function that ensures the pawns moves according to rules
# Function must ensure pawn doesn't move backwards
# Function must ensure pawn only moves one space at a time

def pawn(board, row, column, new_row, new_column):
    if board[row][column] == '♟︎' and new_column == column and new_row == row + 1:
            return True
    elif board[row][column] == '♙' and new_column == column and new_row == row - 1:
            return True
    else:
        return False

# Define a function that enforces the rules for a rook

def rook(board, row, column, new_row, new_column) :
    if board[row][column] == '♜' or board[row][column] == '♖':
        if new_row == row or new_column == column:
            return True
        else:
            return False

    
    
# Function that enforces the rules for the king

def king(board, row, column, new_row, new_column):
    if board[row][column] == '♔' or board[row][column] == '♚':
        if abs(new_column - column) == 1 and new_row - row == 0:
            return True
        elif abs(new_row - row) == 1 and new_column - column == 0:
            return True
        elif abs(new_row - row) == 1 and abs(new_column - column) == 1:
            return True
        else:
            return False
                                      
# Function that enforces the rules for knight 

def knight(board, row, column, new_row, new_column):
    if board[row][column] == '♘' or board[row][column] == '♞':
        if new_column == column + 2 or new_column == column - 2:
            if new_row == row + 1 or new_row == row - 1:
                return True
            else:
                return False
            return True
        
        elif new_column == column + 1 or new_column == column - 1:
            if new_row == row + 2 or new_row == row - 2:
                return True
            return True
        else:
            return False
  
        
  
# Function that enforces the rules for bishop

def bishop(board, row, column, new_row, new_column):
    if board[row][column] == '♗' or board[row][column] == '♝':
        if abs(new_column - column) == abs(new_row - row):
            return True
        else: 
            return False



# Function that enforces the rules for queen

def queen(board, row, column, new_row, new_column):
    if board[row][column] == '♕' or board[row][column] == '♛':
       if abs(new_column - column) == 1 and new_row - row == 0:
           return True
       elif abs(new_row - row) == 1 and new_column - column == 0:
           return True
       elif abs(new_row - row) == 1 and abs(new_column - column) == 1:
           return True
       elif new_row == row or new_column == column:
           return True
       elif abs(new_column - column) == abs(new_row - row):
           return True
       else:
           return False
        
       
        
       
        
# Function that checks which chess rules need to be checked

def chess_rules(board, row, column, new_row, new_column):
    if board[row][column] == '♟︎' or board[row][column] == '♙':
        return pawn(board, row, column, new_row, new_column)
    if board[row][column] == '♜' or board[row][column] == '♖':
        return rook(board, row, column, new_row, new_column)
    if board[row][column] == '♔' or board[row][column] == '♚':
        return king(board, row, column, new_row, new_column)
    if board[row][column] == '♘' or board[row][column] == '♞':
        return knight(board, row, column, new_row, new_column)
    if board[row][column] == '♗' or board[row][column] == '♝':
        return bishop(board, row, column, new_row, new_column)
    if board[row][column] == '♕' or board[row][column] == '♛':
        return queen(board, row, column, new_row, new_column)
        
# Function that ensures the pieces are only moving if theres a clear path        
    
# Function for the main game 

def game():
    print('Welcome to the Chess game!')
  
    player_turn = "White"
    board = chess_board()

    #Game loop
    #Printing the board and starting the game
    
    while True:
        print()
        print_board(board)
        print(f"\n {player_turn} make your move")
       
        while True:
            # Let the player chose which piece they want to move
            piece = input(" Enter the square of the piece you want to move:")
            row, column = process_move(piece)
                              
                        
            #Let the player choose the square they want to move too
            new_position = input(" Where would you like to move to?:")            
            new_row, new_column = process_move(new_position)
           
        
            if row==-1 or column==-1 or new_row==-1 or new_column==-1:
                print("Invalid board position, Try again!")
            else:
                if chess_rules(board, row, column, new_row, new_column):
                    
                    break
                print(" That move breaks chess rules, try again!")
            
        if validity(board, row, column, new_row, new_column):
            
                #print the new chess board
            move(board, row, column, new_row, new_column)
              
            print(" Moving piece from [", piece, "] to [", new_position,"]")
                        
                        
                #Switch players
            if player_turn == "White":
                    player_turn = "Black"
            else:
                    player_turn = "White"
        else:
            print("Not Valid")

            ##define a global rules function that i can put in the game function that checks the 
            # variable and then based on which variable it is it runs it through that function
        
       
            
game()