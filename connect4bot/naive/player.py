#Player class
import numpy as np

class Player():
    self.known_moves = set()
    #bit string
    self.position = b'0000000\
                      0000000\
                      0000000\
                      0000000\
                      0000000\
                      0000000\
                      0000000'

    
    def gain_knowledge(self):
        """
        This method imports the player's learned dataset from the text file
        """
        pass

    def dump_knowledge(self):
        """
        This method updates the text file with the players knowledge in it
        """
        pass

    def update_position(self, location):
        self.postion[location] = 1

    def choose_new_location(self):
        """
        :returns: a 0-6 value denoting the slot the player is choosing.
        """
        pass
