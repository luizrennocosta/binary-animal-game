from controllers.controller import GameController
from models.tree import BinaryTree
import logging

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    rd_tree = BinaryTree("rd")
    game = GameController(rd_tree)
    game.new_game()
