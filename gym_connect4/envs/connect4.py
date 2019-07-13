import gym
import enum
import numpy as np

from gym import spaces

HEIGHT = 6
WIDTH = 7

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


class Connect4Env(gym.Env):
    def __init__(self, opponent):
        self.count = 0
        self.reset()
        self.opponent = opponent
        self.player = Player.P1.value
        self.last_ai_move = 0
        self.probs = [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7]

    def check_would_win(self, player_num):
        for move in self.action_spaces:
            if move not in self.illegal:
                row = self.get_row_number(move)
                if row < 3:
                    if self.check_vertical(move, player_num, would_win=True, row=row):
                        return True, move
                if self.check_horizontal(row, player_num, would_win=True, col=move):
                    return True, move
                if self.check_d1(row, move, player_num, would_win=True):
                    return True, move
                if self.check_d2(row, move, player_num, would_win=True):
                    return True, move
        return False, -1

    def step(self, action):
        # Rewards: -1 for losing, 0 for tie, 1 for winning
        reward = 0
        # Keep track of moves for updating the opponent action policy
        self.count = self.count + 1
        
        # Opponent move. Can be random, bot, or manual (human controlled)
        if self.first_player:
            if self.opponent == 'random':
                skip, opp_action = self.check_would_win(Player.P2.value)
                if skip:
                    self.perform_move(opp_action, Player.P2.value)
                    return np.array(self.state), -75, True, {}
                else:
                    skip, opp_action = self.check_would_win(Player.P1.value)
                if skip:
                    pass
                else:
                    opp_action = -1
                    if self.count % 100000 == 0 and self.count <= 500000:
                        self.probs = self.remake_probs()
                    elif 600000 < self.count <= 800000:
                        if 1 not in self.probs:
                            self.probs = [0, 0, 0, 0, 0, 0, 0]
                            idx = np.random.choice(self.action_spaces)
                            self.probs[idx] = 1
                        while self.probs.index(True) in self.illegal:
                            self.probs = [0, 0, 0, 0, 0, 0, 0]
                            idx = np.random.choice(self.action_spaces)
                            self.probs[idx] = 1
                    elif 800000 < self.count <= 1000000:
                        if self.last_ai_move in self.illegal:
                            while opp_action in self.illegal:
                                opp_action = np.random.choice(self.action_spaces)
                        else:
                            self.probs = [0, 0, 0, 0, 0, 0, 0]
                            self.probs[self.last_ai_move] = 1
                    else:
                        self.probs = [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7]
                    while opp_action in self.illegal:
                        opp_action = np.random.choice(self.action_spaces, p=self.probs)
            elif self.opponent == 'self':
                raise NotImplementedError('Self is not implemented yet')
            elif self.opponent == 'human':
                opp_action = int(input('Give a column number 1-7: ')) -1
            else:
                raise ValueError('Opponent must be properly specified')

            last_played = self.perform_move(opp_action, Player.P2.value)
            self.update_legal_moves(opp_action)
            self.done, reward = self.check_win_condition(last_played, opp_action, Player.P2.value)
            self.first_player = False
            if self.done:
                self.state = self.board

        # AI Bot Turn
        else:
            if action not in self.illegal:
                # If move is legal, do it
                last_played = self.perform_move(action, Player.P1.value)
                self.last_ai_move = action
                self.update_legal_moves(action)
                self.done, reward = self.check_win_condition(last_played, action, Player.P1.value)
                self.state = self.board
                reward = reward + 1
            else:
                # Punish illegal moves heavily
                reward = -100
            self.first_player = True
        return np.array(self.state), reward, self.done, {}

    def seed(self, seed=None):
        return

    def reset(self):
        self.board = np.zeros(HEIGHT * WIDTH).reshape(HEIGHT, WIDTH)
        self.observation_space = spaces.Box(-1, 1, shape=(6,7))
        self.state = self.board
        self.done = False
        self.current_player = Player.P1.value
        self.action_space = spaces.Discrete(7)
        self.action_spaces = [0, 1, 2, 3, 4, 5, 6]
        self.first_player = np.random.choice([True,False])
        self.illegal = [None, -1]
        if 600000 < self.count <= 800000:
            idx = np.random.choice(self.action_spaces)
            self.probs = [0, 0, 0, 0, 0, 0, 0]
            self.probs[idx] = 1
        return np.array(self.state)

    def render(self, mode='human', close=False):
        print(self.board)
        print("")

    def remake_probs(self):
        return np.random.dirichlet(np.ones(7))

    def get_row_number(self, action):
        chosen_col = self.board[:, action]
        for i in range(len(chosen_col)):
            if int(chosen_col[6 - i - 1]) == 0:
                return 6 - i - 1

    def perform_move(self, action, player_num):
        """ Assumes that the move is legal """
        location = self.get_row_number(action)
        chosen_col = self.board[:, action]
        chosen_col[location] = player_num
        return location

    def check_win_condition(self, last_played, action, player_val):
        tie = False
        done = False
        filled = False
        count = 1

        # Check if board is filled
        if Player.Empty.value not in self.board:
            filled = True

        done = self.check_d1(last_played, action, player_val)
        done = done or self.check_d2(last_played, action, player_val)
        done = done or self.check_horizontal(last_played, player_val)
        done = done or self.check_vertical(action, player_val)

        # Tie condition gives 0 reward
        if filled and not done:
            return True, 0

        if done:
            # Game won by player = 1 reward; won by opponent = -1
            return True, (75 * player_val)
        else:
            # Game not done. Reward = 0
            return False, 0

    def check_d1(self, row, col, player_val, would_win = False):
        start_r = row - min(row, col)
        start_c = col - min(row, col)
        count = 0
        while start_r < HEIGHT and start_c < WIDTH:
            if self.board[start_r, start_c] == player_val or (would_win and row == start_r and col == start_c):
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
            start_r = start_r + 1
            start_c = start_c + 1
        return False

    def check_d2(self, row, col, player_val, would_win = False):
        start_r = row + min(HEIGHT - row - 1, col)
        start_c = col - min(HEIGHT - row - 1, col)
        count = 0
        while start_r >= 0 and start_c < WIDTH:
            if self.board[start_r, start_c] == player_val or (would_win and row == start_r and col == start_c):
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
            start_r = start_r - 1
            start_c = start_c + 1
        return False
    
    def check_horizontal(self, row, player_val, would_win = False, col = 0):
        r = self.board[row,:]
        #print(r)
        count = 0
        for i in range(7):
            #print(i)
            #print(r[i])
            if r[i] == player_val or (would_win and i == col):
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
        return False
            #if would_win:
                #return (((r[i] == player_val) + (r[i + 1] == player_val) +
                    #(r[i + 2] == player_val) +  (r[i + 3] == player_val)) == 3) and\
                    #((i == col) or (i + 1 == col) or (i + 2 == col) or (i + 3 == col))
            #if r[i] == r[i + 1] == r[i + 2] == r[i + 3] == player_val:
                #return True
        #return False

    def check_vertical(self, column, player_val, would_win = False, row = 0):
        col = self.board[:,column]
        if would_win:
            return col[row + 1] == col[row + 2] == col[row + 3] == player_val
        for i in range(3):
            if col[i] == col[i + 1] == col[i + 2] == col[i + 3] == player_val:
                return True
        return False
    
    def update_legal_moves(self, col):
        if not np.any(self.board[:,col] == 0) and col not in self.illegal:
            self.illegal.append(col)
