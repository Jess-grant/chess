# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:05:35 2023

@author: jessi
"""




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
    print('The following key is used for this game:')
    print('K = King')
    print('Q = Queen')
    print('R = Rook')
    print('B = Bishop')
    print('H = Knight')
    print('P = Pawn')
    player_turn = "White"
    board = chess_board()

    #Game loop
    while True:
        print()
        print_board(board)
        print(f"\n {player_turn} make your move")
        piece = input(" Use the given key to chose which piece you want to move:")
        if piece == "K" or piece == "Q" or piece =="R" or piece =="B" or piece == "H" or piece =="P":
            print(" You have chosen", piece)
        else: 
            piece = input(" Invalid character, try again:")
        break

main()