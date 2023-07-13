# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:05:35 2023

@author: jessi
"""


"""This is a function that creates a game of chess.
The function assumes that each player will only move their own pieces and will 
not attack their own pieces. 

The function assumes a player will only move their piece if the path is clear
for them to do so.

The function does not take into account any special moves.

The function does not account for stalemate. 

Further, the function assumes if a king is no longer present on the board one of the 
players must have performed checkmate correctly, and therefore, the game 
is over. """


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
        
# Function that checks if a move is valid
def validity(board, row, column, new_row, new_column):
    
    # check that the row and col are within the range
    if column in range(len(board)) and row in range(len(board)):
        return True 
    else:
        return False
    

# Function that moves the piece (assumes it is valid)

def move(board, row, column, new_row, new_column):
    
    #print the new chess board
   
    board[new_row][new_column] = board[row][column]
    board[row][column] = '[]'
    
    
# Convert user input into board indexes
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

# Function that enforces the rules for pawn

def pawn(board, row, column, new_row, new_column):
    if board[row][column] == '♟︎': 
        if row == 1 and new_row == row + 2 and new_column == column and board[new_row][new_column] == '[]':
            return True
        elif row == 1 and new_row == row + 1 and new_column == column and board[new_row][new_column] == '[]':
            return True
        elif new_row == row + 1 and new_column == column and board[new_row][new_column] == '[]':
            return True
        elif new_row == row + 1 and new_column == column + 1 and board[new_row][new_column] != '[]':
            return True
        elif new_row == row + 1 and new_column == column - 1 and board[new_row][new_column] != '[]':
            return True
    elif board[row][column] == '♙':
        if row == 6 and new_row == row - 2 and new_column == column and board[new_row][new_column] == '[]':
            return True
        elif row == 6 and new_row == row - 1 and new_column == column and board[new_row][new_column] == '[]':
            return True
        elif new_row == row - 1 and new_column == column and board[new_row][new_column] == '[]':
            return True
        elif new_row == row - 1 and new_column == column + 1 and board[new_row][new_column] != '[]':
            return True
        elif new_row == row - 1 and new_column == column - 1 and board[new_row][new_column] != '[]':
            return True
    else:
        return False
    
    
# Function that enforces the rules for a rook

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
        
       
# Function that checks if theres a clear path 

def clear(board, row, column, new_row, new_column):
    pass  # Currently N/A    

# Function that checks for checkmate

def checkmate(board):
    has_king_black = False
    has_king_white = False
    for i in range(board_dim):
        for j in range(board_dim):
            if board[i][j] == '♚': 
                has_king_black = True
            elif board[i][j] == '♔':
                has_king_white = True
                               
    if has_king_black and not has_king_white:
        return "Black"
    elif has_king_white and not has_king_black:
        return "White"
    
    return False
            
        

# Function that checks for stalemate
  # Currently N/A     
        
# Function that checks which chess rules need to be verified

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
                    
            check_result = checkmate(board)
            if check_result=="White" or check_result=="Black":
                print(f" Checkmate! Game Over {check_result} Wins!")
                return
                
            #Switch players
            if player_turn == "White":
                    player_turn = "Black"
            else:
                    player_turn = "White"
        else:
            print("Not Valid")   
       
            
game()
