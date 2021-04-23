import numpy as np


class Connect4:
    BOARD_SIZE = (6, 7)
    STATE_DEPTH = 5

    def __init__(self):
        self._current_state = np.zeros((Connect4.STATE_DEPTH, *Connect4.BOARD_SIZE))
        self._current_state[1] = np.ones(Connect4.BOARD_SIZE)
        self._current_state[-2] = np.ones(Connect4.BOARD_SIZE)
        self.visited_states = []

    def get_valid_actions(self):
        full_columns = self._current_state[0, 0, :] + self._current_state[2, 0, :]

        return [not bool(s) for s in full_columns]

    def is_terminated(self):



if __name__ == "__main__":
    firstgame = Connect4()
    print(firstgame._current_state)
    print(firstgame.get_valid_actions())
    firstgame._current_state[0, 0, 4:6] = 1
    firstgame._current_state[2, 0, 2] = 1
    print(firstgame._current_state)
    print(firstgame.get_valid_actions())
