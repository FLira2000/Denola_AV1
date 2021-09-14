from GenTree import GenTree

class Application:
    def __init__(self):
        self.trees = []

    def add_tree_from_file(self):
        filepath = input('Entre com o nome do arquivo: ')
        try:
            self.trees.append(GenTree(file_path=filepath))
        except BaseException as e:
            print(f'Algo ocorreu na leitura do arquivo. ERR: {e}')

    def print_trees():
        _ = [print(tree) for tree in self.trees]

    def create_new_tree(self):
        pass
