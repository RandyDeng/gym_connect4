import gym
import enum
import numpy as np

from gym import error, spaces, utils
from gym.utils import seeding

class C4Env(gym.Env):
    metadata = {'render.modes': ['human', 'bot']}

    def __init__(self):
        # 6 x 7 board size
        self._reset()
        self.player = Locations.P1
        #self.opponent = Locations.P2
        pass

    def _step(self, action):
        #Do the turn




        ######### End of turn
        #self.done, tie = self.check_win_condition()
        #if self.done:
         #   return self.state, reward, self.done, {'state': self.state}
        self.perform_move(action, 1)
        return self.state, 0, self.done, {'state': self.state}
        pass

    def _seed(self, seed=None):
        return

    def _reset(self):
        self.board = np.zeros(6 * 7)
        self.state = {'board': self.board}
        self.done = False
        self.current_player = Locations.P1
        self.action_space = spaces.Discrete(7)
        pass

    def _render(self, mode='human', close=False):
        print(self.board.reshape(6,7))
        print("")
        pass

    def check_win_condition(self):
        if Locations.Empty in self.board:
            pass
        pass
    
    def perform_move(self, action, player_num):
        """
        Assumes that the move is legal
        """
        temp = self.board.reshape(6,7)
        chosen_col = temp[:,(action-1)]
        for i in range(len(chosen_col)):
            #breakpoint()
            if int(chosen_col[6 - i -1]) == 0:
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
    
