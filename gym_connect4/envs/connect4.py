import gym
import enum
import numpy as np


HEIGHT = 6
WIDTH = 7


class Connect4Env(gym.Env):
    metadata = {'render.modes': ['human', 'bot']}

    def __init__(self):
        # 6 x 7 board size
        self._reset()
        self.player = Locations.P1.value
        #self.opponent = Locations.P2
        pass

    def _step(self, action):
        #Do the turn




        ######### End of turn
        #self.done, tie = self.check_win_condition()
        #if self.done:
         #   return self.state, reward, self.done, {'state': self.state}
        self.perform_move(action, Locations.P1.value)
        return self.state, 0, self.done, {'state': self.state}
        pass

    def _seed(self, seed=None):
        return

    def _reset(self):
        self.board = np.zeros(HEIGHT * WIDTH).reshape(HEIGHT, WIDTH)
        self.state = {'board': self.board}
        self.done = False
        self.current_player = Locations.P1.value
        self.action_space = spaces.Discrete(WIDTH)
        pass

    def _render(self, mode='human', close=False):
        print(self.board)
        print("")

    def check_win_condition(self):
        # horizontalCheck
        for j in range(WIDTH - 3):
            for i in range(HEIGHT):
                if (self.board[i][j] == Locations.P1.value and
                    self.board[i][j+1] == Locations.P1.value and
                    self.board[i][j+2] == Locations.P1.value and
                    self.board[i][j+3] == Locations.P1.value):
                        return True

        # verticalCheck
        for i in range(HEIGHT - 3):
            for j in range(WIDTH):
                if (self.board[i][j] == Locations.P1.value and
                    self.board[i+1][j] == Locations.P1.value and
                    self.board[i+2][j] == Locations.P1.value and
                    self.board[i+3][j] == Locations.P1.value):
                        return True
                    
        # ascendingDiagonalCheck 
        for i in range(3, HEIGHT):
            for j in range(WIDTH - 3):
                if (self.board[i][j] == player and
                    self.board[i-1][j+1] == player and
                    self.board[i-2][j+2] == player and
                    self.board[i-3][j+3] == player):
                        return True

        # descendingDiagonalCheck
        for i in range(3, HEIGHT):
            for j in range(WIDTH):
                if (self.board[i][j] == player and
                    self.board[i-1][j-1] == player and
                    self.board[i-2][j-2] == player and
                    self.board[i-3][j-3] == player):
                        return True
        return False

    
    def perform_move(self, action, player_num):
        """ Assumes that the move is legal """
        chosen_col = self.board[:, (action - 1)]
        for i in range(len(chosen_col)):
            if int(chosen_col[6 - i - 1]) == 0:
                chosen_col[6 - i - 1] = player_num
                break

    def choose_legal_move(self):
        pass

class Locations(enum.Enum):
    P1 = 1
    P2 = -1
    Empty = 0

class Actions(enum.Enum):
    Col1 = 0
    Col2 = 1
    Col3 = 2
    Col4 = 3
    Col5 = 4
    Col6 = 5
    Col7 = 6
    
