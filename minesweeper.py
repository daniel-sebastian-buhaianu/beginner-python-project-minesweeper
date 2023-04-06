# implementation of a basic minesweeper game
# which can be played in the terminal window 

import random

# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # lets create the board
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row, col) tuples into this set
        self.dug = set() # if we dig at 0,0 then self.dug = {(0,0)}
    
    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here
        # since we have a 2-D board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                # bomb already exists there, so skip
                continue

            board[row][col] = '*' # plant the bomb
            bombs_planted += 1
        
        return board

    def assign_values_to_board(self):
        # now that we have the bombs planted, let's assign a number 0-8
        # for all the empty spaces, which represents how many neighboring
        # bombs there are. we can precompute these and it'll save us some
        # effort checking what's around the board later on
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] == '*':
                    # if this is already a bomb, we don't want to do anything
                    continue
                self.board[row][col] = self.get_num_bombs_nearby(row, col)

    def get_num_bombs_nearby(self, row, col):
        # let's iterate through each of the neighboring positions
        # and sum number of bombs, making sure we don't go out of bonds
        num_bombs_nearby = 0
        for r in range(max(0, row-1), min(self.dim_size-1, (row+1)) + 1):
            for c in range(max(0, col-1), min(self.dim_size-1, (col+1)) + 1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_bombs_nearby += 1
        return num_bombs_nearby

    def dig(self, row, col):
        # dig at the location chosen by user
        # return True if successful, False if bomb dug

        # scenarios:
        # hit a bomb -> game over
        # dig at location with nearby bombs -> finish dig
        # dig at location with no nearby bombs -> recursively dig neighbors!
        
        self.dug.add((row, col)) # keep track that we dug here
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, (row+1)) + 1):
            for c in range(max(0, col-1), min(self.dim_size-1, (col+1)) + 1):
                if (r, c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r, c)
        
        # if our initial dig didn't hit a bomb, we shouldn't hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object
        # it'll print out what this function returns
        # so we want to return a string that shows the board to the player
        pass        

# play the game
def play(dim_size=10, num_bombs=10):
    # step 1: create the bord and plant the bombs
    board = Board(dim_size, num_bombs)
    
    # step 2: show the user the board and ask for where they want to dig

    # step 3a: if location is a bomb, show game over message
    # step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # step 4: repeat steps 2 and 3a/b until there are no more places to dig -> victory!
    pass

 