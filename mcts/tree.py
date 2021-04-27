class TreeNode:
    def __init__(self, game, model):
        self.state = game.current_state
        self.valid_actions = game.get_valid_actions
        self.policy = model.predict(self.state)[1][*self.valid_actions]
        self.state_value = model.predict(self.state)

        valid_actions_number = sum(self.valid_actions)

        self.action_values = [0]*valid_actions_number
        self.passes = [0]*valid_actions_number
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    

    
