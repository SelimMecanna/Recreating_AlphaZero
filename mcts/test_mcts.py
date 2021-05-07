import pytest
import math

from game.connect4 import Connect4
from mcts.mcts_helpers import simulate_mcts
from mcts.tree import TreeNode
from neuralnet.nnet_utils import build_model

n = 10000
game = Connect4()
model = build_model(game.current_state.shape, 7)
# game.play_move(3)
# game.play_move(3)
# game.play_move(2)
# game.play_move(0)
# game.play_move(4)
# game.play_move(0)
node = TreeNode(game, model)

for _ in range(n):
    simulate_mcts(node, game, model)
    game = Connect4()
    # game.play_move(3)
    # game.play_move(3)
    # game.play_move(2)
    # game.play_move(0)
    # game.play_move(4)
    # game.play_move(0)


@pytest.mark.parametrize("node", [node])
def test_passes(node):
    for act, child in node.children.items():
        if not node.children[act].is_terminal:
            assert node.passes[act] == sum(node.children[act].passes.values()) + 1
        test_passes(node.children[act])


@pytest.mark.parametrize("node", [node])
def test_actions(node):
    if node.parent:
        reversed_children = {v: k for k, v in node.parent.children.items()}
        action = reversed_children[node]
        n_pass = node.parent.passes[action]

    if node.is_terminal:
        v = -n_pass * node.state_value
    else:
        v = -node.state_value

    for act, child in node.children.items():
        v1 = test_actions(node.children[act])
        v += v1

    if node.parent:
        assert math.isclose(v / n_pass, node.parent.action_values[action])

    return -v
