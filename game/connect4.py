import numpy as np


class Connect4:
    BOARD_SIZE = (6, 7)
    STATE_DEPTH = 5

    def __init__(self):
        self.current_state = np.zeros((Connect4.STATE_DEPTH, *Connect4.BOARD_SIZE))
        self.current_state[1] = np.ones(Connect4.BOARD_SIZE)
        self.current_state[-2] = np.ones(Connect4.BOARD_SIZE)
        self.visited_states = []


if __name__ == "__main__":
    firstgame = Connect4()
    print(firstgame.current_state)
