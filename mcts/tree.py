import random


class TreeNode:
    def __init__(self, game, model):
        self.state = game.current_state.copy()
        self.parent = None
        self.children = {}
        game_status, return_value = game.is_terminated()
        self.is_terminal = game_status

        if self.is_terminal:
            self.policy = {}
            self.state_value = return_value
            self.action_values = {}
            self.passes = {}

        else:
            self.policy = {act: 1 / len(game.get_valid_actions()) for act in range(len(game.get_valid_actions()))}
            self.state_value = random.random() * 2 - 1
            self.action_values = {act: 0 for act, val in enumerate(game.get_valid_actions()) if val}
            self.passes = self.action_values.copy()

    def add_child(self, child, action):
        child.parent = self
        self.children[action] = child
