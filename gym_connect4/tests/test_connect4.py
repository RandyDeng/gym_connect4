import pytest

import gym
import gym_connect4

from gym_connect4.envs.connect4 import Player

import numpy as np


ENV = gym.make('gym_connect4:Connect4VsRandomBot-v0')


@pytest.mark.parametrize('board, columns, expected', [
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]),
     [0, 1, 2, 3, 4, 5, 6],
     [False, False, False, False, False, False, False]),
    (np.array([[1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]),
     [0, 1, 2, 3, 4, 5, 6],
     [True, True, True, True, True, True, True]),
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0]]),
     [0, 1, 2, 3, 4, 5, 6],
     [True, True, True, True, True, True, True]),
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1]]),
     [0, 1, 2, 3, 4, 5, 6],
     [True, True, True, True, True, True, True]),
    (np.array([[1, 1, 0, 0, 1, 1, 0],
               [1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 0, 1, 1, 1],
               [1, 0, 0, 1, 1, 1, 0],
               [1, 0, 1, 0, 0, 0, 1],
               [1, 0, 1, 1, 1, 0, 1]]),
     [0, 1, 2, 3, 4, 5, 6],
     [False, False, False, False, True, True, False]),
])
def test_check_vertical_col(board, columns, expected):
    ENV.board = board
    for i in range(len(columns)):
        actual = ENV.check_vertical(columns[i], Player.P1.value)
        assert actual == expected[i]


@pytest.mark.parametrize('board, rows, expected', [
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]),
     [0, 1, 2, 3, 4, 5],
     [False, False, False, False, False, False]),
    (np.array([[1, 1, 1, 1, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0]]),
     [0, 1, 2, 3, 4, 5],
     [True, True, True, True, True, True]),
    (np.array([[0, 1, 1, 1, 1, 0, 0],
               [0, 1, 1, 1, 1, 0, 0],
               [0, 1, 1, 1, 1, 0, 0],
               [0, 1, 1, 1, 1, 0, 0],
               [0, 1, 1, 1, 1, 0, 0],
               [0, 1, 1, 1, 1, 0, 0]]),
     [0, 1, 2, 3, 4, 5],
     [True, True, True, True, True, True]),
    (np.array([[0, 0, 1, 1, 1, 1, 0],
               [0, 0, 1, 1, 1, 1, 0],
               [0, 0, 1, 1, 1, 1, 0],
               [0, 0, 1, 1, 1, 1, 0],
               [0, 0, 1, 1, 1, 1, 0],
               [0, 0, 1, 1, 1, 1, 0]]),
     [0, 1, 2, 3, 4, 5],
     [True, True, True, True, True, True]),
    (np.array([[0, 0, 0, 1, 1, 1, 1],
               [0, 0, 0, 1, 1, 1, 1],
               [0, 0, 0, 1, 1, 1, 1],
               [0, 0, 0, 1, 1, 1, 1],
               [0, 0, 0, 1, 1, 1, 1],
               [0, 0, 0, 1, 1, 1, 1]]),
     [0, 1, 2, 3, 4, 5],
     [True, True, True, True, True, True]),
    (np.array([[0, 1, 1, 1, 0, 0, 0],
               [0, 1, 0, 1, 1, 1, 0],
               [0, 0, 1, 0, 1, 1, 1],
               [0, 1, 1, 1, 1, 0, 0],
               [1, 1, 1, 0, 0, 1, 1],
               [0, 1, 0, 1, 1, 1, 0]]),
     [0, 1, 2, 3, 4, 5],
     [False, False, False, True, False, False]),
])
def test_check_horizontal(board, rows, expected):
    ENV.board = board
    for i in range(len(rows)):
        actual = ENV.check_horizontal(rows[i], Player.P1.value)
        assert actual == expected[i]


@pytest.mark.parametrize('board, row_col, expected', [
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0]]),
     [(2, 0), (3, 1), (4, 2), (5, 3)],
     [True, True, True, True]),
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]),
     [(1, 0), (2, 1), (3, 2), (4, 3)],
     [True, True, True, True]),
    (np.array([[1, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]),
     [(0, 0), (1, 1), (2, 2), (3, 3)],
     [True, True, True, True]),
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 1]]),
     [(2, 3), (3, 4), (4, 5), (5, 6)],
     [True, True, True, True]),
    (np.array([[0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]),
     [(0, 3), (1, 4), (2, 5), (3, 6)],
     [True, True, True, True]),
    (np.array([[0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 0],
               [0, 1, 1, 1, 0, 0, 1],
               [0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0]]),
     [(0, 1), (0, 2), (0, 3),
      (1, 1), (1, 2), (1, 3),
      (2, 1), (2, 2), (1, 3),
      (3, 1), (3, 2), (3, 3),],
     [False, False, False,
      False, False, False,
      False, False, False,
      False, False, False,])
])
def test_check_d1(board, row_col, expected):
    ENV.board = board
    for i in range(len(row_col)):
        row, col = row_col[i]
        actual = ENV.check_d1(row, col, Player.P1.value)
        assert actual == expected[i]


@pytest.mark.parametrize('board, row_col, expected', [
    (np.array([[0, 0, 0, 1, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]),
     [(3, 0), (2, 1), (1, 2), (0, 3)],
     [True, True, True, True]),
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]),
     [(4, 0), (3, 1), (2, 2), (1, 3)],
     [True, True, True, True]),
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0]]),
     [(5, 0), (4, 1), (3, 2), (2, 3)],
     [True, True, True, True]),
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0]]),
     [(5, 1), (4, 2), (3, 3), (2, 4)],
     [True, True, True, True]),
    (np.array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0, 0, 0]]),
     [(5, 3), (4, 4), (3, 5), (2, 6)],
     [True, True, True, True]),
    (np.array([[0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 0],
               [0, 1, 1, 1, 0, 0, 1],
               [0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0]]),
     [(0, 1), (0, 2), (0, 3),
      (1, 1), (1, 2), (1, 3),
      (2, 1), (2, 2), (1, 3),
      (3, 1), (3, 2), (3, 3),],
     [False, False, False,
      False, False, False,
      False, False, False,
      False, False, False,])
])
def test_check_d2(board, row_col, expected):
    ENV.board = board
    for i in range(len(row_col)):
        row, col = row_col[i]
        actual = ENV.check_d2(row, col, Player.P1.value)
        assert actual == expected[i]
