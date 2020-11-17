
class Node:
    """
    Simple Node Class for a Binary Tree
    """

    def __init__(self, content=None) -> None:
        """
            Node constructor with content
        """
        self.left = None
        self.right = None
        self.content = content

    def __repr__(self) -> str:
        """
            Prints node's content and left/right nodes as well
        """
        return f"content: {self.content}, left: {self.left}, right: {self.right}"

    def add_left(self, left_node):
        """
            Adds a left node
        """
        self.left = left_node

    def add_right(self, right_node):
        """
            Adds a right node
        """
        self.right = right_node

    def get_content(self):
        """
        Returns node content
        """
        return self.content

    def get_left(self):
        """
        Returns left node
        """
        return self.left

    def get_right(self):
        """
        Returns right node
        """
        return self.right

    def set_content(self, content):
        """
        Changes node content
        """
        self.content = content
