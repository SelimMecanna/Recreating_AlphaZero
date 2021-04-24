import numpy as np


class Connect4:
    BOARD_SIZE = (6, 7)
    STATE_DEPTH = 5
    CONNECT = 4

    def __init__(self):
        self._current_state = np.zeros((Connect4.STATE_DEPTH, *Connect4.BOARD_SIZE))
        self._current_state[1] = np.ones(Connect4.BOARD_SIZE)
        self._current_state[-2] = np.ones(Connect4.BOARD_SIZE)
        self._visited_states = []

    def get_valid_actions(self):
        return [bool(s) for s in self._current_state[1, 0, :]]

    def is_terminated(self):
        winning_array = np.ones(Connect4.CONNECT)
        winning_string = ''.join(str(i) for i in winning_array)
        if self._current_state[-2] == np.ones(Connect4.BOARD_SIZE):
            player_position = self._current_state[2]
        else:
            player_position = self._current_state[0]

        # Check Horizontal:
        for i in range(Connect4.BOARD_SIZE[0]):
            return consecutive_ones(winning_string, player_position[i])

        # Check Vertical:
        for i in range(Connect4.BOARD_SIZE[1]):
            return consecutive_ones(winning_string, player_position[:, i])

        # Check diagonal \:
        for i in range(Connect4.CONNECT - Connect4.BOARD_SIZE[0], Connect4.BOARD_SIZE[1] - Connect4.CONNECT + 1):
            return consecutive_ones(winning_string, player_position[:, i])

        # Check diagonal /:
        for i in range(Connect4.CONNECT - Connect4.BOARD_SIZE[0], Connect4.BOARD_SIZE[1] - Connect4.CONNECT + 1):
            return consecutive_ones(winning_string, np.fliplr(player_position).diagonal(i))

        return False

    def play_move(self, move):
        pass


def consecutive_ones(string, array):
    joint_array = ''.join(str(j) for j in array)
    if string in joint_array:
        return True


if __name__ == "__main__":
    firstgame = Connect4()
    print(firstgame._current_state)
    print(firstgame.get_valid_actions())
    firstgame._current_state[0, 0, 4:6] = 1
    firstgame._current_state[2, 0, 2] = 1
    print(firstgame._current_state)
    print(firstgame.get_valid_actions())
