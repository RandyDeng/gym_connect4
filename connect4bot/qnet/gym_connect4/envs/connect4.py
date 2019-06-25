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
        self.opponent = Locations.P2
        pass

    def _step(self, action):
        #Do the turn




        ######### End of turn
        self.done, tie = self.check_win_condition()
        if self.game_over:
            return self.state, reward, self.game_over, {'state': self.state}
        pass

    def _reset(self):
        self.board = np.zeros(6 * 7)
        self.done = False
        self.current_player = Locations.P1
        pass

    def _render(self, mode='human', close=False):
        pass

    def check_win_condition(self):
        pass
    

class Locations(enum.Enum):
    P1 = 1
    P2 = -1
    Empty = enum.auto()

class Actions(enum.Enum):
    Col1 = enum.auto()
    Col2 = enum.auto()
    Col3 = enum.auto()
    Col4 = enum.auto()
    Col5 = enum.auto()
    Col6 = enum.auto()
    Col7 = enum.auto()
    
