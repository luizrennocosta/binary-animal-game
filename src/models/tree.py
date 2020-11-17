import logging
from .node import Node


class BinaryTree:
    """Simple BinaryTree class with simple append and modify node methods"""

    def __init__(self, tree_example=None) -> None:
        """Initializes the binary tree with a root empty node

        Args:
            tree_example (str, optional): A string that defines a sample tree
            to load. Defaults to None.
        """
        self.nodes = list()
        self.reverse_index = {}
        if tree_example == "rd":
            self.nodes.append(Node("Seu Animal vive na água?"))
            self.append_node(0, "Macaco", "Peixe")
        else:
            self.nodes.append(Node())

    def __repr__(self) -> str:
        """Prints all tree's nodes

        Returns:
            str: A string composed of the node's content and left and right 
            nodes content
        """
        _str = ""
        for n in self.nodes:
            _str += f"node {n}\n"
        return _str

    def append_node(self, base_node, left_node, right_node) -> None:
        """Appends a left and right nodes to a specific node numerically 
        defined by base_node

        Args:
            base_node (int): The node's index on the `nodes` list
            left_node (string): The left node's content.
            right_node (string): The left node's content.
        """
        logging.debug("Update dict:")
        logging.debug({left_node: len(self.nodes), right_node: len(self.nodes) + 1})
        self.reverse_index.update(
            {left_node: len(self.nodes), right_node: len(self.nodes) + 1}
        )
        self.nodes.append(Node(left_node))
        self.nodes.append(Node(right_node))
        self.nodes[base_node].left = self.nodes[-2]
        self.nodes[base_node].right = self.nodes[-1]

    def change_node_content(self, base_node, content) -> None:
        """Changes the content of a specific node numerically defined by base_node

        Args:
            base_node (int): The node's index on the `nodes` list
            content (str): The node's content
        """
        self.nodes[base_node].set_content(content)