# Chess Dictionary Validator

# In this chapter, we used the dictionary value {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'} to represent a chessboard. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on whether the board is valid.

# A valid board will have exactly one black king and exactly one white king. Each player can have at most 16 pieces, of which only eight can be pawns, and all pieces must be on a valid square from '1a' to '8h'. That is, a piece can’t be on square '9z'. The piece names should begin with either a 'w' or a 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chessboard. (This isn’t an exhaustive list of requirements, but it is close enough for this exercise.)

def isValidChessBoard(board):
    # Track piece counts
    piece_counts = {'w': 0, 'b': 0}
    king_counts = {'w': 0, 'b': 0}
    pawn_counts = {'w': 0, 'b': 0}
    
    # Valid rows and columns
    valid_files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    valid_ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
    valid_pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    for position, piece in board.items():
        # 1. Validate the square (e.g., '1a' or 'a1' depending on how you write it)
        # Your dict uses '2a' (rank then file)
        if len(position) != 2 or position[0] not in valid_ranks or position[1] not in valid_files:
            return False
            
        # 2. Validate piece name format (must start with 'w' or 'b')
        color = piece[0]
        piece_name = piece[1:] # Note: The book prompt uses full names like 'king'/'pawn', your dict uses 'K'/'P'
        
        if color not in ['w', 'b']:
            return False
            
        # Update counts
        piece_counts[color] += 1
        if piece_name.lower() == 'k' or piece_name.lower() == 'king':
            king_counts[color] += 1
        if piece_name.lower() == 'p' or piece_name.lower() == 'pawn':
            pawn_counts[color] += 1

    # 3. Verify total constraints
    if king_counts['w'] != 1 or king_counts['b'] != 1:
        return False
    if piece_counts['w'] > 16 or piece_counts['b'] > 16:
        return False
    if pawn_counts['w'] > 8 or pawn_counts['b'] > 8:
        return False
        
    return True

# Test it out
proper_chess_board = {
    "2a": "wP", "2b": "wP", "1a": "wR", "1b": "wK",
    "7a": "bP", "7b": "bP", "8a": "bR", "8b": "bK"
}

print(isValidChessBoard(proper_chess_board)) # Should output True