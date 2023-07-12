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
    print(board[row][column])
    board[new_row][new_column] = board[row][column]
    board[row][column] = '[]'
    print(board)
    
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
            print(row, column, new_row, new_column)
        
            if row==-1 or column==-1 or new_row==-1 or new_column==-1:
                print("Hey no bad!")
            else:
                break
            
            
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
            print("not valid")
game()