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

        
def chess_board():
           return [['♜', '♞', ' ♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟︎', '♟︎', ' ♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎'],
            ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'],
            ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'],
           ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'],
            ['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]'],
            ['♙', '♙', ' ♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', ' ♗', '♕', '♔', '♗', '♘', '♖']]
      
def print_board(board):
    
    
    print("  ", end= "")
    for i in range(len(board)):
        letters = ['  a', 'b', 'c','d','e','f','g','h']
        print(letters[i], end = "  ")
    print()
    
    
    for i in range(len(board)):
        print(i+1, end = "  ")
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()
       
def main():
    print('Welcome to the Chess game!')
  
    player_turn = "White"
    board = chess_board()

    #Game loop
    #Printing the board and starting the game
    
    while True:
        print()
        print_board(board)
        print(f"\n {player_turn} make your move")
        
        # Let the player chose which piece they want to move
        piece = input(" Enter the square of the piece you want to move:")
        old_cell = piece
        column = ord(old_cell[0]) - ord('a')
        row = int(old_cell[1]) - 1 
        
        #Let the player choose the square they want to move too
        new_position = input(" Where would you like to move?:")
        new_column = ord(new_position[0]) - ord('a')
        new_row = int(new_position[1]) - 1
        print(" Moving piece from [", piece, "] to [", new_position,"]")
        break 

main()