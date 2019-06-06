#board file
import numpy as np
import enum

class Token(enum.Int):
    Blank = enum.auto()
    Red = enum.auto()
    Black = enum.auto()

class Board():
    self.current_state
    
    def fill_spot(self, move):
        """
        Fill a spot with a player's move
        """
        pass
    
    def check_for_winner():
        """
        Check the board for a winner
        """
        pass
