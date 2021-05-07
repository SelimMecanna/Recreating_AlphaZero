
class TreeNode:
    def __init__(self, game, model):
        self.state = game.current_state.copy().reshape((-1, game.STATE_DEPTH, *game.BOARD_SIZE))
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
            predicted_value, predicted_policy = model.predict(self.state)
            self.policy = {act: policy for act, policy in enumerate(predicted_policy.squeeze())}
            self.state_value = float(predicted_value.squeeze())
            self.action_values = {act: 0 for act, val in enumerate(game.get_valid_actions()) if val}
            self.passes = self.action_values.copy()

    def add_child(self, child, action):
        child.parent = self
        self.children[action] = child
