from math import sqrt
import random
from mcts.tree import TreeNode


def simulate_mcts(tree_node, game, model):
    if tree_node.is_terminal:
        return -tree_node.state_value

    if not tree_node.children:
        if tree_node.parent:
            reversed_children = {v: k for k, v in tree_node.parent.children.items()}
            action = reversed_children[tree_node]
            if not tree_node.parent.passes[action]:
                return -tree_node.state_value
        action = random.choice(list(tree_node.action_values))
        game.play_move(action)
        new_node = TreeNode(game, model)
        tree_node.add_child(new_node, action)
        tree_node.action_values[action] = (tree_node.action_values[action] * tree_node.passes[
            action] - new_node.state_value) / (tree_node.passes[action] + 1)
        tree_node.passes[action] += 1

        return new_node.state_value

    max_ucb = -float('inf')
    picked_action = -1
    cpuct = 4
    for act in tree_node.action_values.keys():
        ucb = tree_node.action_values[act] + cpuct * tree_node.policy[act] * (sqrt(sum(tree_node.passes.values()))) / (
                tree_node.passes[act] + 1)
        if ucb > max_ucb:
            max_ucb = ucb
            picked_action = act

    game.play_move(picked_action)

    if picked_action in tree_node.children.keys():
        new_node = tree_node.children[picked_action]

    else:
        new_node = TreeNode(game, model)
        tree_node.add_child(new_node, picked_action)

    v = simulate_mcts(new_node, game, model)

    tree_node.action_values[picked_action] = (tree_node.action_values[picked_action] * tree_node.passes[
        picked_action] + v) / (tree_node.passes[picked_action] + 1)

    tree_node.passes[picked_action] += 1

    return -v
