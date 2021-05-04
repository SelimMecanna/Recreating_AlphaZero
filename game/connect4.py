import numpy as np
import sys


class Connect4:
    BOARD_SIZE = (6, 7)
    STATE_DEPTH = 5
    CONNECT = 4

    def __init__(self):
        self.current_state = np.zeros((Connect4.STATE_DEPTH, *Connect4.BOARD_SIZE))
        self.current_state[1] = np.ones(Connect4.BOARD_SIZE)
        self.current_state[-2] = np.ones(Connect4.BOARD_SIZE)
        self._visited_states = []

    def get_valid_actions(self):
        return [bool(s) for s in self.current_state[1, 0, :]]

    def is_terminated(self):
        winning_array = np.ones(Connect4.CONNECT)
        winning_string = ''.join(str(i) for i in winning_array)
        if np.all(self.current_state[-2]):
            player_position = self.current_state[2]
        else:
            player_position = self.current_state[0]

        # Check Horizontal:
        for i in range(Connect4.BOARD_SIZE[0]):
            if consecutive_ones(winning_string, player_position[i]):
                return True, -1.

        # Check Vertical:
        for i in range(Connect4.BOARD_SIZE[1]):
            if consecutive_ones(winning_string, player_position[:, i]):
                return True, -1.

        # Check diagonal \:
        for i in range(Connect4.CONNECT - Connect4.BOARD_SIZE[0], Connect4.BOARD_SIZE[1] - Connect4.CONNECT + 1):
            if consecutive_ones(winning_string, player_position.diagonal(i)):
                return True, -1.

        # Check diagonal /:
        for i in range(Connect4.CONNECT - Connect4.BOARD_SIZE[0], Connect4.BOARD_SIZE[1] - Connect4.CONNECT + 1):
            if consecutive_ones(winning_string, np.fliplr(player_position).diagonal(i)):
                return True, -1.

        if all([not ele for ele in self.get_valid_actions()]):
            return True, 0.

        return False, None

    def play_move(self, move):
        if move not in range(0, Connect4.BOARD_SIZE[1] + 1):
            raise ValueError(f"move {move} is out of bounds")

        if not self.get_valid_actions()[move]:
            raise ValueError(f"move {move} is not a valid move")

        if np.all(self.current_state[-2]):
            current_player_indices = (0, -2)
            opposing_player_index = -1
        else:
            current_player_indices = (2, -1)
            opposing_player_index = -2

        drop_index = Connect4.BOARD_SIZE[0] - 1

        while not self.current_state[1, drop_index, move]:
            drop_index -= 1

        self._visited_states.append(self.current_state.copy())

        self.current_state[1, drop_index, move] = 0.
        self.current_state[current_player_indices[0], drop_index, move] = 1.
        self.current_state[current_player_indices[1]] = np.zeros(Connect4.BOARD_SIZE)
        self.current_state[opposing_player_index] = np.ones(Connect4.BOARD_SIZE)


def consecutive_ones(string, array):
    joint_array = ''.join(str(j) for j in array)
    if string in joint_array:
        return True
