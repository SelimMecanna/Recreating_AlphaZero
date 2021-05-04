import random


class TreeNode:
    def __init__(self, game, model):
        self.state = game.current_state.copy()
        # self.policy = model.predict(self.state)[1][*self.valid_actions]
        # self.state_value = model.predict(self.state)
        self.policy = {act: 1 / len(game.get_valid_actions()) for act in range(len(game.get_valid_actions()))}
        self.state_value = random.random() * 2 - 1

        self.action_values = {act: 0 for act, val in enumerate(game.get_valid_actions()) if val}
        self.passes = self.action_values.copy()
        self.children = {}
        self.parent = None

    def add_child(self, child, action):
        child.parent = self
        self.children[action] = child
