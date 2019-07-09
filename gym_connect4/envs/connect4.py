import gym
import enum
import numpy as np

from gym import spaces

HEIGHT = 6
WIDTH = 7

class Connect4Env(gym.Env):
    metadata = {'render.modes': ['human', 'bot']}

    def __init__(self):
        self.reset()
        self.player = Player.P1.value

    def step(self, action):
        #### RANDOM CHOIE MOVE
        #print(self.action_space)
        if self.first_player:
            opp_action = np.random.choice(self.action_space)
            #print(opp_action)
            last_played = self.perform_move(opp_action, Player.P2.value)
            self.update_legal_moves(opp_action)
            self.done, reward = self.check_win_condition(last_played, opp_action, Player.P2.value)
            self.first_player = False
            if self.done:
                self.state = self.board
                return np.array(self.state), reward, self.done, {}
                #return self.state, reward, self.done, {}
        ######### End of turn
        #self.done, tie = self.check_win_condition()
        #if self.done:
         #   return self.state, reward, self.done, {'state': self.state}
        #AI MOVE
        else:
            last_played = self.perform_move(action, Player.P1.value)
            self.update_legal_moves(action)
            self.done, reward = self.check_win_condition(last_played, action, Player.P1.value)
            self.first_player = True
            self.state = self.board
            return np.array(self.state), reward, self.done, {}
            #return self.state, reward, self.done, {}
        return 0, 0, 0, {}

    def seed(self, seed=None):
        return

    def reset(self):
        self.board = np.zeros(HEIGHT * WIDTH).reshape(HEIGHT, WIDTH)
        self.observation_space = spaces.Box(-1, 1, shape=(6,7))
        #self.observation_space = spaces.Box(-1, 1, dtype=np.float32)
        #self.state = {'board': self.board}
        self.state = self.board
        self.done = False
        self.current_player = Player.P1.value
        self.action_space = [0, 1, 2, 3, 4, 5, 6]
        self.first_player = np.random.choice([True,False])
        return np.array(self.state)

    def render(self, mode='human', close=False):
        print(self.board)
        print("")

    def perform_move(self, action, player_num):
        """ Assumes that the move is legal """
        chosen_col = self.board[:, action]
        for i in range(len(chosen_col)):
            if int(chosen_col[6 - i - 1]) == 0:
                chosen_col[6 - i - 1] = player_num
                return 6 - i - 1

    def check_win_condition(self, last_played, action, player_val):
        tie = False
        done = False
        filled = False
        count = 1
        if Player.Empty.value not in self.board:
            filled = True
        if (0 < last_played and 0 < action):
            if self.board[last_played - 1][action - 1] == player_val:
                done = self.check_d1(last_played, action, player_val)
        elif last_played < HEIGHT - 1 and action <  WIDTH - 1:
            if self.board[last_played + 1][action + 1] == player_val:
                done = self.check_d1(last_played, action, player_val)

        if (0 < last_played and action < WIDTH - 1):
            if self.board[last_played - 1][action + 1] == player_val:
                done = done or self.check_d2(last_played, action, player_val)
        elif (last_played < HEIGHT - 1 and 0 < action):
            if self.board[last_played + 1][action - 1] == player_val:
                done = done or self.check_d2(last_played, action, player_val)

        if (action < WIDTH - 1) or (0 < action):
            if self.board[last_played][action - 1] == player_val:
                done = done or self.check_horizontal(last_played, player_val)
        elif 0 < action:
            if self.board[last_played][action + 1] == player_val:
                done = done or self.check_horizontal(last_played, player_val)

        if (last_played < HEIGHT - 1):
            if self.board[last_played + 1][action] == player_val:
                done = done or self.check_vertical(action, player_val)

        if filled and not done:
            # TIE = 0 reward
            return True, 0
        if done:
            # Game won by player = 1 reward; won by opponent = -1
            return True, (1 * player_val)
        else:
            # Game not done = 0 reward
            return False, 0

    def check_d1(self, row, col, player_val):
        start_r = row - min(row, col)
        start_c = col - min(row, col)
        count = 0
        while start_r < HEIGHT and start_c < WIDTH:
            if self.board[start_r, start_c] == player_val:
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
            start_r = start_r + 1
            start_c = start_c + 1
        return False

    def check_d2(self, row, col, player_val):
        start_r = row + min(HEIGHT - row - 1, col)
        start_c = col - min(HEIGHT - row - 1, col)
        #print('row {} col {}, sr {} sc {}'.format(row, col, start_r, start_c))
        count = 0
        while start_r >= 0 and start_c < WIDTH:
            if self.board[start_r, start_c] == player_val:
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
            start_r = start_r - 1
            start_c = start_c + 1
        return False
    
    def check_horizontal(self, row, player_val):
        count = 0
        r = self.board[row,:]
        for i in range(4):
            if r[i] == r[i + 1] == r[i + 2] == r[i + 3] == player_val:
                return True
        return False

    def check_vertical(self, column, player_val):
        col = self.board[:,column]
        for i in range(3):
            if col[i] == col[i + 1] == col[i + 2] == col[i + 3] == player_val:
                return True
        return False
    
    def update_legal_moves(self, col):
        #for i in self.action_space[:]:
        if not np.any(self.board[:,col] == 0):
            #print('removed col {}'.format(col))
            self.action_space.remove(col)
                #break

class Player(enum.Enum):
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

