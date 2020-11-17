import click


class GameController:
    def __init__(self, tree):
        """Initializes the controller with a given binary tree

        Args:
            tree (BinaryTree): A BinaryTree object.
        """
        self.tree = tree

    def ask_player(self, question, default=None):
        """Creates a question expecting an answer from the player.

        Args:
            question (str): A question to ask the player.
            default (str, optional): A default answer in case the player enters nothing. Defaults to None.

        Returns:
            str: Returns the player's response.
        """
        resp = click.prompt(question, type=str, default=default)
        if resp == "exit":
            self.exit_game()
        return resp

    def insert_new_question(self, relevant_node):
        """Inserts a new question in the tree. Along with its yes/no answers (nodes).

        Args:
            relevant_node (models.Node): The reference node to spawn the new nodes from.
        """
        node_to_change = self.tree.reverse_index[relevant_node.get_content()]
        animal = self.ask_player("Em qual animal você pensou?")
        difference = self.ask_player(
            f"O que o/a {animal} faz que o/a {relevant_node.get_content()} não faz?"
        )
        self.tree.append_node(node_to_change, relevant_node.get_content(), animal)
        self.tree.change_node_content(node_to_change, f"Seu animal {difference}?")

    def exit_game(self):
        """Exits the game
        """
        print("Obrigado por jogar!!!")
        exit(0)

    def process_node(self, current_node):
        """Processes a node, creating a new question if needed, 
        or walking through the tree when the player answers a question.

        Args:
            current_node (models.Node): The tree's current node to process.

        Returns:
            models.Node: Returns the new current node. Can be the root node
            (indicated by a 0 return) or a new node after answering a question
        """
        if current_node.get_content() in self.tree.reverse_index:
            # If node is an Animal node, at the end of the tree
            resp = self.ask_player(
                f"O seu animal é o {current_node.get_content()}?", default="n"
            )
            userResponse = resp.lower()[0]
            if userResponse == "n":
                self.insert_new_question(current_node)
                current_node = 0
            elif userResponse == "s":
                print("Acertei")
                current_node = 0
            else:
                print("Resposta inválida, insira s ou n")
        else:
            # If node is a Question node
            resp = self.ask_player(current_node.get_content(), default="N")
            left_node = current_node.get_left()
            right_node = current_node.get_right()
            node_dictionary_response = {
                "n": left_node,
                "s": right_node,
            }
            try:
                current_node = node_dictionary_response[resp.lower()[0]]
            except KeyError:
                print("Resposta inválida, insira S ou N")
        return current_node

    def new_game(self):
        """Initiates a new game
        """
        current_node = 0
        while True:
            if current_node == 0:
                self.ask_player(
                    "Pense em um animal, digite OK para continuar, ou exit a qualquer momento para sair",
                    default="OK",
                )
                current_node = self.tree.nodes[current_node]

            current_node = self.process_node(current_node)
